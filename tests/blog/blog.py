from post import Post


class Blog:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.posts: list[Post] = []

    def __repr__(self) -> str:
        return f"{self.title} by {self.author} ({len(self.posts)} posts)"
