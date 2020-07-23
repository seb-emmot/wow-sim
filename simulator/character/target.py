from simulator.character.buffs import BuffName, Buff


class Target:

    def __init__(self, level, buffs: dict = None) -> None:
        super().__init__()

        self.level = level
        self.buffs = dict()

        if buffs is None:
            return
        else:
            for buff_name in buffs:
                self.add_buff(buffs[buff_name])

    def get_buff(self, buff_name: BuffName) -> Buff:
        return self.buffs[buff_name]

    def add_buff(self, buff: Buff):
        self.buffs[buff.name] = buff

    def remove_buff(self, buff_name: BuffName, stacks=0):
        buff = self.buffs[buff_name]
        if (buff.stacks - stacks) < 1 or stacks == 0:
            self.buffs.pop(buff_name)
        else:
            buff.stacks -= stacks

    def remove_expired_buffs(self, time : int):
        buffs_to_remove = []
        for buff_name in self.buffs:
            if self.buffs[buff_name].end_time <= time:
                buffs_to_remove.append(buff_name)

        for entry in buffs_to_remove:
            self.remove_buff(entry)


    @property
    def level(self) -> int:
        return self._level

    @level.setter
    def level(self, level):
        if level < 1 or level > 63:
            raise Exception("Level out of bounds")
        self._level = level

    def calculate_hit_chance(self, attacker):
        level_diff = abs(attacker.level - self.level)
        attacker_hit = attacker.stats.spell_hit if attacker.stats.spell_hit is not None else 0

        if level_diff == 0:
            hit_chance = 0.96 + attacker_hit
        elif level_diff == 1:
            hit_chance = 0.95 + attacker_hit
        elif level_diff == 2:
            hit_chance = 0.94 + attacker_hit
        elif level_diff == 3:
            hit_chance = 0.83 + attacker_hit
        else:
            raise Exception("Cannot handle level diffs of more than 3")

        # hit chance can never be above 99%
        return hit_chance if hit_chance < 1.0 else 0.99