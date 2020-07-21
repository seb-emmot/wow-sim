from unittest import TestCase

from simulator.character.stats import BaseStats, PrimaryStats


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