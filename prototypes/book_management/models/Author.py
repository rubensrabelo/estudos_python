from dataclasses import dataclass


@dataclass
class Author:
    """Classe que representa um autor."""
    name: str
    gender: str
    id: int = None

    __next_id: int = 1  # Variável privata para automatizar a contagem do id

    def __post_init__(self) -> None:
        """Inicializa o ID do autor após a criação da instância."""
        self.id = Author.__next_id
        Author.__next_id += 1

    @staticmethod
    def reset_id_counter() -> None:
        """Reseta o contador de IDs."""
        Author.__next_id = 1
