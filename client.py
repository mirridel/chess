import json
import socket
import chess

username = 'mirridel'
user = {'username': username}
turn_message = {'username': username, 'message': 'move', 'move': ''}

def print_board(board):
    count = 8
    out = ["A B C D E F G H\n",
           "----------------\n"]
    txt = board.split("\n")
    for t in txt:
        out.append("{} | {}\n".format(t, count))
        count -= 1
    print("".join(out))

def client_program():
    host = "localhost"  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    wrapper = json.dumps(user)
    client_socket.send(wrapper.encode())  # send message

    input_data = client_socket.recv(1024)
    _input = json.loads(input_data.decode())

    if _input['message'] == 'wait':
        print("Please wait!")

    while _input["message"] != 'start':
        input_data = client_socket.recv(1024)
        _input = json.loads(input_data.decode())
        print(_input)

    while True:
        input_data = client_socket.recv(1024)
        _input = json.loads(input_data.decode())
        print(_input)
        fen_board = _input['board']
        print_board(chess.Board(fen_board).__str__())

        if _input['server_message'] == 'turn':
            output_message = input(" -> ")  # take input
            turn_message['move'] = output_message
            print(turn_message)
            wrapper = json.dumps(turn_message)
            client_socket.send(wrapper.encode())  # send message
            while True:
                input_data = client_socket.recv(1024)
                _input = json.loads(input_data.decode())
                if _input['message'] == 'okay':
                    break
                else:
                    output_message = input(" -> ")  # take input
                    turn_message['move'] = output_message
                    print(turn_message)
                    wrapper = json.dumps(turn_message)
                    client_socket.send(wrapper.encode())  # send message
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
