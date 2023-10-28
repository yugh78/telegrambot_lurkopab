import aiosqlite
from models.post import Post
from models.picture import Picture

# Таблицы в БД
TABLES = ["post", "picture"]

class DatabaseContext:

    def __init__(self, databaseName: str):
        """
        Parameters
        ---
        databaseName: str
            Название файла базы данных.
        """
        self.databaseName = databaseName

    async def ensureCreated(self):
        """
        Создаёт таблицы в базе данных.
        """
        async with aiosqlite.connect(self.databaseName) as db:
            for table in TABLES:
                with open(f"./database/{table}.sql", "r") as file:
                    command = ''.join(file.readlines())

                await db.execute(command)
                await db.commit()


    async def addPost(self, post: Post):
        async with aiosqlite.connect(self.databaseName) as db:
            with open(f"./database/create_{'post'}_command.sql", "r") as file:
                command = ''.join(file.readlines())
            command = command.replace("@text", f'"{post.text}"')
            command = command.replace("@topic", f'"{post.topic}"')
            command = command.replace("@hash", f'"{post.hash}"')

            await db.execute(command)
            await db.commit()

        newPostId = await self.getLastPostId()

        for pic in post.pictures:
            await self.addPicture(pic, newPostId)

    async def getLastPostId(self) -> int:
        async with aiosqlite.connect(self.databaseName) as db:
            with open(f"./database/get_last_post.sql", "r") as file:
                command = ''.join(file.readlines())

            async with db.execute(command) as cursor:
                async for row in cursor:
                    return row[0]

    async def addPicture(self, picture: Picture, postId: int):
        async with aiosqlite.connect(self.databaseName) as db:
            with open(f"./database/create_{'picture'}_command.sql", "r") as file:
                command = ''.join(file.readlines())

            command = command.replace("@link", f'"{picture.link}"')
            command = command.replace("@post_id", f'"{postId}"')

            await db.execute(command)
            await db.commit()

    async def getPost(self, postId: int) -> Post:
        async with aiosqlite.connect(self.databaseName) as db:
            with open(f"./database/get_post.sql", "r") as file:
                command = ''.join(file.readlines())
            command = command.replace("@id", str(postId))
            

            post = Post()

            async with db.execute(command) as cursor:
                async for row in cursor:
                    post.id = row[0]
                    post.text = row[1]
                    post.topic = row[2]
                    post.hash = row[3]
            
            post.pictures = await self.getPictures(postId)

            return post
                
    async def getPictures(self, postId: int) -> list[Picture]:
        async with aiosqlite.connect(self.databaseName) as db:
            with open(f"./database/get_pictures.sql", "r") as file:
                command = ''.join(file.readlines())
            command = command.replace("@postId", str(postId))

            pictures = []

            async with db.execute(command) as cursor:
                async for row in cursor:
                    pic = Picture()
                    pic.id = row[0]
                    pic.link = row[1]
                    pic.postId = row[2]
                    
                    pictures.append(pic)

            return pictures

