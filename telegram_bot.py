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
    text = msg.text.replace('/getpost', '')
    if len(text) > 0:
        db.connect()
        count = Post.select(fn.COUNT(Post.hash)).where(Post.topic.contains(text)).scalar()
        # print(len(count_query))
        post_id = random.randint(0, count)
        post_query = Post.select().where(Post.id == post_id)
        post = Post()
        for row in post_query:
            post = row
        db.close()
        for i in range(0, len(str(post.text)),4096):
            s = str(post.text)[i: i + 4096]
            await msg.answer(text=s )
    else:
        await msg.answer(text='съебался')


async def main() -> None:
    db.connect()
    db.create_tables([User, UserAction])
    db.close()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
