import pika
import sys

def wake_up_confirmation(ch, method, properties, body):
    print(f"Recieved message: {body}")
    if body.decode('utf-8') == "waked up":
        connection.close()
        exit(0)
    pass

host = sys.argv[1]

connection = pika.BlockingConnection(pika.URLParameters(host))
channel = connection.channel()
channel.queue_declare(queue='wol')

channel.basic_publish(exchange='',
                      routing_key='wol',
                      properties=pika.BasicProperties(expiration='60000'),
                      body='wake up',
                      )

channel.basic_consume(queue='wol',
                    auto_ack=True,
                    on_message_callback=wake_up_confirmation)
channel.start_consuming()
