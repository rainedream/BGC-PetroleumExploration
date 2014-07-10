
def enum(**enums):
    return type('Enum', (), enums)
ActionType = enum(BUY='Buy', EXPLORE='Explore', DRILL='Drill', STIMULATE='Stimulate', STOP='StopProduction')


class Action:
    def __init__(self, action_type, x, y):
        self._type = action_type
        self._x = x
        self._y = y

    def to_xml(self):
        pass