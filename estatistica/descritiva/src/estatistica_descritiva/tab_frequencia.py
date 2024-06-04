import itertools


class teste:
    def __init__(self, lista):
        self.lista = sorted(lista)
        self.dicionario = {}

    def addDicionario(self):
        gr = itertools.groupby(self.lista)
        for c, v in gr:
            self.dicionario[c] = len(list(v))

    def __str__(self):
        return "\n".join(f"{c}: {v}" for c, v in self.dicionario)


if __name__ == "__main__":
    lista = [1, 1, 2, 3, 4, 4]
    dicionario = {}
    t = teste(lista)
    print(t)
    gr = itertools.groupby(lista)
    
    for c, v in gr:
        dicionario[c] = len(list(v))
    
    print(dicionario)
