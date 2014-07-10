class State:
    def buy(self, x, y):
        raise IllegalActionException('Buy')

    def explore(self, x, y):
        raise IllegalActionException('Explore')

    def drill(self, x, y):
        raise IllegalActionException('Drill')

    def stimulate(self, x, y):
        raise IllegalActionException('Stimulate')

    def stop(self, x, y):
        raise IllegalActionException('Stop Production')


class IllegalActionException(Exception):
    def __init__(self, action_name):
        super().__init__()
        self._action_name = action_name
