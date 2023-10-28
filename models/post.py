from models.picture import Picture

@dataclass
class Post:
    id: int = 0
    text: str
    topic: str
    hash: str
    pictures: list[Picture] = []

