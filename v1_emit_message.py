"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Denise Case
    Date: January 14, 2023

    Amber Speer
    Streaming Data
    Module 3 Assignment

"""

# add imports at the beginning of the file
import pika

mess1 = "Hello World!"
mess2 = "Hola Vida!"
mess3 = "Howdy ya'll!"
# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=mess1)
# print a message to the console for the user
print(" [x] Sent %r" % mess1)
ch.basic_publish(exchange='', routing_key='hello', body=mess2)
print(" [x] Sent %r" % mess2)
ch.basic_publish(exchange='', routing_key='hello', body=mess3)
print(" [x] Sent %r" % mess3)
# close the connection to the server
conn.close()
