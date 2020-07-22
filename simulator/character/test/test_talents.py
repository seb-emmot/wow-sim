from unittest import TestCase

from simulator.character.talents import Talents


class TestTalents(TestCase):

    def test_setup_talents(self):
        talent_dict = {"improved_frostbolt": 5}
        talents = Talents(talent_dict)

        for entry in talent_dict:
            talent = getattr(talents, entry)
            self.assertEqual(talent, talent_dict[entry])

    def test_setup_invalid_talents(self):
        talent_dict = {"nonexistant_talent": 5}

        self.assertRaises(AttributeError, Talents, talent_dict)

    def test_setup_empty_talents(self):
        talents = Talents({})

        attr_dict = vars(talents)
        for entry in attr_dict:
            self.assertEqual(attr_dict[entry], 0)

    def test_add_spell_modifiers(self):
        talent_dict = {
            "elemental_precision": 3,
            "ice_shards": 5,
            "piercing_ice": 3,
        }
        talents = Talents(talent_dict)

        spell_stats = talents.get_spell_modifiers()
