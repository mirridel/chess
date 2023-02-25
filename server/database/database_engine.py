from sqlalchemy.orm import sessionmaker
import sqlalchemy as db

from database.models import Users, GameSessions, GameStorage

engine = db.create_engine('postgresql+psycopg2://postgres:19092001@localhost/Chess')
conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

models = {
    "users": Users,
    "game_sessions": GameSessions,
    "game_storage": GameStorage
}


def insert(class_, data):
    obj = class_(data, session)
    if obj.id == -1:
        obj.id = None
    if obj.id is None:
        session.add(obj)
        session.commit()
        return obj.to_json()
    return None


def update(class_, data):
    obj = class_(data, session)
    session.merge(obj)
    session.commit()
    return str(obj.id)


def auth(data):
    result = session.query(Users).filter(Users.username == data["username"] and Users.password == data["password"]).one()
    return {"id": result.id}


def get_secret_question(data):
    result = session.query(Users).filter(Users.username == data["username"]).one()
    return {"secret_question": result.secret_question}


def change_password(data):
    result = session.query(Users).filter(Users.username == data["username"] and Users.answer == data["answer"]).one()
    result.password = data["password"]
    session.merge(result)
    session.commit()
    return {"new_password": result.password}
