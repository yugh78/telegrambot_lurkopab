from dataclasses import dataclass
from peewee import *
from config import DATABASE as db

@dataclass
class Post(Model):
    id = IntegerField()
    text = TextField()
    topic = TextField()
    hash = TextField()
    pictures: []

    class Meta:
        database = db

@dataclass
class User(Model):
    id = IntegerField()
    chat_id = IntegerField()
    actions = []

    class Meta:
        database = db


@dataclass
class Picture(Model):
    id = IntegerField()
    link = TextField()
    postId = ForeignKeyField(Post, backref='pictures')

    class Meta:
        database = db


@dataclass
class UserAction(Model):
    id = IntegerField()
    user_id = ForeignKeyField(User, backref='action')
    choosen_topic = TextField()

    class Meta:
        database = db


