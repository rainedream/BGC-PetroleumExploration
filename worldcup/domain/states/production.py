from worldcup.domain.states.state import State
from worldcup.domain.action import *

class Production(State):
    def __init__(self):
        super().__init__()

    def stimulate(self, x, y):
        return Action(ActionType.STIMULATE, x, y)

    def stop(self, x, y):
        return Action(ActionType.STOP, x, y)
