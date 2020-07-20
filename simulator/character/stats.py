from __future__ import annotations

from abc import *

from simulator.gear import GearSet


class BaseStats(ABC):

    def __init__(self) -> None:
        pass
        # self.strength = None
        # self.agility = None
        # self.stamina = None
        # self.intellect = None
        # self.spirit = None
        #
        # self.health = None
        # self.mana = None
        # self.armor = None
        #
        # self.spell_hit = None
        # self.spell_crit = None
        # self.spell_power = None
        # self.mana_regen = None

    def __add__(self, other: BaseStats) -> BaseStats:
        other_vars = vars(other)

        for entry in other_vars:
            try:
                primary_value = getattr(self, entry)
            except AttributeError:
                primary_value = None
            secondary_value = other_vars[entry]
            if primary_value is None:
                updated_value = secondary_value
            elif secondary_value is None:
                updated_value = primary_value
            else:
                updated_value = primary_value + secondary_value

            setattr(self, entry, updated_value)

        return self


class PrimaryStats(BaseStats):

    def __init__(self, strength, agility, stamina, intellect, spirit) -> None:
        super().__init__()
        self.strength = strength
        self.agility = agility
        self.stamina = stamina
        self.intellect = intellect
        self.spirit = spirit


class DerivedStats(BaseStats):

    def __init__(self, primary_stats: PrimaryStats) -> None:
        super().__init__()
        self.armor = 2.0 * primary_stats.agility
        self.mana = 15.0 * primary_stats.intellect
        self.spell_crit = 0.01 * primary_stats.intellect / 59.5
        self.health = 10.0 * primary_stats.stamina
        self.mana_regen = 5.0 * primary_stats.spirit / 12.5


class GearbasedStats(BaseStats):

    def __init__(self, gear: GearSet) -> None:
        super().__init__()
        self.spell_power = gear.calculate_spell_power()
        self.spell_crit = gear.calculate_spell_crit()
        self.spell_hit = gear.calculate_spell_hit()
        self.strength,\
            self.agility,\
            self.stamina,\
            self.intellect,\
            self.spirit\
            = gear.calculate_base_attributes()


