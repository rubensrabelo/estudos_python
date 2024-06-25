from dataclasses import dataclass

from entities.enums import StatusTask


@dataclass
class Task:
    name: str
    status: StatusTask
