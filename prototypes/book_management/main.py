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

    def menu(self):
        for key, value in options.items():
            print(f"[{key}] {value}")

        option = input("Insert your command: ")

        if option in options:
            if option == "1":
                self.__add_book()
            elif option == "2":
                self.__update_book()
            elif option == "3":
                self.__remove_book()
            elif option == "4":
                self.menu()
            elif option == "5":
                self.__show_book()
            else:
                print("Bye")
        else:
            print("not ok")

    def __add_book(self):
        title = input("Insert the title: ")
        pages_qtd = int(input("Insert the pages quantity: "))
        price = float(input("Insert the price: "))
        publishing_company = input("Insert the Publishing Company: ")

        book = Book(title, pages_qtd, price, publishing_company)
        book.add_author(input("Insert the author: "))
        bc.add(book)

    def __update_book(self):
        ...

    def __remove_book(self):
        ...

    def __show_book(self):
        ...


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
