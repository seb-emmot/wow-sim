from simulator.character.stats import PrimaryStats
from simulator.gear import GearSet


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
