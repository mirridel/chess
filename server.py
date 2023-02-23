import json
import socket
import threading
import chess

ServerSideSocket = socket.socket()
host = 'localhost'
port = 5000
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)

room = {'first_player': {'username': '', 'connection': ''},
        'second_player': {'username': '', 'connection': ''}}


def game_engine():
    first_player = room['first_player']
    second_player = room['second_player']

    board = chess.Board()

    example = {'username': '', 'board': '', 'server_message': 'wait'}

    while True:

        example['board'] = board.fen()
        print(board)
        print(board.pseudo_legal_moves)

        """
        TRUE - белые
        FALSE - черные
        """
        if board.turn:
            print("Ход: БЕЛЫЕ")
            target_player = first_player
            another_player = second_player
        else:
            print("Ход: ЧЕРНЫЕ")
            target_player = second_player
            another_player = first_player

        mess = example
        mess['username'] = target_player['username']
        mess['server_message'] = 'turn'
        wrapper = json.dumps(mess)
        # print(wrapper)
        target_player['connection'].send(wrapper.encode())

        mess = example
        mess['username'] = another_player['username']
        mess['server_message'] = 'wait'
        wrapper = json.dumps(mess)
        # print(wrapper)
        another_player['connection'].send(wrapper.encode())

        while True:
            input_data = target_player['connection'].recv(2048)
            input_message = json.loads(input_data.decode())
            if input_message['message'] == 'move':
                try:
                    move = chess.Move.from_uci(input_message['move'])
                    #print("Move: {}".format(move))
                    #print(move in board.legal_moves)
                    if move in board.pseudo_legal_moves:
                        board.push(move)
                    output_message = {'message': 'okay'}
                    wrapper = json.dumps(output_message)
                    target_player['connection'].send(wrapper.encode())
                    break
                except:
                    output_message = {'message': 'error'}
                    wrapper = json.dumps(output_message)
                    target_player['connection'].send(wrapper.encode())


class multi_threaded_client(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection

    def run(self):
        while True:
            data = self.connection.recv(2048)
            wrapper = json.loads(data.decode())
            print(wrapper['username'])

            if room['first_player']['username'] == '':
                room['first_player']['username'] = wrapper['username']
                room['first_player']['connection'] = self.connection
                output_message = {'message': 'wait'}
                wrapper = json.dumps(output_message)
                self.connection.send(wrapper.encode())

            elif room['second_player']['username'] == '':
                room['second_player']['username'] = wrapper['username']
                room['second_player']['connection'] = self.connection
                output_message = {'message': 'wait'}
                wrapper = json.dumps(output_message)
                self.connection.send(wrapper.encode())

                output_message = {'message': 'start'}
                wrapper = json.dumps(output_message)
                room['first_player']['connection'].send(wrapper.encode())
                room['second_player']['connection'].send(wrapper.encode())
                print(room)
            break


"""
    connection.close()
"""

threadLock = threading.Lock()
threads = []

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    work = multi_threaded_client(Client)
    work.start()
    threads.append(work)

    if len(threads) == 2:
        work.join()
        break

game_engine()

ServerSideSocket.close()
