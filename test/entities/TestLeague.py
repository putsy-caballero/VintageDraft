from entities.entity_enums import *
from test.entities.TestSampleEntities import *
import unittest


class TestLeague(unittest.TestCase):
    def test_assign_points(self):
        stats = []
        stats.append(("a", 9))
        stats.append(("b", 8))
        stats.append(("c", 8))
        stats.append(("d", 7))
        stats.append(("e", 7))
        stats.append(("f", 7))
        stats.append(("g", 6))
        stats.append(("h", 5))
        stats.append(("i", 4))
        stats.append(("j", 4))
        output = League.assign_points(stats)
        expected_output = [(('a', 9), 10.0), (('b', 8), 8.5), (('c', 8), 8.5), (('d', 7), 6.0), (('e', 7), 6.0), (('f', 7), 6.0), (('g', 6), 4.0), (('h', 5), 3.0), (('i', 4), 1.5), (('j', 4), 1.5)]
        self.assertEqual(output, expected_output)

    def test_calculate_category_standings(self):
        league = TestSampleEntities.get_league()
        team1 = TestSampleEntities.get_team("1")
        team2 = TestSampleEntities.get_team("2")
        league.teams.append(team1)
        league.teams.append(team2)
        putsy = TestSampleEntities.get_putsy()
        slim = TestSampleEntities.get_slim()
        team1.add_player(putsy, Positions.second_base, 1948)
        team2.add_player(putsy, Positions.second_base, 1951)
        standings = league.calculate_standings()
        self.assertEqual(standings[Batter]['Career'][BattingCategories.HR][1], ((team2, 1.0), 1.5))
        self.assertEqual(standings[Batter]['BY'][BattingCategories.HR][1], ((team1, 0), 1.0))
        self.assertEqual(standings[Pitcher]['Career'][PitchingCategories.ERA][1], ((team2, 0), 1.5))
        team1.add_player(slim, Positions.pitcher, 1921)
        team2.add_player(slim, Positions.pitcher, 1923)
        standings = league.calculate_standings()
        self.assertEqual(standings[Batter]['Career'][BattingCategories.HR][1], ((team2, 1.0), 1.5))
        self.assertEqual(standings[Batter]['BY'][BattingCategories.HR][1], ((team1, 0), 1.0))
        self.assertEqual(standings[Pitcher]['BY'][PitchingCategories.W][1], ((team2, 10), 1.0))
        self.assertEqual(standings["Overall"][team1], 32)




if __name__ == '__main__':
    unittest.main()