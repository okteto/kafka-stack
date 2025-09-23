from kafka import KafkaConsumer

topic_name = 'messages'

if __name__ == '__main__':
  print('Starting consumer...')
  consumer = KafkaConsumer(topic_name, bootstrap_servers='kafka:19092')
  
  print('receiving messages...')
  for message in consumer:
      print(f'received message {message}')

  print('exiting...')