import pika
import sys
import os

mac_address = sys.argv[2]

def wake_up_gaming_pc(ch, method, properties, body):
    print(f"Recieved message: {body}")
    if body.decode('utf-8') == "wake up":
        os.system(f"echo Waking up {mac_address}")
        os.system(f"sudo etherwake -i eth0 {mac_address}")
    pass

host = sys.argv[1]

connection = pika.BlockingConnection(pika.URLParameters(host))
channel = connection.channel()
channel.queue_declare(queue='wol')
channel.basic_consume(queue='wol',
                    auto_ack=True,
                    on_message_callback=wake_up_gaming_pc)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
