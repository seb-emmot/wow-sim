from enum import Enum


class BuffName(Enum):
    WintersChill = 0


class Buff:
    def __init__(self, name : BuffName, stacks, start_time, end_time) -> None:
        super().__init__()
        self.name = name
        self.stacks = stacks
        self.start_time = start_time
        self.end_time = end_time


class WintersChill(Buff):
    def __init__(self, start_time, end_time, stacks) -> None:
        super().__init__(BuffName.WintersChill, stacks, start_time, end_time)

