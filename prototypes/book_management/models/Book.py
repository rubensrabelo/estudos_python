from models.Author import Author
from models.PublishingCompany import PublishingCompany


class Book:
    def __init__(self, name: str, pages_quantity: int, price: float, publishingCompany: PublishingCompany) -> None:
        self.name = name
        self.pages_quantity = pages_quantity
        self.price = price
        self.publishingCompany = publishingCompany
        self.authors: list[Author] = []

    def add_author(self, author: Author):
        self.authors.append(author)

    def remove_author(self, author: Author):
        self.authors.remove(author)

    def __str__(self) -> str:
        first_part = f"{__class__.__name__}(Name={self.name}, Pages Quantity={self.pages_quantity}"
        second_part = f", Price={self.price}, Publishing Company={self.publishingCompany.name}"
        third_part = ", Authors=[" + ", ".join(str(author.name) for author in self.authors) + "])"
        return first_part + second_part + third_part
