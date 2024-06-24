from dataclasses import dataclass
from entities.enums.TaskStatus import TaskStatus


@dataclass
class Task:
    name: str
    status: TaskStatus


if __name__ == "__main__":
    from enums.TaskStatus import TaskStatus

    minha_tarefa = Task("Completar relatório", TaskStatus.IN_PROGRESS)
    print(f"{minha_tarefa}")
