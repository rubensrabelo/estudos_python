from dataclasses import dataclass


@dataclass
class PublishingCompany:
    """Classe que representa uma empresa editora."""
    name: str
    uf: str
    id: int = None

    __next_id: int = 1  # Variável privata para automatizar a contagem do id

    def __post_init__(self) -> None:
        """
        Método que inicializa o ID da empresa após a criação da instância.
        """
        self.id = PublishingCompany.__next_id
        PublishingCompany.__next_id += 1

    @staticmethod
    def reset_id_counter() -> None:
        """Método para resetar o contador de IDs."""
        PublishingCompany.__next_id = 1
