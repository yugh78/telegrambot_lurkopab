from dataclasses import dataclass
from peewee import *
from config import DATABASE as db


class Post(Model):
    # id = IntegerField()
    text = TextField()
    topic = TextField()
    hash = TextField()

    # pictures: []

    class Meta:
        database = db


class User(Model):
    user_id = CharField()
    full_name = CharField()

    class Meta:
        database = db


class Picture(Model):
    # id = IntegerField()
    link = CharField()
    post = ForeignKeyField(Post, backref='pictures')

    class Meta:
        database = db


class UserAction(Model):
    user = ForeignKeyField(User, backref='actions')
    chosen_topic = CharField()

    class Meta:
        database = db
