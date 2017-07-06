from entities.entity_enums import *
from entities.Batter import Batter
from entities.LeagueSettings import LeagueSettings

import unittest


class TestLeagueSettings(unittest.TestCase):
    def test_init(self):
        league_settings = LeagueSettings(None, None, None, 200, None, 100, 100, 40, 17000, None, None, None)
        self.assertEqual(league_settings.league_type, LeagueType.decades)
        self.assertEqual(league_settings.scoring_type, ScoringType.additive)
        self.assertEqual(league_settings.positions[Positions.catcher], (2, 2))
        self.assertEqual(league_settings.pos_qual_career, 200)
        self.assertEqual(league_settings.avg_obp, AvgObp.avg)
        self.assertEqual(league_settings.min_ab_year, 100)
        self.assertEqual(league_settings.min_ip_year, 100)
        self.assertEqual(league_settings.min_gp_year, 40)
        self.assertEqual(league_settings.team_career_ip, 17000)
        self.assertEqual(league_settings.type_distribution[Batter][Decades.dec_1870s], (0, 1))
        self.assertListEqual(league_settings.batting_categories, [BattingCategories.HR, BattingCategories.R, BattingCategories.RBI, BattingCategories.SB, BattingCategories.AVG])
        self.assertListEqual(league_settings.pitching_categories, [PitchingCategories.ERA, PitchingCategories.WHIP, PitchingCategories.W, PitchingCategories.SO, PitchingCategories.SV])
#        league_settings = LeagueSettings(LeagueType.decades, ScoringType.additive, None, 200, None, 100, 40, 17000, None)

if __name__ == '__main__':
    unittest.main()