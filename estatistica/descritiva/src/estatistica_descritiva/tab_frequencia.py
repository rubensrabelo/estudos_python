import itertools
from dataclasses import dataclass, field
from typing import List

# import pandas as pd
# from random import randint


@dataclass
class TabelaFrequencia:
        numeros: List[int] = field(default_factory=List)


if __name__ == "__main__":
    lista_num = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 8, 8, 9, 9]

    tab = TabelaFrequencia(lista_num)

    # Levar o código abaixo para a classe:
    # values = itertools.groupby(lista_num)
    # d = {}
    # for key, value in values:
    #       d[key] = len(list(value))
    # print(d)
