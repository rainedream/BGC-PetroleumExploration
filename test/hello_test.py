from unittest import TestCase
from worldcup import hello


class HelloTest(TestCase):

    def setUp(self):
        return

    def test_say_hello(self):
        something = hello.say_hello()
        self.assertEquals("Hello World", something)