from simulator.character.stats import BaseStats


class Talents:

    def __init__(self, talents_dict: dict) -> None:
        super().__init__()
        self.improved_frostbolt = 0
        self.elemental_precision = 0
        self.ice_shards = 0
        self.piercing_ice = 0
        self.frost_channeling = 0
        self.winters_chill = 0

        self.arcane_subtlety = 0
        self.arcane_focus = 0
        self.arcane_concentration = 0
        self.improved_arcane_explosion = 0
        self.arcane_meditation = 0
        self.presence_of_mind = 0
        self.arcane_mind = 0
        self.arcane_instability = 0
        self.arcane_power = 0

        self._validate_talent_dict(talents_dict)
        self._update_talents(talents_dict)

    def _validate_talent_dict(self, talent_dict: dict):
        for entry in talent_dict:
            try:
                getattr(self, entry)
            except Exception:
                raise

    def _update_talents(self, talent_dict: dict):
        for entry in talent_dict:
            setattr(self, entry, talent_dict[entry])

    def get_base_attribute_modifiers(self):
        pass

    def get_spell_modifiers(self) -> BaseStats:
        stats = BaseStats()
        stats.spell_hit = self.elemental_precision * 0.02
        stats.spell_damage_multiplier *= (1 + 0.02 * self.piercing_ice)
        stats.spell_crit_multiplier *= (1 + 0.2 * self.ice_shards)
        return stats


class Buff:
    def __init__(self, start_time, end_time) -> None:
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
