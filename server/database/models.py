from sqlalchemy import Column, ForeignKey, Boolean, Time, Date, VARCHAR, BIGINT, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# Храним данные о зарегистрированных пользователях
class Users(Base):
    __tablename__ = "users"
    id = Column(BIGINT, primary_key=True)
    username = Column(VARCHAR(16))
    password = Column(VARCHAR(128))
    secret_question = Column(VARCHAR(128))
    answer = Column(VARCHAR(16))

    def __init__(self, data, session):
        self.id = data["id"]
        self.username = data["username"]
        self.password = data["password"]
        self.secret_question = data["secret_question"]
        self.answer = data["answer"]

    def to_json(self):
        result = {
            "id": self.id,
            "username": self.username,
            "secret_question": self.secret_question
        }
        return result


# Храним начатые сессии игр
class GameSessions(Base):
    __tablename__ = "game_sessions"
    id = Column(BIGINT, primary_key=True)
    first_player_id = Column(BIGINT, ForeignKey("users.id"))
    second_player_id = Column(BIGINT, ForeignKey("users.id"))
    start_date = Column(Date)
    start_time = Column(Time)
    status = Column(Boolean)

    def __init__(self, data, session):
        self.id = data["id"]
        self.first_player_id = data["first_player_id"]
        self.second_player_id = data["second_player_id"]
        self.start_date = data["start_date"]
        self.start_time = data["start_time"]
        self.status = data["status"]

    def to_json(self):
        result = {
            "id": self.id,
            "first_player_id": self.first_player_id,
            "second_player_id": self.second_player_id,
            "start_date": self.start_date,
            "start_time": self.start_time,
            "status": self.status,
        }
        return result


# Храним результаты законченных игр
class GameStorage(Base):
    __tablename__ = "game_storage"
    id = Column(BIGINT, primary_key=True)
    game_session_id = Column(BIGINT, ForeignKey("game_session.id"))
    end_date = Column(Date)
    end_time = Column(Time)
    result = Column(Text)
    history = Column(Text)

    def __init__(self, data, session):
        self.id = data["id"]
        self.game_session_id = data["game_session_id"]
        self.end_date = data["end_date"]
        self.end_time = data["end_time"]
        self.result = data["result"]
        self.history = data["history"]

    def to_json(self):
        result = {
            "id": self.id,
            "game_session_id": self.game_session_id,
            "end_date": self.end_date,
            "end_time": self.end_time,
            "result": self.result,
            "history": self.history,
        }
        return result
