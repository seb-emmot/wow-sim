class Talents:

    def __init__(self) -> None:
        super().__init__()

    def get_base_attribute_modifiers(self):
        pass


class Buff:
    def __init__(self, start_time, end_time) -> None:
        super().__init__()
        self.start_time = start_time
        self.end_time = end_time
