from kafka import KafkaConsumer

if __name__ == '__main__':
  print('Starting consumer...')
  consumer = KafkaConsumer('messages', bootstrap_servers='kafka:9092')
  
  print('receiving messages...')
  for message in consumer:
      print(f'received message {message}')

  print('exiting...')