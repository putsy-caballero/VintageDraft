from entities.Player import Player

class PitcherStats(object):
    def __init__(self, master, pitching_stats):
        self.playerID = master["playerID"]
        self.first_name = master["nameFirst"]
        self.last_name = master["nameLast"]
        for entry in pitching_stats:
            self.pitching_year_stats[entry["yearID"]] = {}
            for field in ["W", "L", "G", "GS", "IPOuts", "SV", "H", "ER", "BB", "SO", "ERA"]:
                self.pitching_year_stats[entry["year_ID"]][field] = entry[field]
                self.pitching_career_stats[field] += entry[field]
            self.pitching_year_stats[entry["year_ID"]]["WHIP"] = 3 * (self.pitching_year_stats["H"] + self.pitching_year_stats["BB"]) / self.pitching_year_stats["IPOuts"]
        self.pitching_career_stats["ERA"] = self.pitching_career_stats["ER"] * 27 / self.pitching_career_stats["IPOuts"]
        self.pitching_career_stats["WHIP"] = 3 * (self.pitching_career_stats["H"] + self.pitching_career_stats["BB"]) / self.pitching_career_stats["IPOuts"]

class Pitcher(Player):

    def __init__(self, playerID, firstname, lastname, year, career_stats, year_stats):
        super().__init__(playerID, firstname, lastname, year, career_stats, year_stats)

    def valid_year(self, year, league_settings):
        return self.year_stats[year]["IP"] >= league_settings.min_ip_year

    def pos_qual_career(self, position, league_settings):
        return True

