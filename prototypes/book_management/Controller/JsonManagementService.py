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
        with open(self.__PATH_FILE, "r", encoding="utf-8") as file_read:
            data = json.load(file_read)
        return data

    def add_file(self, value: dict[str, Union[str, float]]) -> None:
        data = self.open_file()
        data.append(value)

        with open(self.__PATH_FILE, "w") as file_write:
            json.dump(data, file_write, indent=4)

    def remove_value(self, index):
        data = self.open_file()
        del data[index]
        self.add_file(data)

    # Esse método é algo da classe, pois ela que conhece os seus atributos
    # def update_file(self, index: int, value: dict[str, Union[str, float]]) -> None:
    #     data = self.open_file()
    #     data[index] = value

    # Repensar se vale a pena construir essa classe
    # def show_file(self):
    #     with open(self.__PATH_FILE) as file:
    #         ...