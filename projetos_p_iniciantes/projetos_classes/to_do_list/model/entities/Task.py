from dataclasses import dataclass


@dataclass
class Task:
    name: str
    status: int
