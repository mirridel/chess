import json
import socket
import time
from threading import Thread

import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = 'localhost'
Port = 5000
server.connect((IP_address, Port))


def get_message():
    message = server.recv(2048)
    print(message.decode())


def send_message():
    message = sys.stdin.readline().split("\n")
    output_message = {"message": message[0], "information": {"id": -1, "username": "", "password": "", "secret_question": "", "answer": ""}}
    wrapper = json.dumps(output_message)
    print(wrapper)
    server.send(wrapper.encode())
    time.sleep(1)
    sys.stdout.write("<You>")
    sys.stdout.flush()


while True:
    Thread(target=send_message).start()
    Thread(target=get_message).start()
server.close()

