import asyncio

from peewee import fn

import config
from aiogram import Bot, Dispatcher, types
from sys import argv
import random
from aiogram.filters import CommandStart, Command

from models import User, UserAction, Post

bot = Bot(argv[1])
dp = Dispatcher()

db = config.DATABASE
greetings = '''
Здарова
Мои возможности:
getpost - текст на заданную тему
'''


@dp.message(CommandStart())
async def start_handler(msg: types.Message):
    db.connect()
    query = User.select().where(User.user_id == msg.from_user.id)
    if not any(query):
        user = User.create(user_id=msg.from_user.id, full_name=msg.from_user.full_name)
    db.close()
    await msg.answer(text=greetings)


@dp.message(Command('getpost'))
async def get_post(msg: types.Message):
    topic = msg.text.replace('/getpost', '')
    if len(topic) > 0:
        db.connect()
        UserAction.create(user=User.get(User.user_id == msg.from_user.id), chosen_topic=topic)
        count = Post.select(fn.COUNT(Post.hash)).where(Post.topic.contains(topic)).scalar()
        post_id = random.randint(0, count)
        post_query = Post.select().where(Post.id == post_id)
        post = Post()

        if count == 0:
            await msg.answer(text='Отсутствует текст на эту тему')
            db.close()
        else:
            for row in post_query:
                post = row
            db.close()
            post_text = str(post.text)
            post_text_ar = [post_text[i:i + 4096] for i in range(0, len(post_text), 4096)]
            for x in post_text_ar:
                await msg.answer(text=x)


async def main() -> None:
    db.connect()
    db.create_tables([User, UserAction])
    db.close()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
