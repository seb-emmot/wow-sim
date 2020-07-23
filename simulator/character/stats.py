from __future__ import annotations

from simulator.character.talents import Talents


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

        self.spell_damage_multiplier = None
        self.spell_crit_multiplier = None

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

    # TODO: Break out weights (possibly inject weight numbers)
    def update_secondary_stats(self):
        self.armor = 2.0 * self.agility
        self.mana = 15.0 * self.intellect
        self.spell_crit = 0.01 * self.intellect / 59.5
        self.health = 10.0 * self.stamina
        self.mana_regen = 5.0 * self.spirit / 12.5

    # TODO: This is mage-specific and should not be here.
    def update_from_talents(self, talents: Talents):
        self.spell_hit = 0
        self.spell_crit_multiplier = 0.5
        self.spell_damage_multiplier = 1.0

        self.spell_hit += talents.elemental_precision * 0.02
        self.spell_damage_multiplier *= (1 + 0.02 * talents.piercing_ice)
        self.spell_crit_multiplier *= (1 + 0.2 * talents.ice_shards)


class PrimaryStats(BaseStats):

    def __init__(self, strength, agility, stamina, intellect, spirit) -> None:
        super().__init__()
        self.strength = strength
        self.agility = agility
        self.stamina = stamina
        self.intellect = intellect
        self.spirit = spirit


class AttributeMultipliers:
    def __init__(self, strength=1, agility=1, stamina=1, intellect=1, spirit=1) -> None:
        super().__init__()
        self.strength_multiplier = strength
        self.agility_multiplier = agility
        self.stamina_multiplier = stamina
        self.intellect_multiplier = intellect
        self.spirit_multiplier = spirit

    def __mul__(self, other: AttributeMultipliers) -> AttributeMultipliers:
        new_multipliers = AttributeMultipliers(
            strength=self.strength_multiplier * other.strength_multiplier,
            agility=self.agility_multiplier * other.agility_multiplier,
            stamina=self.stamina_multiplier * other.stamina_multiplier,
            intellect=self.intellect_multiplier * other.intellect_multiplier,
            spirit=self.spirit_multiplier * other.spirit_multiplier,
        )

        return new_multipliers
