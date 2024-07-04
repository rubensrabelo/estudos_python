from Controller.JsonManagementService import JsonManagementService
from models.Author import Author


class AuthorController:
    __JSON_AUTHOR = "authors.json"
    __JSON_SERVICE = JsonManagementService(__JSON_AUTHOR)

    @staticmethod
    def add(author: Author) -> None:
        value = author.__dict__
        AuthorController.__JSON_SERVICE.add_file(value)

    @staticmethod
    def remove(index) -> None:
        AuthorController.__JSON_SERVICE.remove_value(index)

    @staticmethod
    def update(index: int, name: str = None, gender: str = None) -> None:
        data = AuthorController.__JSON_SERVICE.open_file()

        if name:
            data[index]["name"] = name

        if gender:
            data[index]["gender"] = gender

        AuthorController.__JSON_SERVICE.add_file(data)

    @staticmethod
    def show():
        ...
