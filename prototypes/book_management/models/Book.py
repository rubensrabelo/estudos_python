class Book:
    """Classe que representa um livro."""

    __id_counter: int = 0  # Variável de classe privada para rastrear IDs únicos

    def __init__(self, name: str, pages_quantity: int, price: float, publishing_company: str) -> None:
        """
        Inicializa uma instância de Book.

        Args:
            name (str): O nome do livro.
            pages_quantity (int): A quantidade de páginas do livro.
            price (float): O preço do livro.
            publishing_company (PublishingCompany): A empresa editora do livro.
        """
        self.name: str = name
        self.pages_quantity: int = pages_quantity
        self.price: float = price
        self.publishing_company: str = publishing_company
        self.authors: list[str] = []
        self.id = self.__increment_id()

    def __increment_id(self) -> int:
        """Incrementa o ID do livro e retorna o novo ID."""
        Book.__id_counter += 1
        return Book.__id_counter

    @staticmethod
    def reset_id_counter() -> None:
        """Reseta o contador de IDs."""
        Book.__id_counter = 0

    def add_author(self, author: str) -> None:
        """Adiciona um autor à lista de autores do livro.

        Args:
            author (Author): O autor a ser adicionado.
        """
        self.authors.append(author)

    def remove_author(self, author: str) -> None:
        """Remove um autor da lista de autores do livro.

        Args:
            author (Author): O autor a ser removido.
        """
        self.authors.remove(author)

    def __str__(self) -> str:
        """Retorna uma representação em string do livro."""
        first_part = f"{__class__.__name__}(Name={self.name}, Pages Quantity={self.pages_quantity}"
        second_part = f", Price={self.price}, Publishing Company={self.publishing_company}"
        third_part = ", Authors=[" + ", ".join(str(author) for author in self.authors) + "])"
        return first_part + second_part + third_part
