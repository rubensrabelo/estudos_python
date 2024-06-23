import shutil
import os
from pathlib import Path


class FolderHandling:
    @staticmethod
    def saving_in_folder(file):
        folder = Path("database", "db")
        if not folder.exists():
            folder.mkdir()

        caminho_atual = os.path.join("to_do_list", file)
        caminho_destino = os.path.join("database", "db")

        if os.path.exists(caminho_destino):
            shutil.move(caminho_atual, caminho_destino)
