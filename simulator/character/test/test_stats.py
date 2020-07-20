from simulator.character.stats import BaseStats


class TestBaseStats:
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