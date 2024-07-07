from typing import Union

from Controller.JsonManagementService import JsonManagementService
from models.Book import Book


class BookController:
    __json_service = JsonManagementService("books.json")

    @staticmethod
    def add(value: dict[str, Union[str, float]]) -> None:
        """Adiciona um livro ao arquivo JSON."""
        BookController.__json_service.add_file(value)

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
            raise IndexError("Índice fora dos limites.")

        BookController.__json_service.add_file(data)

    @staticmethod
    def show() -> str:
        """Retorna uma representação em string de todos os livros."""
        datas = BookController.__json_service.open_file()
        books = [Book(**data) for data in datas]
        return "\n".join(str(book) for book in books)
