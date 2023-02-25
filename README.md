# chess

Регистрация
    
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
                     
Авторизация
    
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
 
 Получение секретного вопроса
 
    Формат запроса:
    {"message": "get_secret_question",
     "information": {"username": <username>}

    Формат ответа (в случае успеха):
    {"message": "get_secret_question_success",
     "information": {"secret_question": <secret_question>}}

    Формат ответа (в случае ошибки):
    {"message": "get_secret_question_fail",
     "information": <Exception>}
     
 Смена пароля
 
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
 
 Поиск игры
 
    Формат запроса:
    {"message": "find_game",
     "information": ""}

    Формат ответа (в случае успеха):
    {"message": "wait",
     "information": ""}
    
    Или если игра началась:
    {"message": "start",
     "information": ""}
    
    Формат ответа (если не пользователь не авторизован):
    {"message": "not_authorized",
     "information": <Exception>}
