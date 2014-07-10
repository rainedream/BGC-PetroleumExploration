from worldcup.domain.states.state import State
from worldcup.domain.action import *

class Stimulated(State):
    def __init__(self):
        super().__init__()

    def stop(self, x, y):
        return Action(ActionType.STOP, x, y)


