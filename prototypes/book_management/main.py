from controller import BookController as bc
from models.Book import Book

options = {
    "1": "Adding Book",
    "2": "Update Book",
    "3": "Remove Book",
    "4": "Show All Books",
    "5": "See Menu",
    "6": "Quit Program",
}


class App:

    def menu(self, option: str, book_data: Book = None, index: int = None) -> None:
        # while True:
        #     for key, value in options.items():
        #         print(f"[{key}] {value}")

        #     option = input("Insert your command: ")

        if option in options:
            if option == "1":
                self.__add_book(book_data)
            elif option == "2":
                self.__update_book(index, book_data)
            elif option == "3":
                self.__remove_book(index)
            elif option == "4":
                print(self.__show_book())
            elif option == "5":
                self.menu()
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
    import csv

    app = App()

    # abrir o arquivo CSV
    # with open("inputs_livros.csv", "r") as file:
    #     lines = csv.reader(file)
    #     for i, line in enumerate(lines):
    #         if i != 0:
    #             book = Book(line[0], int(line[1]), float(line[2]), line[3])
    #             book.add_author(line[4])

    #             app.menu("1", book)

    # Inserir um dado para testar
    # Atualizar o dado
    # apagar o dado
    # mostrar todos os dados

    # Está incluindo mais arquivo após apagar
    app.menu(option="3", index=4)
