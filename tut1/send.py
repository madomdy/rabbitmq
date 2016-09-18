import pika

rabbit_host = '172.18.204.35'

connection = pika.BlockingConnection(pika.ConnectionParameters(
    rabbit_host
))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello from rabbitmq at %s' % rabbit_host)
print("[x] The message is sent")

connection.close()
