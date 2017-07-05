from entities.entity_enums import *
from entities.Errors import *
from test.entities.TestSampleEntities import *
import unittest


class TestTeam(unittest.TestCase):
    def test_get_team_decades(self):
        team = TestSampleEntities.get_team()
        putsy = TestSampleEntities.get_putsy()
        team.add_player(putsy, Positions.second_base, 1948)
        decade_players = team.get_team_decades()
        self.assertTrue(decade_players[Batter][Decades.dec_1940s] == 1)
        team.add_player(putsy, Positions.middle_infield, 1951)
        decade_players = team.get_team_decades()
        self.assertTrue(decade_players[Batter][Decades.dec_1940s] == 1)
        self.assertTrue(decade_players[Batter][Decades.dec_1950s] == 1)
        slim = TestSampleEntities.get_slim()
        team.add_player(slim, Positions.pitcher, 1922)
        decade_players = team.get_team_decades()
        self.assertTrue(decade_players[Pitcher][Decades.dec_1920s] == 1)

    def test_add_player(self):
        team = TestSampleEntities.get_team()
        putsy = TestSampleEntities.get_putsy()
        team.add_player(putsy, Positions.second_base, 1948)
        self.assertEqual(team.players[Batter][Positions.second_base][0][0], putsy)
        self.assertTrue(team.players[Batter][Positions.second_base][0][1] == 1948)
        with self.assertRaises(PositionFullError):
            team.add_player(putsy, Positions.second_base, 1951)
        with self.assertRaises(DecadeFullError):
            team.add_player(putsy, Positions.middle_infield, 1948)
        with self.assertRaises(InvalidYearError):
            team.add_player(putsy, Positions.middle_infield, 1947)
        with self.assertRaises(InvalidPositionError):
            team.add_player(putsy, Positions.first_base, 1948)

    def test_generate_stats(self):
        team = TestSampleEntities.get_team()
        putsy = TestSampleEntities.get_putsy()
        team.add_player(putsy, Positions.second_base, 1948)
        team.add_player(putsy, Positions.middle_infield, 1951)
        stats = team.generate_stats()
        self.assertEqual(stats[Batter]["Career"]["HR"], 2)
        self.assertEqual(stats[Batter]["BY"]["RBI"], 30)
        self.assertAlmostEqual(stats[Batter]["BY"]["AVG"], 116/512)
        slim = TestSampleEntities.get_slim()
        team.add_player(slim, Positions.pitcher, 1922)
        stats = team.generate_stats()
        self.assertEqual(stats[Pitcher]["Career"]["W"], 95)
        self.assertEqual(stats[Pitcher]["BY"]["L"], 20)
        self.assertAlmostEqual(stats[Pitcher]["BY"]["WHIP"], 1.550, 3)

if __name__ == '__main__':
    unittest.main()