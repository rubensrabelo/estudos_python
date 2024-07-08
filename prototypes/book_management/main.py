# "Alice no País das Maravilhas",200,29.99,"Wonderland Publishing","Lewis Carroll"
# "Dom Quixote",400,39.99,"Mancha Press","Miguel de Cervantes"

if __name__ == "__main__":
    from models import Book
    from controller import BookController as bc

    # abrir o arquivo CSV

    # Tranformar os dados em Book
    book = Book("Alice no País das Maravilhas", 200, 29.99, "Wonderland Publishing")
    book.add_author("Lewis Carroll")
    book2 = Book("Dom Quixote", 400, 39.99, "Mancha Press")
    book2.add_author("Miguel de Cervantes")

    # Adicionar os dados no bd
    bc.add(book)
    bc.add(book2)
