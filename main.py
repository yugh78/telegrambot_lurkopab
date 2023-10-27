import asyncio
from database import DatabaseContext
from models.post import Post
from models.picture import Picture
from vk import VkClient,sort_collection

import sys
import json
def fill_db():
    vk_client = VkClient(sys.argv[2])
    post_count = vk_client.get_post_count()
    posts = []
    offset = 0
    while post_count > 0:
        posts = sort_collection(vk_client.get_data(offset))
        for post in posts:
            print(post['text'])
        offset += 100
        post_count -= 100


async def main_async():
    if sys.argv[1] == 'fill-database':
        fill_db()

    elif sys.argv[1] == 'startbot':
        pass
    else: print('Wrong command')


    #print(json.dumps(r, indent=4))
    #s = {'items':r}
    #print(json.dumps(r))
    #print(json.dumps(s,indent=2))

    # db = DatabaseContext("db.db")
    # await db.ensureCreated()
    #
    # post = Post()
    # post.text = "Cool post"
    # post.topic = "About coolnesses"
    # pic = Picture()
    # pic.link = 'google.com'
    # post.hash = "hash"
    # post.pictures = [pic, pic]
    #
    # await db.addPost(post)
    # post = await db.getPost(4)
    # for pic in post.pictures:
    #     print(pic.id)
    # print(post.pictures)
    # await db.getLastPostId()

    pass


if __name__ == '__main__':
    asyncio.run(main_async())
