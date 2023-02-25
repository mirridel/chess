import json
import threading

import chess


# Формат сообщения: {"message": <>, "information": <>}
def send_message(connection, message, information):
    output_message = {'message': message, 'information': information}
    wrapper = json.dumps(output_message)
    connection.send(wrapper.encode())


class game_engine(threading.Thread):
    def __init__(self, _room):
        threading.Thread.__init__(self)
        self.room = dict(_room)

    def run(self):
        board = chess.Board()

        while True:
            first_player = self.room['first_player']
            second_player = self.room['second_player']

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

            send_message(target_player, 'turn', {'board': board.fen()})
            send_message(another_player, 'wait', {'board': board.fen()})

            while True:
                wrapper = target_player.recv(2048)
                input_message = json.loads(wrapper.decode())
                if input_message['message'] == 'move':
                    try:
                        move = chess.Move.from_uci(input_message['move'])
                        if move in board.pseudo_legal_moves:
                            board.push(move)
                        send_message(target_player, 'move_success', {'board': board.fen()})
                        break
                    except:
                        send_message(target_player, 'error', {'board': board.fen()})
