import socket
import threading

from multithreading.client_engine import multi_threaded_client

ServerSideSocket = socket.socket()
host = 'localhost'
port = 5000

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)

threadLock = threading.Lock()
threads = []
while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    work = multi_threaded_client(Client)
    work.start()
    threads.append(work)
