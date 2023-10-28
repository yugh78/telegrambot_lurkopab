from models.picture import Picture
from dataclasses import dataclass, field

@dataclass
class Post:
    id: int = 0
    text: str = ""
    topic: str = ""
    hash: str = ""
    pictures: list[Picture] = field(default_factory=list[Picture])

