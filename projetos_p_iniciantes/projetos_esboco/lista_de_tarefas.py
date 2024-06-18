# Lista de Tarefas

lista_de_tarefas = []


def inserir_tarefa(nome, situacao="Em andamento"):
    lista_de_tarefas.append({
        "nome": nome,
        "situacao": situacao
    })


def remover_tarefa(indice):
    del lista_de_tarefas[indice]


def marcar_conclusao(indice):
    lista_de_tarefas[indice]["situacao"] = "finalizado"


def visualizar_tarefas():
    return "\n".join(f"[{i+1}] - {tarefa['nome']} ({tarefa['situacao']})" for i, tarefa in enumerate(lista_de_tarefas))


opcoes_do_programa = {
    "1": "Inserir Tarefa",
    "2": "Remover Tarefa",
    "3": "Visualizar Tarefas",
    "4": "Marcar como Concluído",
    "5": "Sair do Programa",
}

while True:
    print("Escolha uma opção: ")
    for valor, chave in opcoes_do_programa.items():
        print(f"[{valor}]: {chave}")
    print()
    opcao = str(input("Digite sua opção: "))

    if opcao in opcoes_do_programa:
        if opcao == "1":
            nome = input("Digite um nome: ")
            inserir_tarefa(nome)
        elif opcao == "2":
            indice = int(input("Digite o indice da tarefa: "))
            remover_tarefa(indice - 1)
        elif opcao == "3":
            print("-" * 30)
            print(visualizar_tarefas())
            print("-" * 30)
        elif opcao == "4":
            indice = int(input("Digite o indice da tarefa: "))
            marcar_conclusao(indice - 1)
        else:
            break
    else:
        print("Digite uma opção válida!")
    print()
