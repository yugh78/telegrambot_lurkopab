from models.picture import Picture
class Post:
    id: int
    text: str
    topic: str
    hash: str
    pictures: list[Picture]
    def __str__(self):
        return (f'{self.text}, {self.topic}, {self.hash}')

