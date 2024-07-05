from dataclasses import dataclass


@dataclass
class Post:
    title: str
    content: str

    def json(self) -> dict[str, str]:
        return {
            "title": self.title,
            "content": self.content,
        }
