from simulator.character.enums import Magic


class FrostBolt:
    CAST_TIME = 3000
    MAGIC_SCHOOL = Magic.Frost

    def __init__(self, timestamp: int, hit: bool, damage) -> None:
        super().__init__()
        self.timestamp = timestamp
        self.hit = hit
        self.damage = damage