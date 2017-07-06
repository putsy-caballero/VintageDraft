from entities.entity_enums import *
from test.entities.TestSampleEntities import *
import unittest


class TestBatter(unittest.TestCase):
    def test_valid_year(self):
        league_settings = TestSampleEntities.get_league_settings()
        putsy = TestSampleEntities.get_putsy()
        self.assertTrue(putsy.valid_year(1948, league_settings))
        self.assertFalse(putsy.valid_year(1949, league_settings))
        self.assertFalse(putsy.valid_year(1965, league_settings))

    def test_pos_qual_career(self):
        league_settings = TestSampleEntities.get_league_settings()
        putsy = TestSampleEntities.get_putsy()
        self.assertTrue(putsy.pos_qual_career(Positions.second_base, league_settings))
        self.assertFalse(putsy.pos_qual_career(Positions.third_base, league_settings))
        league_settings.pos_qual_career = 100
        self.assertTrue(putsy.pos_qual_career(Positions.third_base, league_settings))

if __name__ == '__main__':
    unittest.main()