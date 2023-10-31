
import re
from models import *
from config import DATABASE as db
from vk import VkClient, sort_collection
from sys import argv

def fill_db():
    db.connect()
    db.create_tables([Post, Picture, User, UserAction])
    vk_client = VkClient(argv[1])
    post_count = vk_client.get_post_count()
    offset = 0

    while post_count > 0:
        posts = sort_collection(vk_client.get_data(offset))
        for post in posts:
            parse_post(post).save()
        offset += 100

        post_count -= 100
    db.close()

hashtag_regex = re.compile('#[\S]*')


def parse_post(unparsed):
    post = Post.create(
        text = unparsed['text'].replace('"', "'"),
        topic = ' '.join(re.findall(hashtag_regex, unparsed['text'])),
        hash = unparsed['hash']
    )
    for unparsed_picture in where(unparsed['attachments'], lambda x: x['type'] == 'photo'):
        # здесь выдает ошибку
        # 'NoneType' object does not support item assignment
        link = sorted(unparsed_picture['photo']['sizes'], key=lambda x: x['height'], reverse=True)[0]['url']
        if link is not None:
            picture = Picture.create(link=link,post=post)
            # picture.link = sorted(unparsed_picture['photo']['sizes'], key=lambda x: x['height'], reverse=True)[0]['url']
    return post



def where(coll, func):
    new_c = []
    for x in coll:
        if func(x):
            new_c.append(x)
    return new_c


if __name__ == '__main__':
    fill_db()
