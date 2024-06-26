from dataclasses import dataclass

from model.entities.enums import StatusTask


@dataclass
class Task:
    name: str
    status: StatusTask = StatusTask.PENDING
