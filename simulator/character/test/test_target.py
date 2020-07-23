from unittest import TestCase

from simulator.character.buffs import Buff
from simulator.character.target import Target


class MyTestCase(TestCase):
    
    def setUp(self) -> None:
        super().setUp()
        self.target = Target(63)

    def test_setup_target(self):
        self.assertEqual(self.target.level, 63)
        self.assertEqual(len(self.target.buffs), 0)

    def test_add_buff(self):
        buffone = Buff(0, 1, 0, 1000)
        self.target.add_buff(buffone)

        self.assertEqual(self.target.get_buff(0), buffone)
        self.assertEqual(len(self.target.buffs), 1)

    def test_remove_buff(self):
        self._setup_single_buff_case()

        self.target.remove_buff(0)

        self.assertRaises(KeyError, self.target.get_buff, 0)
        self.assertEqual(len(self.target.buffs), 0)

    def test_remove_non_existant_buff(self):
        self.assertRaises(KeyError, self.target.remove_buff, 0)

    def test_remove_expired_buffs(self):
        self._setup_single_buff_case()

        self.assertEqual(len(self.target.buffs), 1)

        self.target.remove_expired_buffs(1500)

        self.assertRaises(KeyError, self.target.get_buff, 0)
        self.assertEqual(len(self.target.buffs), 0)

    def test_remove_multiple_expired_buffs(self):
        self._setup_multi_buff_case()
        self.assertEqual(len(self.target.buffs), 3)

        self.target.remove_expired_buffs(2001)

        self.assertEqual(len(self.target.buffs), 1)
        self.assertEqual(self.target.buffs[2].end_time > 2001, True)

    def _setup_single_buff_case(self):
        buff = Buff(0, 1, 0, 1000)
        self.target.add_buff(buff)

    def _setup_multi_buff_case(self):
        buffone = Buff(0, 1, 0, 1000)
        bufftwo = Buff(1, 1, 500, 2000)
        buffthree = Buff(2, 1, 0, 4000)

        self.target.add_buff(buffone)
        self.target.add_buff(bufftwo)
        self.target.add_buff(buffthree)

