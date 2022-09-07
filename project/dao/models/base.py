from project.setup_db import db


class BaseModel(object):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
