import os
import json
from typing import Union


class JsonManagementService:
    __PATH_DIR = r"C:\Users\ruben\OneDrive\01. estudo\01_linguagem_programacao\02_python\estudos_python\prototypes\book_management\database"

    def __init__(self, file: str) -> None:
        self.__file: str = file
        self.__PATH_FILE: str = os.path.join(
            JsonManagementService.__PATH_DIR, file
            )

    def open_file(self) -> list[dict[str, Union[str, float]]]:
        """Abre o arquivo JSON e retorna os dados como uma lista de dicionários."""
        try:
            with open(self.__PATH_FILE, "r", encoding="utf-8") as file_read:
                data = json.load(file_read)
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            data = []
        return data

    def add_file(self, value: dict[str, Union[str, float]]) -> None:
        """Adiciona um valor ao arquivo JSON."""
        data = self.open_file()
        data.append(value)

        with open(self.__PATH_FILE, "w", encoding="utf-8") as file_write:
            json.dump(data, file_write, indent=4)

    def remove_value(self, index: int) -> None:
        """Remove um valor do arquivo JSON baseado no índice."""
        data = self.open_file()

        if not data:
            raise ValueError("There is no data to remove.")

        try:
            del data[index]
        except IndexError:
            raise IndexError("Index out of bounds.")

        self.add_file(data)
