from unittest import TestCase
from worldcup.handlers.exploration_handler import parse_parameters


class RequestParserTest(TestCase):

    def test_should_parse_request_to_parameter_dict(self):
        request = "round=193&money=980000"
        params = parse_parameters(request)

        self.assertEquals('193', params['round'])
        self.assertEquals('980000', params['money'])
