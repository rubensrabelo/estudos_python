from enum import Enum, auto


class StatusTask(Enum):
    PENDING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    CANCELED = auto()
