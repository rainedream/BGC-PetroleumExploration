from worldcup.domain.states.state import State


class Position:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = State()
        self.expected_volume = 0
        self.produced_volume = 0
        self.produced_at_last_run = 0
        self.stimulation_has_effect = False

