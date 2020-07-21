from simulator.character.stats import BaseStats, PrimaryStats


class Gear:

    def __init__(self, stats_dict) -> None:
        super().__init__()
        self.name = stats_dict.get("name", 0)
        self.strength = stats_dict.get("str", 0)
        self.agility = stats_dict.get("agi", 0)
        self.stamina = stats_dict.get("sta", 0)
        self.intellect = stats_dict.get("int", 0)
        self.spirit = stats_dict.get("spi", 0)

        self.spell_crit = stats_dict.get("spell_crit", 0)
        self.spell_hit = stats_dict.get("spell_hit", 0)
        self.spell_power = stats_dict.get("spell_power", 0)


class GearSet:

    def __init__(self, gear_dict: dict) -> None:
        super().__init__()
        self.head = Gear(gear_dict.get("head", {}))
        self.neck = Gear(gear_dict.get("neck", {}))
        self.shoulder = Gear(gear_dict.get("shoulder", {}))
        self.back = Gear(gear_dict.get("back", {}))
        self.chest = Gear(gear_dict.get("chest", {}))
        self.wrist = Gear(gear_dict.get("wrist", {}))
        self.hands = Gear(gear_dict.get("hands", {}))
        self.waist = Gear(gear_dict.get("waist", {}))
        self.legs = Gear(gear_dict.get("legs", {}))
        self.boots = Gear(gear_dict.get("boots", {}))
        self.ring_1 = Gear(gear_dict.get("ring_1", {}))
        self.ring_2 = Gear(gear_dict.get("ring_2", {}))
        self.trinket_1 = Gear(gear_dict.get("trinket_1", {}))
        self.trinket_2 = Gear(gear_dict.get("trinket_2", {}))
        self.main_hand = Gear(gear_dict.get("main_hand", {}))
        self.off_hand = Gear(gear_dict.get("off_hand", {}))
        self.ranged = Gear(gear_dict.get("ranged", {}))

    def calculate_gear_stats(self) -> BaseStats:
        stats = BaseStats()
        stats += self._calculate_base_attributes()
        stats += self._calculate_spell_stats()

        return stats

    def _calculate_base_attributes(self) -> BaseStats:
        gearlist = vars(self)

        strength = 0
        agility = 0
        stamina = 0
        intellect = 0
        spirit = 0

        for gear in gearlist:
            try:
                strength += gearlist[gear].strength if gearlist[gear].strength is not None else 0
                agility += gearlist[gear].agility if gearlist[gear].agility is not None else 0
                stamina += gearlist[gear].stamina if gearlist[gear].stamina is not None else 0
                intellect += gearlist[gear].intellect if gearlist[gear].intellect is not None else 0
                spirit += gearlist[gear].spirit if gearlist[gear].spirit is not None else 0
            except TypeError:
                raise

        return PrimaryStats(strength, agility, stamina, intellect, spirit)

    def _calculate_spell_stats(self) -> BaseStats:
        gearlist = vars(self)
        sp = 0
        sc = 0
        sh = 0
        for gear in gearlist:
            try:
                sp += gearlist[gear].spell_power
                sc += gearlist[gear].spell_crit
                sh += gearlist[gear].spell_hit
            except TypeError:
                raise

        stat = BaseStats()
        stat.spell_hit = sh
        stat.spell_crit = sc
        stat.spell_power = sp

        return stat
