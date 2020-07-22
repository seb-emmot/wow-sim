import random

import numpy as np

from simulator.character.buffs import BuffName
from simulator.character.character import Mage
from simulator.character.enums import Magic


class FrostBolt:
    CAST_TIME = 3000
    MAGIC_SCHOOL = Magic.Frost

    def __init__(self, source: Mage, target, timestamp: int) -> None:
        super().__init__()

        base_low = 440
        base_high = 475
        sp_mod = 0.814

        hit_chance = target.calculate_hit_chance(source)
        base = random.randint(base_low, base_high)
        dmg = (base + source.stats.spell_power * sp_mod) * source.stats.spell_damage_multiplier
        hit = np.random.choice([0, 1], p=[1 - hit_chance, hit_chance])

        crit_chance = source.stats.spell_crit
        try:
            wc_buff = target.get_buff(BuffName.WintersChill)
            stacks = wc_buff.stacks
            crit_chance += stacks * 0.02
        except KeyError:
            pass
        crit = np.random.choice([0, 1], p=[1 - crit_chance, crit_chance])
        crit_extra_dmg = crit * (dmg * source.stats.spell_crit_multiplier)

        cast_time = self.CAST_TIME - (source.talents.improved_frostbolt * 100)
        hit_timestamp = timestamp + cast_time

        self.timestamp = hit_timestamp
        self.hit = hit
        self.damage = dmg + crit_extra_dmg
