from simulator.character.character import Mage, Target
from simulator.spells import FrostBolt


class SpellFactory:

    def __init__(self) -> None:
        super().__init__()

    def spell_generator(self, source: Mage, target: Target, casts) -> iter:
        prev_timestamp = 0
        for i in range(0, casts):
            fb = self.generate_spell(source, target, prev_timestamp)
            prev_timestamp = fb.timestamp
            yield fb

    def generate_spell(self, source: Mage, target: Target, timestamp: int) -> FrostBolt:
        frostbolt = FrostBolt(source, target, timestamp)
        return frostbolt

