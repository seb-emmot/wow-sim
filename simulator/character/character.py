from simulator.character.buffs import Buff, BuffName
from simulator.character.stats import PrimaryStats
from simulator.gear import GearSet


class Target:

    def __init__(self, level, buffs: dict = None) -> None:
        super().__init__()
        if buffs is None:
            buffs = {}

        self.level = level
        self.buffs = buffs

    def get_buff(self, buffname: BuffName):
        return self.buffs[buffname]

    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, level):
        if level < 1 or level > 63:
            raise Exception("Level out of bounds")
        self._level = level

    def calculate_hit_chance(self, attacker):
        level_diff = abs(attacker.level - self.level)
        attacker_hit = attacker.stats.spell_hit if attacker.stats.spell_hit is not None else 0

        if level_diff == 0:
            hit_chance = 0.96 + attacker_hit
        elif level_diff == 1:
            hit_chance = 0.95 + attacker_hit
        elif level_diff == 2:
            hit_chance = 0.94 + attacker_hit
        elif level_diff == 3:
            hit_chance = 0.83 + attacker_hit
        else:
            raise Exception("Cannot handle level diffs of more than 3")

        # hit chance can never be above 99%
        return hit_chance if hit_chance < 1.0 else 0.99


class Mage:

    def __init__(self, race, talents, gear: GearSet, level) -> None:
        super().__init__()

        self.race = race
        self.level = level
        self.talents = talents

        # Race Human
        self.stats = PrimaryStats(30, 35, 45, 125, 120) + gear.calculate_gear_stats()

        self.stats.update_from_talents(talents)
        self.stats.update_secondary_stats()
