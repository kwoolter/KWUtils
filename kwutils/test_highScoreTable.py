from unittest import TestCase

from kwutils.KWGameClasses import *


class TestHighScoreTable(TestCase):

    def test_add(self):
        table = HighScoreTable("Zelda", 4)
        table.add("KAW", 1000)
        table.add("JHW", 5655)
        table.add("REW", 115655)
        self.fail()

    def test_is_high_score(self):
        self.fail()

    def test_save(self):
        self.fail()

    def test_load(self):
        self.fail()

    def test_print(self):
        self.fail()
