import requests
import json
import asyncio
from database import DatabaseContext
from models.post import Post
from models.picture import Picture
# Замените 'APP_ID' на ваш собственный APP_ID
# APP_ID = ' '
# url = 'https://api.vk.com/method/wall.get'
# r = requests.post(url,
#                   params={'v':5.154,'domain':'lurkopub_alive','count':10,'filter':'all'},
#                   headers= {'Authorization':f"Bearer {APP_ID}"})
# res = json.loads(r.text)
# print(res)
# fl = filter(lambda item: item['inner_type'] == 'wall_wallpost', res['response']['items'])
# print(*fl)



async def main():
    db = DatabaseContext("db.db")
    await db.ensureCreated()

    """ post = Post()
    post.text = "Cool post"
    post.topic = "About coolnesses"
    post.hash = "hash"
    post.pictures= [Picture("google.com"), Picture("ya.ru")]

    await db.addPost(post) """
    post = await db.getPost(4)
    for pic in post.pictures:
        print(pic.id)
    print(post.pictures)
    # await db.getLastPostId() 


if __name__ == "__main__":
    asyncio.run(main())










