# LISTA COMPRAS

lista_de_compras = []

opcoes = {
    "1": "Adicionar",
    "2": "Remover",
    "3": "Visualizar",
    "4": "Sair do Programa",
}


def adicionar():
    ...


def remover():
    ...


def visualizar():
    ...


while True:
    print("DIGITE UMA OPCAO:")
    for chave, valor in opcoes.items():
        print(f"[{chave}] {valor}")
    print()

    opcao = input("Digite uma opcao: ")

    if opcao in opcoes:
        if opcao == 1:
            adicionar()
        if opcao == 1:
            remover()
        if opcao == 1:
            visualizar()
        else:
            break
    else:
        print("Digite uma opcao valida!")
    ...
