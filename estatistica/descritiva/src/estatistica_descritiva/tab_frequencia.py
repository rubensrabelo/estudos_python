import itertools


class teste:
    def __init__(self, lista):
        self.lista = sorted(lista)
        self.dicionario = {}
        self.addDicionario()

    def addDicionario(self):
        gr = itertools.groupby(self.lista)
        for c, v in gr:
            self.dicionario[c] = len(list(v))

    def __str__(self):
        return "\n".join(f"{c}: {v}" for c, v in self.dicionario.items())


if __name__ == "__main__":
    lista = [1, 1, 2, 3, 4, 4]
    t = teste(lista)
    # t.addDicionario()
    print(t)

    # Não estou conseguindo obter resultado na organização dos dados
