import shutil
import os
from pathlib import Path


class FolderHandling:
    @staticmethod
    def saving_in_folder(file):
        folder = Path("database", "db")
        if not folder.exists():
            folder.mkdir()

        caminho_atual = os.path.join(".", file)
        caminho_destino = os.path.join("database", "db")

        # Tenho que ajeitaar a lógica para inserir novos valore após a criação do caminho destinho

        if os.path.exists(caminho_destino):
            shutil.move(caminho_atual, caminho_destino)
        else:
             ...
