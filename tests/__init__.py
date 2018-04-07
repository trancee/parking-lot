import unittest
import pytest


class MainTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys
