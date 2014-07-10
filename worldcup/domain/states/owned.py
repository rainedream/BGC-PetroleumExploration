from worldcup.domain.states.state import State
from worldcup.domain.action import *

class Owned(State):
    def __init__(self):
        super().__init__()

    def explore(self, x, y):
        return Action(ActionType.EXPLORE, x, y)

    def drill(self, x, y):
        return Action(ActionType.DRILL, x, y)