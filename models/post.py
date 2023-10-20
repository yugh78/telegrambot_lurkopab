from models.picture import Picture
class Post:
    id: int
    text: str
    topic: str
    hash: str
    pictures: list[Picture]

