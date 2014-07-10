from unittest import TestCase
from worldcup.domain.action import *

class ActionTest(TestCase):

    def test_should_convert_action_buy_to_xml(self):
        action = Action(ActionType.BUY, 1, 2)
        expected_xml = "<Execute>Buy</Execute><BuyAtX>1</BuyAtX><BuyAtY>2</BuyAtY>"

        self.assertEquals(expected_xml, action.to_xml())

    def test_should_convert_action_explore_to_xml(self):
        action = Action(ActionType.EXPLORE, 2, 3)
        expected_xml = "<Execute>Explore</Execute><ExploreAtX>2</ExploreAtX><ExploreAtY>3</ExploreAtY><ServiceProvider>SLB</ServiceProvider>"

        self.assertEquals(expected_xml, action.to_xml())

    def test_should_convert_action_drill_to_xml(self):
        action = Action(ActionType.DRILL, 2, 3)
        expected_xml = "<Execute>Drill</Execute><DrillAtX>2</DrillAtX><DrillAtY>3</DrillAtY><ServiceProvider>SLB</ServiceProvider>"

        self.assertEquals(expected_xml, action.to_xml())

    def test_should_convert_action_stimulate_to_xml(self):
        action = Action(ActionType.STIMULATE, 2, 3)
        expected_xml = "<Execute>Stimulate</Execute><StimulateAtX>2</StimulateAtX><StimulateAtY>3</StimulateAtY><ServiceProvider>SLB</ServiceProvider>"

        self.assertEquals(expected_xml, action.to_xml())

    def test_should_convert_action_stop_to_xml(self):
        action = Action(ActionType.STOP, 2, 3)
        expected_xml = "<Execute>StopProduction</Execute><StopProductionAtX>2</StopProductionAtX><StopProductionAtY>3</StopProductionAtY>"

        self.assertEquals(expected_xml, action.to_xml())