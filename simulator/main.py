import json

from simulator.character.buffs import BuffName, WintersChill
from simulator.character.character import Mage
from simulator.character.target import Target
from simulator.gear import GearSet
from simulator.character.talents import Talents
from simulator.character.enums import Race
from simulator.spellfactory import SpellFactory


def main(gear_config, bolts):

    with open(gear_config, "r") as f:
        gear_file_content = f.read()

    talent_dict = {
        "improved_frostbolt": 5,
        "elemental_precision": 3,
        "ice_shards": 5,
        "piercing_ice": 3,
    }

    gear_dict = json.loads(gear_file_content)

    gear = GearSet(gear_dict)
    talents = Talents(talent_dict)
    char = Mage(Race.Human, talents, gear, 60)

    target_buffs = {BuffName.WintersChill: WintersChill(0, 1000, 0)}
    target = Target(63, target_buffs)

    spell_factory = SpellFactory()

    casts = spell_factory.spell_generator(char, target, bolts)

    return casts


if __name__ == "__main__":

    gear_filename = "config/gear.json"
    num_bolts = 100

    total_dmg = 0
    hits = list(main(gear_filename, num_bolts))
    for entry in hits:
        print(entry.timestamp, entry.damage)
        total_dmg += entry.damage
    print(total_dmg)
