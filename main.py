import asyncio
from database import DatabaseContext
from vk import VkClient, sort_collection
import re
import sys
import json


async def fill_db():
    db = DatabaseContext('db.db')
    await db.ensureCreated()
    vk_client = VkClient(sys.argv[2])
    post_count = vk_client.get_post_count()
    posts = []
    offset = 0

    while post_count > 0:
        posts = sort_collection(vk_client.get_data(offset))
        for post in posts:
            parsed_post = parse_post(post)
            await db.addPost(parsed_post)
        offset += 100

        post_count -= 100


hashtag_regex = re.compile('#[\S]*')


def parse_post(unparsed):
    post = Post()
    post.text = unparsed['text'].replace('"',"'")
    post.topic = ' '.join(re.findall(hashtag_regex, unparsed['text']))
    post.hash = unparsed['hash']
    post.pictures = []
    for unparsed_picture in where(unparsed['attachments'], lambda x: x['type'] == 'photo'):
        picture = Picture()
        picture.link = sorted(unparsed_picture['photo']['sizes'], key=lambda x: x['height'], reverse=True)[0]['url']
        post.pictures.append(picture)
    return post


def where(coll, func):
    new_c = []
    for x in coll:
        if func(x):
            new_c.append(x)
    return new_c


async def main_async():
    if sys.argv[1] == 'fill-database':
        await fill_db()

    elif sys.argv[1] == 'startbot':
        pass
    else:
        print('Wrong command')

    pass


if __name__ == '__main__':
    asyncio.run(main_async())
