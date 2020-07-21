from __future__ import annotations


class BaseStats:

    def __init__(self) -> None:
        pass
        self.strength = 0
        self.agility = 0
        self.stamina = 0
        self.intellect = 0
        self.spirit = 0

        self.health = None
        self.mana = None
        self.armor = None

        self.spell_hit = None
        self.spell_crit = None
        self.spell_power = None
        self.mana_regen = None

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

    def update_secondary_stats(self):
        self.armor = 2.0 * self.agility
        self.mana = 15.0 * self.intellect
        self.spell_crit = 0.01 * self.intellect / 59.5
        self.health = 10.0 * self.stamina
        self.mana_regen = 5.0 * self.spirit / 12.5


class PrimaryStats(BaseStats):

    def __init__(self, strength, agility, stamina, intellect, spirit) -> None:
        super().__init__()
        self.strength = strength
        self.agility = agility
        self.stamina = stamina
        self.intellect = intellect
        self.spirit = spirit
