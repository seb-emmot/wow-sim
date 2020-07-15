import random
import numpy

from stats import PrimaryStats, DerivedStats, GearbasedStats


class Character:

    def __init__(self, race, level) -> None:
        self.race = race
        self.level = level
        super().__init__()


class Target:

    def __init__(self, level) -> None:
        super().__init__()
        self.level = level

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

        return hit_chance if hit_chance < 1.0 else 0.99


class FrostBolt:
    CAST_TIME = 2500

    def __init__(self, timestamp: int, hit: bool, damage) -> None:
        super().__init__()
        self.timestamp = timestamp
        self.hit = hit
        self.damage = damage


class Mage(Character):

    def __init__(self, race, gear, level) -> None:
        super().__init__(race, level)

        # Race Human
        primary_stats = PrimaryStats(30, 35, 45, 125, 120)
        derived_stats = DerivedStats(primary_stats)
        gear_stats = GearbasedStats(gear)

        self.stats = primary_stats + derived_stats
        self.stats += gear_stats

    def frostbolt_generator(self, target, casts) -> iter:
        prev_timestamp = 0
        for i in range(0, casts):
            fb = self.generate_frostbolt(target, prev_timestamp)
            prev_timestamp = fb.timestamp
            yield fb

    def generate_frostbolt(self, target, start_timestamp) -> FrostBolt:
        base_low = 440
        base_high = 475
        sp_mod = 0.814

        hit_chance = target.calculate_hit_chance(self)
        base = random.randint(base_low, base_high)
        dmg = base + self.stats.spell_power * sp_mod
        hit = numpy.random.choice([0, 1], p=[1 - hit_chance, hit_chance])
        crit = numpy.random.choice([1, 2], p=[1 - self.stats.spell_crit, self.stats.spell_crit])

        hit_timestamp = start_timestamp + FrostBolt.CAST_TIME

        frostbolt = FrostBolt(hit_timestamp, hit, dmg * crit)

        return frostbolt
