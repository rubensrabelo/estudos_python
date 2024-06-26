from dataclasses import dataclass, field
from typing import List

from model.entities.Task import Task
from model.entities.enums import StatusTask


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
        except IndexError:
            print("Error: No task exists with this index in the To-Do List.")

    def update_task(self, index: int, name: str | None = None, status: StatusTask | None = None) -> None:
        if name and status:
            self.tasks[index]["name"] = name
            self.tasks[index]["status"] = status
            return
        elif name and not status:
            self.tasks[index]["name"] = name
            self.tasks[index]["name"] = StatusTask.PENDING
            return
        self.tasks[index]["status"] = StatusTask
        return
