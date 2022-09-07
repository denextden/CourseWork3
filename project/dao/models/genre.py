from project.dao.models.base import BaseModel
from project.setup_db import db


class Genre(BaseModel, db.Model):
    __tablename__ = "genres"

    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<Genre '{self.name.title()}'>"


# from marshmallow import Schema, fields
#
# from project.setup_db import db
#
#
# class Genre(db.Model):
#     __tablename__ = 'genre'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#
#
# class GenreSchema(Schema):
#     id = fields.Int()
#     name = fields.Str()


