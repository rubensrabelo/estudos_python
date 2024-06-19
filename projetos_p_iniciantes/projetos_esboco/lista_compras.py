# LISTA COMPRAS

lista_de_compras = []

opcoes = {
    "1": "Adicionar",
    "2": "Remover",
    "3": "Visualizar",
    "4": "Sair do Programa",
}


def adicionar(nome, preco):
    lista_de_compras.append({
        "nome": nome,
        "preco": preco,
    })


def remover(indice):
    del lista_de_compras[indice]


def visualizar():
    return "\n".join(
        f"[{i}] Nome: {produto['nome']} e Preco: {produto['preco']}" for i, produto in enumerate(lista_de_compras)
    )


while True:
    print("DIGITE UMA OPCAO:")
    for chave, valor in opcoes.items():
        print(f"[{chave}] {valor}")
    print()

    opcao = input("Digite uma opcao: ")

    if opcao in opcoes:
        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o valor do produto: "))
            adicionar(nome, preco)
        elif opcao == "2":
            indice = int(input("Digite o indice do produto: "))
            remover(indice)
        elif opcao == "3":
            print(visualizar())
        else:
            break
    else:
        print("Digite uma opcao valida!")
