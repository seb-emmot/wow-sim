class Gear:

    def __init__(self, stats_dict) -> None:
        super().__init__()
        self.name = stats_dict.get("name")
        self.strength = stats_dict.get("str")
        self.agility = stats_dict.get("agi")
        self.stamina = stats_dict.get("sta")
        self.intellect = stats_dict.get("int")
        self.spirit = stats_dict.get("spi")

        self.spell_crit = stats_dict.get("spell_crit")
        self.spell_hit = stats_dict.get("spell_hit")
        self.spell_power = stats_dict.get("spell_power")


class GearSet:

    def __init__(self, gear_dict) -> None:
        super().__init__()
        self.head = Gear(gear_dict.get("head"))
        self.neck = Gear(gear_dict.get("neck"))
        self.shoulder = Gear(gear_dict.get("shoulder"))
        self.back = Gear(gear_dict.get("back"))
        self.chest = Gear(gear_dict.get("chest"))
        self.wrist = Gear(gear_dict.get("wrist"))
        self.hands = Gear(gear_dict.get("hands"))
        self.waist = Gear(gear_dict.get("waist"))
        self.legs = Gear(gear_dict.get("legs"))
        self.boots = Gear(gear_dict.get("boots"))
        self.ring_1 = Gear(gear_dict.get("ring_1"))
        self.ring_2 = Gear(gear_dict.get("ring_2"))
        self.trinket_1 = Gear(gear_dict.get("trinket_1"))
        self.trinket_2 = Gear(gear_dict.get("trinket_2"))
        self.main_hand = Gear(gear_dict.get("main_hand"))
        self.off_hand = Gear(gear_dict.get("off_hand"))
        self.ranged = Gear(gear_dict.get("ranged"))

    def calculate_base_attributes(self):
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

        return strength, agility, stamina, intellect, spirit

    def calculate_spell_power(self) -> int:
        gearlist = vars(self)
        sp = 0
        for gear in gearlist:
            try:
                sp += gearlist[gear].spell_power
            except TypeError:
                continue

        return sp

    def calculate_spell_crit(self) -> float:
        gearlist = vars(self)
        sc = 0
        for gear in gearlist:
            try:
                sc += gearlist[gear].spell_crit
            except TypeError:
                continue

        return sc

    def calculate_spell_hit(self):
        gearlist = vars(self)
        sh = 0
        for gear in gearlist:
            try:
                sh += gearlist[gear].spell_hit
            except TypeError:
                continue

        return sh
