# Lista de Tarefas

lista_de_tarefas = []


def inserir_tarefa():
    ...


def remover_tarefa():
    ...


def marcar_conclusao():
    ...


def visualizar_tarefas():
    ...


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
    opcao = str(input("Digite sua o5pção: "))

    if opcao in opcoes_do_programa:
        if opcao == "1":
            inserir_tarefa()
        elif opcao == "2":
            remover_tarefa()
        elif opcao == "3":
            visualizar_tarefas()
        elif opcao == "4":
            marcar_conclusao()
        else:
            break
    else:
        print("Digite uma opção válida!")
    print()
