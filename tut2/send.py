import pika
import sys

rabbit_host = '172.18.204.35'

connection = pika.BlockingConnection(pika.ConnectionParameters(
    rabbit_host
))

channel = connection.channel()
channel.queue_declare(queue='durable_task_queue', durable=True)
message = ' '.join(sys.argv[1:]) or 'Hello from rabbitmq at %s' % rabbit_host

channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode = 2, # make message persistent, not to
                                             # be lost when rabbitmq dies. the
                                             # same idea as with `durable=True`
                                             # option in queue declaring
                      ))
print("[x] The message %r is sent" % message)

connection.close()
