import json

from character import Mage, Target
from gear import GearSet
from stats import Race


# Currently only exists for testing
def main(gear_config, bolts):

    with open(gear_config, "r") as f:
        gear_file_content = f.read()

    gear_dict = json.loads(gear_file_content)

    gear = GearSet(gear_dict)

    char = Mage(Race.Human, gear, 60)
    target = Target(63)

    casts = char.frostbolt_generator(target, bolts)

    return casts


if __name__ == "__main__":

    gear = "config/gear.json"
    num_bolts = 100

    hits = list(main(gear, num_bolts))
    print(len(hits))
