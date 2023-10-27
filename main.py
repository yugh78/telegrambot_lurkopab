import asyncio
from database import DatabaseContext
from models.post import Post
from models.picture import Picture
import vk
import sys
import json


async def main_async():
    r = vk.get_data2(sys.argv[1])
    print(json.dumps(r, indent=4))
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
