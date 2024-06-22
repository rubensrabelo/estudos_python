from dataclasses import dataclass, field
from typing import List

from entities.Task import Task


@dataclass
class ToDoList:
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append({
            "name": task.name,
            "status": task.status,
        })

    def remove_task(self, index: int) -> None:
        del self.tasks[index]

    def update_task(self, index: int, name: str | None = None, status: str | None = None) -> None:
        if name and status:
            self.tasks[index]["name"] = name
            self.tasks[index]["status"] = status
            return
        elif name and not status:
            self.tasks[index]["name"] = name
            return
        self.tasks[index]["status"] = status
        return


if __name__ == "__main__":
    from entities.Task import Task

    # Criando uma instância da lista de tarefas
    my_todo_list = ToDoList()

    # Adicionando tarefas à lista
    task1 = Task(name="Fazer compras", status="Pendente")
    task2 = Task(name="Estudar Python", status="Em andamento")
    my_todo_list.add_task(task1)
    my_todo_list.add_task(task2)

    # Verificando as tarefas na lista
    print(my_todo_list.tasks)  # Deve imprimir: [{'name': 'Fazer compras', 'status': 'Pendente'}, {'name': 'Estudar Python', 'status': 'Em andamento'}]

    # Removendo uma tarefa
    my_todo_list.remove_task(0)
    print(my_todo_list.tasks)  # Deve imprimir: [{'name': 'Estudar Python', 'status': 'Em andamento'}]

    # Atualizando uma tarefa
    my_todo_list.update_task(0, status="Concluído")
    print(my_todo_list.tasks)  # Deve imprimir: [{'name': 'Estudar Algoritmos', 'status': 'Concluído'}]
