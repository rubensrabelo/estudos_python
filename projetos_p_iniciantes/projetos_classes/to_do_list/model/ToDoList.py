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
