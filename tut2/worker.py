import pika
import time

rabbit_host = '172.18.204.35'

connection = pika.BlockingConnection(pika.ConnectionParameters(
    rabbit_host
))

channel = connection.channel()

channel.queue_declare(queue='durable_task_queue', durable=True)

def callback(ch, method, properties, body):
    print('[x] Received %r' % body)
    time.sleep(body.count(b'.'))
    print("[x] Task is done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='task_queue')

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
