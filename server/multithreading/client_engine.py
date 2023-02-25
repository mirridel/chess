import json
import threading

from database.database_engine import auth, insert, get_secret_question, change_password
from database.models import Users
from multithreading.game_engine import game_engine
from local_storage import players_queue, online_users, authorized_users


# Формат сообщения: {"message": <>, "information": <>}
def send_message(connection, message, information):
    output_message = {'message': message, 'information': information}
    wrapper = json.dumps(output_message)
    connection.send(wrapper.encode())


class multi_threaded_client(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        self.connection = connection
        self.exitTrigger = True

    """
    РЕГИСТРАЦИЯ
    Формат запроса:
    {"message": "registration",
     "information": {"id": -1,
                     "username": <username>,
                     "password": <password>,
                     "secret_question": <secret_question>,
                     "answer": <answer>}}
                     
    Формат ответа (в случае успеха):
    {"message": "registration_success",
     "information": {"id": <id>,
                     "username": <username>,
                     "secret_question": <secret_question>
                     
    Формат ответа (в случае ошибки):
    {"message": "registration_fail",
     "information": {"id": <id>,
                     "username": <username>,
                     "secret_question": <secret_question>
    """

    def __registration(self, wrapper):
        try:
            if wrapper['information']['username'] != '' and wrapper['information']['password'] != '' and \
                    wrapper['information']['secret_question'] != '' and wrapper['information']['answer'] != '':
                db_message = insert(Users, wrapper['information'])
                send_message(self.connection, 'registration_success', db_message)
        except Exception as ex:
            send_message(self.connection, 'registration_fail', ex.__str__())

    """
    АВТОРИЗАЦИЯ
    Формат запроса:
    {"message": "authorization",
     "information": {"username": <username>,
                     "password": <password>}}

    Формат ответа (в случае успеха):
    {"message": "authorization_success",
     "information": {"id": <id>}}

    Формат ответа (в случае ошибки):
    {"message": "authorization_fail",
     "information": <Exception>}
    """

    def __authorization(self, wrapper):
        try:
            if wrapper['information']['username'] != '' and wrapper['information']['password'] != '':
                db_message = auth(wrapper['information'])
                send_message(self.connection, 'authorization_success', db_message)
                authorized_users[self.connection] = db_message
        except Exception as ex:
            send_message(self.connection, 'authorization_fail', ex.__str__())

    """
    ПОЛУЧЕНИЕ СЕКРЕТНОГО ВОПРОСА
    Формат запроса:
    {"message": "get_secret_question",
     "information": {"username": <username>}

    Формат ответа (в случае успеха):
    {"message": "get_secret_question_success",
     "information": {"secret_question": <secret_question>}}

    Формат ответа (в случае ошибки):
    {"message": "get_secret_question_fail",
     "information": <Exception>}
    """

    def __get_secret_question(self, wrapper):
        try:
            if wrapper['information']['username'] != '':
                db_message = get_secret_question(wrapper['information'])
                send_message(self.connection, 'get_secret_question_success', db_message)
        except Exception as ex:
            send_message(self.connection, 'get_secret_question_fail', ex.__str__())

    """
    СМЕНА ПАРОЛЯ
    Формат запроса:
    {"message": "change_password",
     "information": {"username": <username>,
                     "password": <password>,
                     "answer": <answer>}

    Формат ответа (в случае успеха):
    {"message": "change_password_success",
     "information": {"new_password": <password>}}

    Формат ответа (в случае ошибки):
    {"message": "change_password_fail",
     "information": <Exception>}
    """

    def __change_password(self, wrapper):
        try:
            if wrapper['information']['username'] != '' and wrapper['information']['answer'] != '':
                db_message = change_password(wrapper['information'])
                send_message(self.connection, 'change_password_success', db_message)
        except Exception as ex:
            print(ex)
            send_message(self.connection, 'change_password_fail', ex.__str__())

    def __find_game(self):
        try:
            """
            Забираем первого игрока в очереди.
            """
            if players_queue[0] != self.connection:
                player_from_queue = players_queue[0]
                players_queue.pop(0)
                room = {'first_player': player_from_queue, 'second_player': self.connection}
                chess_engine = game_engine(room)
                chess_engine.start()

                work = multi_threaded_client(player_from_queue)
                work.start()

        except Exception as ex:
            """
            Если в очереди никого нет, то клиент становится  в очередь.
            Сервер отправляет клиенту сообщение 'wait'.            
            """
            players_queue.append(self.connection)
            send_message(self.connection, 'wait', '')
            print(ex)
            """
            НЕ КОСТЫЛЬ, А КОСТЫЛИЩЕЕЕ
            """
            self.exitTrigger = False

    def run(self):
        online_users.add(self.connection)
        while self.exitTrigger:
            print("Online users: {}".format(len(online_users)))
            print("Authorized users: {}".format(len(authorized_users)))
            try:
                data = self.connection.recv(2048)
                wrapper = json.loads(data.decode())
                print("{}: '{}' ".format(self.connection, wrapper['message']))

                if wrapper['message'] == "registration":
                    self.__registration(wrapper)
                elif wrapper['message'] == "authorization":
                    self.__authorization(wrapper)
                elif wrapper['message'] == "get_secret_question":
                    self.__get_secret_question(wrapper)
                elif wrapper['message'] == "change_password":
                    self.__change_password(wrapper)
                elif wrapper['message'] == "find_game":
                    if authorized_users.get(self.connection) is not None:
                        self.__find_game()
                    else:
                        send_message(self.connection, 'not_authorized', '')
                else:
                    send_message(self.connection, 'error', '')
            except Exception as ex:
                print(ex)
                online_users.discard(self.connection)
                authorized_users.pop(self.connection)
                break
