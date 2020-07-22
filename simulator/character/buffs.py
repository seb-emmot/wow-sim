from enum import Enum


class BuffName(Enum):
    WintersChill = 0


class Buff:
    def __init__(self, start_time, end_time) -> None:
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time


class WintersChill(Buff):
    def __init__(self, start_time, end_time, stacks) -> None:
        super().__init__(start_time, end_time)
        self.stacks = stacks
