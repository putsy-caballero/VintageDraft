from entities.entity_enums import *
from test.entities.TestSampleEntities import *
import unittest


class TestPitcher(unittest.TestCase):
    def test_valid_year(self):
        league_settings = TestSampleEntities.get_league_settings()
        slim = TestSampleEntities.get_slim()
        self.assertTrue(slim.valid_year(1920, league_settings))
        league_settings.min_ip_year = 200
        self.assertFalse(slim.valid_year(1924, league_settings))
        self.assertFalse(slim.valid_year(1965, league_settings))

    def test_pos_qual_career(self):
        league_settings = TestSampleEntities.get_league_settings()
        slim = TestSampleEntities.get_slim()
        self.assertTrue(slim.pos_qual_career(Positions.pitcher, league_settings))
        self.assertFalse(slim.pos_qual_career(Positions.second_base, league_settings))

if __name__ == '__main__':
    unittest.main()