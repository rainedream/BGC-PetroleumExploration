
def enum(**enums):
    return type('Enum', (), enums)
ActionType = enum(BUY='Buy', EXPLORE='Explore', DRILL='Drill', STIMULATE='Stimulate', STOP='StopProduction')


class Action:
    TEMPLATE_BUY = "<Execute>%s</Execute><BuyAtX>%d</BuyAtX><BuyAtY>%d</BuyAtY>"
    TEMPLATE_EXPLORE = "<Execute>%s</Execute><ExploreAtX>%d</ExploreAtX><ExploreAtY>%d</ExploreAtY><ServiceProvider>SLB</ServiceProvider>"
    TEMPLATE_DRILL = "<Execute>%s</Execute><DrillAtX>%d</DrillAtX><DrillAtY>%d</DrillAtY><ServiceProvider>SLB</ServiceProvider>"
    TEMPLATE_STIMULATE = "<Execute>%s</Execute><StimulateAtX>%d</StimulateAtX><StimulateAtY>%d</StimulateAtY><ServiceProvider>SLB</ServiceProvider>"
    TEMPLATE_STOP = "<Execute>%s</Execute><StopProductionAtX>%d</StopProductionAtX><StopProductionAtY>%d</StopProductionAtY>"

    def __init__(self, action_type, x, y):
        self._type = action_type
        self._x = x
        self._y = y

    def to_xml(self):
        if self._type == ActionType.BUY:
            return self.format_with_template(Action.TEMPLATE_BUY)
        elif self._type == ActionType.EXPLORE:
            return self.format_with_template(Action.TEMPLATE_EXPLORE)
        elif self._type == ActionType.DRILL:
            return self.format_with_template(Action.TEMPLATE_DRILL)
        elif self._type == ActionType.STIMULATE:
            return self.format_with_template(Action.TEMPLATE_STIMULATE)
        elif self._type == ActionType.STOP:
            return self.format_with_template(Action.TEMPLATE_STOP)

    def format_with_template(self, template):
        return template % (self._type, self._x, self._y)