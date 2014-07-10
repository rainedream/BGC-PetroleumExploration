from worldcup.domain.states.state import State
from worldcup.domain.action import *

class Null(State):
    def __init__(self):
        super().__init__()

    def buy(self, x, y):
        return Action(ActionType.BUY, x, y)
