from dataclasses import dataclass, field
from typing import List

from entities.Task import Task
from entities.enums.TaskStatus import TaskStatus


@dataclass
class ToDoList:
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        if not task:
            raise ValueError(
                "Error: Task can't be None."
                )
        self.tasks.append({
            "name": task.name,
            "status": task.status,
        })

    def remove_task(self, index: int) -> None:
        try:
            del self.tasks[index]
        except IndexError as e:
            print(f"Error: {e}")

    # Falta testar se o código abaixo está coerente - teste

    def update_task(self, index: int, name: str | None = None, status: int  | None = None) -> None:
        if status:
            if status not in list(range(1, 4)):
                raise ValueError("Error: Status should be in range 1 to 3")
            if status == 1:
                task_status: TaskStatus = TaskStatus.PENDING
            elif status == 2:
                task_status = TaskStatus.IN_PROGRESS
            else:
                task_status = TaskStatus.COMPLETED

        if name and status:
            self.tasks[index]["name"] = name
            self.tasks[index]["status"] = task_status
            return
        elif name and not status:
            self.tasks[index]["name"] = name
            return
        self.tasks[index]["status"] = task_status
        return
