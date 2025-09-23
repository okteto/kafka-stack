from flask import Flask, request, jsonify
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import time
import sys

app = Flask(__name__)
topic_name = 'messages'

def connect_to_kafka(max_retries=30, retry_delay=2):
    """Connect to Kafka with retry logic"""
    for attempt in range(max_retries):
        try:
            app.logger.info(f'Attempting to connect to Kafka (attempt {attempt + 1}/{max_retries})...')
            producer = KafkaProducer(bootstrap_servers='kafka:9092')
            app.logger.info('Successfully connected to Kafka!')
            return producer
        except NoBrokersAvailable as e:
            app.logger.warning(f'Kafka not available yet, retrying in {retry_delay} seconds... ({e})')
            time.sleep(retry_delay)
        except Exception as e:
            app.logger.error(f'Unexpected error: {e}')
            time.sleep(retry_delay)
    
    app.logger.error(f'Failed to connect to Kafka after {max_retries} attempts')
    sys.exit(1)

# Initialize Kafka producer with retry logic
producer = None

@app.route('/', methods=["POST"])
def send():
    global producer
    if producer is None:
        return jsonify({"error": "Kafka producer not initialized"}), 500
        
    app.logger.info("received message")
    content = request.get_json()
    jd = json.dumps(content).encode('utf-8')
    producer.send(topic_name, jd)
    app.logger.info("sent message")
    return jsonify({"status":"ok"})

if __name__ == '__main__':
    app.logger.info('Starting server...')
    producer = connect_to_kafka()
    app.run(host='0.0.0.0', port=8080)