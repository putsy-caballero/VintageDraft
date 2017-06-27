from entities.LeagueSettings import Positions
from entities.Player import Player

class BatterStats(object):

    def __init__(self, master, batting_stats, fielding_stats):
        self.playerID = master["playerID"]
        self.first_name = master["nameFirst"]
        self.last_name = master["nameLast"]
        for entry in batting_stats:
            self.batting_year_stats[entry["yearID"]] = {}
            for field in ["G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB", "CS", "BB", "SO", "IBB", "HBP", "SH", "SF"]:
                self.batting_year_stats[entry["year_ID"]][field] = entry[field]
                self.batting_career_stats[field] += entry[field]

        position_map = {
            "C": Positions.catcher,
            "1B": Positions.first_base,
            "2B": Positions.second_base,
            "3B": Positions.third_base,
            "SS": Positions.shortstop,
            "LF": Positions.left_field,
            "CF": Positions.center_field,
            "RF": Positions.right_field
        }

        for year in fielding_stats["year_ID"]:
            for posn in year:
                if posn["Pos"] in position_map:
                    pos = position_map[posn["Pos"]]
                    self.fielding_stats[year][pos] = {}
                    for field in ["G", "GS", "InnOuts"]:
                        self.fielding_stats[year][pos][field] = posn[field]
                        self.fielding_career_stats[pos][field] += posn[field]

class Batter(Player):
    def __init__(self, playerID, firstname, lastname, year, career_stats, year_stats):
        super().__init__(playerID, firstname, lastname, year, career_stats, year_stats)

    def valid_year(self, year, league_settings):
        batting_year_stats = self.year_stats[year]
        return batting_year_stats["AB"] >= league_settings.min_ab_year

    def pos_qual_career(self, position, year, league_settings):
        return self.fielding_career_stats[position]["G"] >= league_settings.pos_qual_career
