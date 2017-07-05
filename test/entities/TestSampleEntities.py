from entities.LeagueSettings import LeagueSettings
from entities.League import League
from entities.Batter import Batter, BatterStats
from entities.Pitcher import Pitcher, PitcherStats
from entities.Team import Team
from entities.User import User


class TestSampleEntities(object):
    @staticmethod
    def get_league_settings() -> LeagueSettings:
        return LeagueSettings(None, None, None, 200, None, 100, 100, 40, 17000, None)

    @staticmethod
    def get_league() -> League:
        league_settings = TestSampleEntities.get_league_settings()
        return League("Test League", league_settings, 720)

    @staticmethod
    def get_user() -> User:
        return User("test", "testpw", "Mike", "foo")

    @staticmethod
    def get_team() -> Team:
        return Team(TestSampleEntities.get_league(), "test league", TestSampleEntities.get_user())

    @staticmethod
    def get_putsy() -> Batter:
        master = {
            "playerID": "cabalpu01",
            "nameFirst": "Putsy",
            "nameLast": "Caballero"
        }
        batting_stats = [{
            "yearID": 1944,
            "G":   4,
            "AB":  4,
            "R":   0,
            "H":   0,
            "2B":  0,
            "3B":  0,
            "HR":  0,
            "RBI": 0,
            "SB":  0,
            "CS":  None,
            "BB":  0,
            "SO":  1,
            "IBB": None,
            "HBP": 0,
            "SH":  0,
            "SF":  None,
        }, {
            "yearID": 1945,
            "G":   9,
            "AB":  1,
            "R":   1,
            "H":   0,
            "2B":  0,
            "3B":  0,
            "HR":  0,
            "RBI": 1,
            "SB":  0,
            "CS":  None,
            "BB":  0,
            "SO":  0,
            "IBB": None,
            "HBP": 0,
            "SH":  0,
            "SF":  None,
        }, {
            "yearID": 1947,
            "G":   2,
            "AB":  7,
            "R":   2,
            "H":   1,
            "2B":  0,
            "3B":  0,
            "HR":  0,
            "RBI": 0,
            "SB":  0,
            "CS":  None,
            "BB":  1,
            "SO":  0,
            "IBB": None,
            "HBP": 0,
            "SH":  0,
            "SF":  None,
        }, {
            "yearID": 1948,
            "G":   113,
            "AB":  351,
            "R":   33,
            "H":   86,
            "2B":  12,
            "3B":  1,
            "HR":  0,
            "RBI": 19,
            "SB":  7,
            "CS":  None,
            "BB":  24,
            "SO":  18,
            "IBB": None,
            "HBP": 0,
            "SH":  5,
            "SF":  None,
        }, {
            "yearID": 1949,
            "G":   29,
            "AB":  69,
            "R":   8,
            "H":   19,
            "2B":  3,
            "3B":  0,
            "HR":  0,
            "RBI": 3,
            "SB":  0,
            "CS":  None,
            "BB":  0,
            "SO":  3,
            "IBB": None,
            "HBP": 0,
            "SH":  1,
            "SF":  None,
        }, {
            "yearID": 1950,
            "G":   46,
            "AB":  24,
            "R":   12,
            "H":   4,
            "2B":  0,
            "3B":  0,
            "HR":  0,
            "RBI": 0,
            "SB":  1,
            "CS":  None,
            "BB":  2,
            "SO":  2,
            "IBB": None,
            "HBP": 0,
            "SH":  0,
            "SF":  None,
        }, {
            "yearID": 1951,
            "G":   84,
            "AB":  161,
            "R":   15,
            "H":   30,
            "2B":  3,
            "3B":  2,
            "HR":  1,
            "RBI": 11,
            "SB":  1,
            "CS":  2,
            "BB":  12,
            "SO":  7,
            "IBB": None,
            "HBP": 0,
            "SH":  0,
            "SF":  None,
        }, {
            "yearID": 1952,
            "G":   35,
            "AB":  42,
            "R":   10,
            "H":   10,
            "2B":  3,
            "3B":  0,
            "HR":  0,
            "RBI": 6,
            "SB":  1,
            "CS":  0,
            "BB":  2,
            "SO":  3,
            "IBB": None,
            "HBP": 0,
            "SH":  1,
            "SF":  None,
        }]
        fielding_stats = [{
            "yearID":  1944,
            "Pos":     "3B",
            "G":       2,
            "GS":      0,
            "InnOuts": 24
        }, {
            "yearID":  1945,
            "Pos":     "3B",
            "G":       5,
            "GS":      0,
            "InnOuts": 30
        }, {
            "yearID":  1947,
            "Pos":     "2B",
            "G":       2,
            "GS":      2,
            "InnOuts": 39
        }, {
            "yearID":  1947,
            "Pos":     "3B",
            "G":       1,
            "GS":      0,
            "InnOuts": 6
        }, {
            "yearID":  1948,
            "Pos":     "3B",
            "G":       79,
            "GS":      73,
            "InnOuts": 1854
        }, {
            "yearID":  1948,
            "Pos":     "2B",
            "G":       23,
            "GS":      19,
            "InnOuts": 516
        }, {
            "yearID":  1949,
            "Pos":     "2B",
            "G":       21,
            "GS":      15,
            "InnOuts": 453
        }, {
            "yearID":  1949,
            "Pos":     "SS",
            "G":       1,
            "GS":      0,
            "InnOuts": 15
        }, {
            "yearID":  1950,
            "Pos":     "2B",
            "G":       5,
            "GS":      3,
            "InnOuts": 81
        }, {
            "yearID":  1950,
            "Pos":     "3B",
            "G":       4,
            "GS":      0,
            "InnOuts": 36
        }, {
            "yearID":  1950,
            "Pos":     "SS",
            "G":       2,
            "GS":      0,
            "InnOuts": 6
        }, {
            "yearID":  1951,
            "Pos":     "2B",
            "G":       54,
            "GS":      43,
            "InnOuts": 1198
        }, {
            "yearID":  1951,
            "Pos":     "3B",
            "G":       3,
            "GS":      0,
            "InnOuts": 12
        }, {
            "yearID":  1951,
            "Pos":     "SS",
            "G":       1,
            "GS":      0,
            "InnOuts": 6
        }, {
            "yearID":  1952,
            "Pos":     "SS",
            "G":       8,
            "GS":      3,
            "InnOuts": 138
        }, {
            "yearID":  1952,
            "Pos":     "2B",
            "G":       7,
            "GS":      1,
            "InnOuts": 59
        }, {
            "yearID":  1952,
            "Pos":     "3B",
            "G":       7,
            "GS":      4,
            "InnOuts": 144
        }]
        batter_stats = BatterStats(master, batting_stats, fielding_stats)
        return Batter(batter_stats)

    @staticmethod
    def get_slim() -> Pitcher:
        master = {
            "playerID": "harrisl01",
            "nameFirst": "Slim",
            "nameLast": "Harriss"
        }
        pitching_stats = [{
            "yearID": 1920,
            "W":      9,
            "L":      14,
            "G":      31,
            "GS":     25,
            "IPOuts": 576,
            "SV":     0,
            "H":      226,
            "ER":     87,
            "BB":     57,
            "SO":     60,
            "ERA":    4.08
        }, {
            "yearID": 1921,
            "W":      11,
            "L":      16,
            "G":      39,
            "GS":     28,
            "IPOuts": 683,
            "SV":     3,
            "H":      258,
            "ER":     108,
            "BB":     73,
            "SO":     92,
            "ERA":    4.27
        }, {
            "yearID": 1922,
            "W":      9,
            "L":      20,
            "G":      47,
            "GS":     32,
            "IPOuts": 689,
            "SV":     3,
            "H":      262,
            "ER":     128,
            "BB":     94,
            "SO":     102,
            "ERA":    5.02
        }, {
            "yearID": 1923,
            "W":      10,
            "L":      16,
            "G":      46,
            "GS":     28,
            "IPOuts": 628,
            "SV":     6,
            "H":      221,
            "ER":     93,
            "BB":     95,
            "SO":     89,
            "ERA":    4.00
        }, {
            "yearID": 1924,
            "W":      6,
            "L":      10,
            "G":      36,
            "GS":     13,
            "IPOuts": 369,
            "SV":     2,
            "H":      138,
            "ER":     64,
            "BB":     62,
            "SO":     45,
            "ERA":    4.68
        }, {
            "yearID": 1925,
            "W":      19,
            "L":      12,
            "G":      46,
            "GS":     33,
            "IPOuts": 758,
            "SV":     1,
            "H":      263,
            "ER":     98,
            "BB":     95,
            "SO":     95,
            "ERA":    3.49
        }, {
            "yearID": 1926,
            "W":      9,
            "L":      15,
            "G":      33,
            "GS":     28,
            "IPOuts": 510,
            "SV":     0,
            "H":      201,
            "ER":     82,
            "BB":     55,
            "SO":     47,
            "ERA":    4.34
        }, {
            "yearID": 1927,
            "W":      14,
            "L":      21,
            "G":      44,
            "GS":     27,
            "IPOuts": 653,
            "SV":     1,
            "H":      253,
            "ER":     101,
            "BB":     66,
            "SO":     77,
            "ERA":    4.18
        }, {
            "yearID": 1928,
            "W":      8,
            "L":      11,
            "G":      27,
            "GS":     15,
            "IPOuts": 385,
            "SV":     1,
            "H":      141,
            "ER":     66,
            "BB":     533,
            "SO":     37,
            "ERA":    4.63
        }]
        pitcher_stats = PitcherStats(master, pitching_stats)
        return Pitcher(pitcher_stats)