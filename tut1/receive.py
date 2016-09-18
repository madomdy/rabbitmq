import pika

rabbit_host = '172.18.204.35'

connection = pika.BlockingConnection(pika.ConnectionParameters(
    rabbit_host
))

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print('[x] Received %r' % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
