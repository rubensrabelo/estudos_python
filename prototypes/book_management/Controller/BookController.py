from typing import Union

from controller.JsonManagementService import JsonManagementService
from models.Book import Book


class BookController:
    __json_service = JsonManagementService("books.json")

    @staticmethod
    def add(value: Book) -> None:
        """Adiciona um livro ao arquivo JSON."""
        value_dict: dict[str, Union[str, float]] = value.__dict__
        BookController.__json_service.add_file(value_dict)

    @staticmethod
    def remove(index: int) -> None:
        """Remove um livro do arquivo JSON pelo índice."""
        BookController.__json_service.remove_value(index)

    @staticmethod
    def update(index: int, data_book: Book) -> None:
        """Atualiza os dados de um livro no arquivo JSON pelo índice."""
        data = BookController.__json_service.open_file()

        try:
            data[index]["name"] = data_book.name
            data[index]["pages_quantity"] = data_book.pages_quantity
            data[index]["price"] = data_book.price
            data[index]["publishing_company"] = data_book.publishing_company
            data[index]["authors"] = list(data_book.authors)
        except IndexError:
            raise IndexError("Index out of bounds.")

        BookController.__json_service.add_file(data)

    @staticmethod
    def show() -> str:
        """Retorna uma representação em string de todos os livros."""
        datas = BookController.__json_service.open_file()
        books = [
            Book(data["name"], data["pages_quantity"], data["price"], data["publishing_company"], data["authors"])
            for data in datas
            ]
        return "\n".join(str(book) for book in books)
