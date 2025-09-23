from kafka import KafkaConsumer
import time
import sys
from kafka.errors import NoBrokersAvailable

topic_name = 'messages'

def connect_to_kafka(max_retries=30, retry_delay=2):
    """Connect to Kafka with retry logic"""
    for attempt in range(max_retries):
        try:
            print(f'Attempting to connect to Kafka (attempt {attempt + 1}/{max_retries})...')
            consumer = KafkaConsumer(topic_name, bootstrap_servers='kafka:9092')
            print('Successfully connected to Kafka!')
            return consumer
        except NoBrokersAvailable as e:
            print(f'Kafka not available yet, retrying in {retry_delay} seconds... ({e})')
            time.sleep(retry_delay)
        except Exception as e:
            print(f'Unexpected error: {e}')
            time.sleep(retry_delay)
    
    print(f'Failed to connect to Kafka after {max_retries} attempts')
    sys.exit(1)

if __name__ == '__main__':
  print('Starting consumer...')
  consumer = connect_to_kafka()
  
  print('receiving messages...')
  try:
      for message in consumer:
          print(f'received message {message}')
  except KeyboardInterrupt:
      print('Consumer interrupted')
  except Exception as e:
      print(f'Consumer error: {e}')
  finally:
      consumer.close()
      print('exiting...')