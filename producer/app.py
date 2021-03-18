from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:9092')

@app.route('/', methods=["POST"])
def send():
    app.logger.info("received message")
    content = request.get_json()
    jd = json.dumps(content).encode('utf-8')
    producer.send('messages', jd)
    app.logger.info("sent message")
    return jsonify({"status":"ok"})

if __name__ == '__main__':
  app.logger.info('Starting server...')
  app.run(host='0.0.0.0', port=8080)