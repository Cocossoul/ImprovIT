import pika
import sys

host = sys.argv[1]

connection = pika.BlockingConnection(pika.URLParameters(host))
channel = connection.channel()
channel.queue_declare(queue='wol')

channel.basic_publish(exchange='',
                      routing_key='wol',
                      body='wake up',
                      )

connection.close()
