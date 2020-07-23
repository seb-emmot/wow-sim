import random

import numpy as np

from simulator.character.buffs import BuffName
from simulator.character.character import Mage
from simulator.character.enums import Magic


class FrostBolt:
    BASE_CAST_TIME = 3000
    MAGIC_SCHOOL = Magic.Frost

    def __init__(self, source: Mage, target, cast_time_start: int) -> None:
        super().__init__()
        self._source = source
        self._target = target
        self._cast_time_start = cast_time_start

        self._base_low = 440
        self._base_high = 475
        self._sp_mod = 0.814

        self.timestamp = None
        self.hit = None
        self.damage = None

        self.evaluate_cast_time()
        self.evaluate_hit()

    def evaluate_hit(self):
        hit_chance = self._target.calculate_hit_chance(self._source)
        base = random.randint(self._base_low, self._base_high)
        dmg = (base + self._source.stats.spell_power * self._sp_mod) * self._source.stats.spell_damage_multiplier
        hit = np.random.choice([0, 1], p=[1 - hit_chance, hit_chance])

        crit_chance = self._source.stats.spell_crit
        try:
            wc_buff = self._target.get_buff(BuffName.WintersChill)
            stacks = wc_buff.stacks
            crit_chance += stacks * 0.02
        except KeyError:
            pass
        crit = np.random.choice([0, 1], p=[1 - crit_chance, crit_chance])
        crit_extra_dmg = crit * (dmg * self._source.stats.spell_crit_multiplier)

        self.hit = hit
        self.damage = dmg + crit_extra_dmg

    def evaluate_cast_time(self):
        cast_time = self.BASE_CAST_TIME - (self._source.talents.improved_frostbolt * 100)
        hit_timestamp = self._cast_time_start + cast_time
        self.timestamp = hit_timestamp
