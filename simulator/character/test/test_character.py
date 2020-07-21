from unittest import TestCase
from simulator.character.character import *
from simulator.character.talents import Talents


class TestCharacter(TestCase):

    def test_setup_human_mage(self):
        talents = Talents({})
        gear_dict = {}
        gear = GearSet(gear_dict)
        char = Mage(Race.Human, talents, gear, 60)

        self.assertEqual(char.race, Race.Human)
        self.assertEqual(char.level, 60)
        self.assertEqual(char.talents, talents)
