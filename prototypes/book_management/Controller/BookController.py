from typing import Union

from Controller.JsonManagementService import JsonManagementService
from models.Book import Book


class BookController:
    __json_service = JsonManagementService("books.json")

    @staticmethod
    def add(value) -> None:
        BookController.__json_service.add_file(value)

    @staticmethod
    def remove(index) -> None:
        BookController.__json_service.remove_value(index)

    @staticmethod
    def update(index, data_book: Book) -> None:
        data = BookController.__json_service.open_file()

        data[index]["name"] = data_book.name
        data[index]["pages_quantity"] = data_book.pages_quantity
        data[index]["price"] = data_book.price
        data[index]["publishing_company"] = data_book.publishing_company
        data[index]["authors"] = list(data_book.authors)

    @staticmethod 
    def show():
        datas = BookController.__json_service.open_file()
        return "\n".join(Book(data) for data in datas)
