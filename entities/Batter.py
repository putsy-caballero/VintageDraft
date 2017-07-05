from entities.entity_enums import Positions
from entities.Player import Player


class BatterStats(object):

    def __init__(self, master, batting_stats, fielding_stats):
        self.playerID = master["playerID"]
        self.first_name = master["nameFirst"]
        self.last_name = master["nameLast"]
        self.batting_year_stats = {}
        self.batting_career_stats = {}
        for entry in batting_stats:
            self.batting_year_stats[entry["yearID"]] = {}
            for field in ["G", "AB", "R", "H", "2B", "3B", "HR", "RBI", "SB", "CS", "BB", "SO", "IBB", "HBP", "SH", "SF"]:
                if field in entry and entry[field] != None:
                    self.batting_year_stats[entry["yearID"]][field] = entry[field]
                    self.batting_career_stats[field] = self.batting_career_stats.get(field, 0) + entry[field]
                else:
                    self.batting_year_stats[entry["yearID"]][field] = None
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

        self.fielding_stats = {}
        self.fielding_career_stats = {}
        for entry in fielding_stats:
            year = entry["yearID"]
            if year not in self.fielding_stats:
                self.fielding_stats[year] = {}
            if entry["Pos"] in position_map:
                pos = position_map[entry["Pos"]]
                self.fielding_stats[year][pos] = {}
                if pos not in self.fielding_career_stats:
                    self.fielding_career_stats[pos] = {}
                for field in ["G", "GS", "InnOuts"]:
                    self.fielding_stats[year][pos][field] = entry[field]
                    self.fielding_career_stats[pos][field] = self.fielding_career_stats[pos].get(field, 0) + entry[field]


class Batter(Player):
    def __init__(self, stats: BatterStats):
        super().__init__(stats.playerID, stats.first_name, stats.last_name, stats)

    def valid_year(self, year, league_settings):
        return year in self.stats.batting_year_stats and self.stats.batting_year_stats[year]["AB"] >= league_settings.min_ab_year

    def pos_qual_career(self, position, league_settings):
        if position == Positions.middle_infield:
            return self.pos_qual_career(Positions.second_base, league_settings) or self.pos_qual_career(Positions.shortstop, league_settings)
        if position == Positions.corner_infield:
            return self.pos_qual_career(Positions.first_base, league_settings) or self.pos_qual_career(Positions.third_base, league_settings)
        if position not in self.stats.fielding_career_stats:
            return False
        if self.stats.fielding_career_stats[position]["G"] >= league_settings.pos_qual_career:
            return True
        max_games = -1
        for k in self.stats.fielding_career_stats:
            if self.stats.fielding_career_stats[k]["G"] > max_games:
                max_games = self.stats.fielding_career_stats[k]["G"]
        if max_games < league_settings.pos_qual_career and self.stats.fielding_career_stats[position]["G"] == max_games:
            return True
        return False
