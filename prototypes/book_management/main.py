from models.Book import Book
from controller import BookController as bc


options = {
    "1": "Adding Book",
    "2": "Update Book",
    "3": "Remove Book",
    "4": "Show All Books",
    "5": "See Menu",
    "6": "Quit Program",
}


class App:

    def menu(self, book_data: Book = None, index: int = None) -> None:
        while True:
            for key, value in options.items():
                print(f"[{key}] {value}")

            option = input("Insert your command: ")

            if option in options:
                if option == "1":
                    self.__add_book(book_data)
                elif option == "2":
                    self.__update_book(index, book_data)
                elif option == "3":
                    self.__remove_book(index)
                elif option == "4":
                    self.__show_book()
                elif option == "5":
                    continue
                else:
                    print("See you later!")
            else:
                print("Invalid option. Try again.")

    def __add_book(self, book_data: Book) -> None:
        bc.add(book_data)

    def __update_book(self, index: int, data_book: Book) -> None:
        bc.update(index, data_book)

    def __remove_book(self, index: int) -> None:
        bc.remove(index)

    def __show_book(self) -> str:
        return bc.show()


if __name__ == "__main__":
    app = App()
    app.menu()

    # # abrir o arquivo CSV

    # # Tranformar os dados em Book

    # book = Book("Alice no País das Maravilhas", 200, 29.99, "Wonderland Publishing")
    # book.add_author("Lewis Carroll")
    # book2 = Book("Dom Quixote", 400, 39.99, "Mancha Press")
    # book2.add_author("Miguel de Cervantes")

    # # Adicionar os dados no bd
    # bc.add(book)
    # bc.add(book2)
