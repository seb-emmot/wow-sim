from unittest import TestCase

from simulator.character.stats import BaseStats, PrimaryStats, AttributeMultipliers
from simulator.character.talents import Talents


class TestBaseStats(TestCase):
    def test_base_stats(self):
        a = BaseStats()
        a.shared = 10
        a.only_a = 333

        b = BaseStats()
        b.shared = 5
        b.only_b = 666

        c = a + b

        assert c.shared == 15
        assert c.only_b == 666
        assert c.only_a == 333

    def test_primary_stats(self):
        stat = PrimaryStats(4, 2, 1, 8, 9)

        self.assertEqual(stat.strength, 4)
        self.assertEqual(stat.agility, 2)
        self.assertEqual(stat.stamina, 1)
        self.assertEqual(stat.intellect, 8)
        self.assertEqual(stat.spirit, 9)

    def test_update_secondary_stats(self):
        stat = BaseStats()
        stat.update_secondary_stats()

        self.assertEqual(stat.armor, 0)
        self.assertEqual(stat.mana, 0)
        self.assertEqual(stat.health, 0)

    def test_update_secondary_stats_hmage(self):
        stat = BaseStats()
        stat += PrimaryStats(30, 35, 45, 125, 120)

        stat.update_secondary_stats()

        self.assertEqual(stat.armor, 70)
        self.assertEqual(stat.mana, 1875)
        self.assertEqual(stat.health, 450)

    def test_update_from_talents(self):
        stat = BaseStats()
        talent_dict = {
            "elemental_precision": 3,
            "ice_shards": 5,
            "piercing_ice": 3,
        }
        talents = Talents(talent_dict)

        stat.update_from_talents(talents)

        self.assertEqual(stat.spell_crit_multiplier, 1.0)
        self.assertEqual(stat.spell_damage_multiplier, 1.06)


class TestAttributeMultipliers(TestCase):

    def test_setup_multiplier(self):
        multipliers = AttributeMultipliers(1, 2, 3, 4, 5)

        self.assertEqual(multipliers.strength_multiplier, 1)
        self.assertEqual(multipliers.agility_multiplier, 2)
        self.assertEqual(multipliers.stamina_multiplier, 3)
        self.assertEqual(multipliers.intellect_multiplier, 4)
        self.assertEqual(multipliers.spirit_multiplier, 5)

    def test_multiply_multipliers(self):
        first = AttributeMultipliers(1.1, 2, 3, 4, 5)
        second = AttributeMultipliers(5, 4, 3, 2, 1)

        product = first * second

        self.assertEqual(product.strength_multiplier, 5.5)
        self.assertEqual(product.agility_multiplier, 8.0)
        self.assertEqual(product.stamina_multiplier, 9.0)
        self.assertEqual(product.intellect_multiplier, 8.0)
        self.assertEqual(product.spirit_multiplier, 5.0)
