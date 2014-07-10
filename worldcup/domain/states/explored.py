from worldcup.domain.states.state import State
from worldcup.domain.action import *

class Explored(State):
    def __init__(self):
        super().__init__()

    def drill(self, x, y):
        return Action(ActionType.DRILL, x, y)