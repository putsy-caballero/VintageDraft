from entities.entity_enums import Positions
from entities.Player import Player


class PitcherStats(object):
    def __init__(self, master, pitching_stats):
        self.playerID = master["playerID"]
        self.first_name = master["nameFirst"]
        self.last_name = master["nameLast"]
        self.pitching_year_stats = {}
        self.pitching_career_stats = {}
        for entry in pitching_stats:
            self.pitching_year_stats[entry["yearID"]] = {}
            for field in ["W", "L", "G", "GS", "IPOuts", "SV", "H", "ER", "BB", "SO", "ERA"]:
                if field in entry and entry[field] != None:
                    self.pitching_year_stats[entry["yearID"]][field] = entry[field]
                    self.pitching_career_stats[field] = self.pitching_career_stats.get(field, 0) + entry[field]
                else:
                    self.pitching_year_stats[entry["yearID"]][field] = None
            self.pitching_year_stats[entry["yearID"]]["WHIP"] = 3 * (self.pitching_year_stats[entry["yearID"]]["H"] + self.pitching_year_stats[entry["yearID"]]["BB"]) / self.pitching_year_stats[entry["yearID"]]["IPOuts"]
        self.pitching_career_stats["ERA"] = self.pitching_career_stats["ER"] * 27 / self.pitching_career_stats["IPOuts"]
        self.pitching_career_stats["WHIP"] = 3 * (self.pitching_career_stats["H"] + self.pitching_career_stats["BB"]) / self.pitching_career_stats["IPOuts"]


class Pitcher(Player):

    def __init__(self, stats: PitcherStats):
        super().__init__(stats.playerID, stats.first_name, stats.last_name, stats)

    def valid_year(self, year, league_settings):
        if year not in self.stats.pitching_year_stats:
            return False
        return self.stats.pitching_year_stats[year]["IPOuts"] >= league_settings.min_ip_year * 3 or self.stats.pitching_year_stats[year]["G"] > league_settings.min_gp_year

    def pos_qual_career(self, position, league_settings):
        return position == Positions.pitcher

