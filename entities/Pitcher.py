from entities import db
from entities.entity_enums import Positions
from entities.Player import Player

class PitcherYearStats(db.Model):
    playerID = db.Column(db.String(9), primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    W = db.Column(db.Integer, nullable=False)
    L = db.Column(db.Integer, nullable=False)
    G = db.Column(db.Integer, nullable=False)
    SV = db.Column(db.Integer, nullable=False)
    IPouts = db.Column(db.Integer, nullable=False)
    H = db.Column(db.Integer, nullable=False)
    ER = db.Column(db.Integer, nullable=False)
    BB = db.Column(db.Integer, nullable=False)
    SO = db.Column(db.Integer, nullable=False)
    ERA = db.Column(db.Float, nullable=False)
    WHIP = db.Column(db.Float, nullable=False)

    def __init__(self, id, year, stats):
        self.playerID = id
        self.year = year
        self.W = stats['W']
        self.L = stats['L']
        self.G = stats['G']
        self.SV = stats['SV']
        self.IPouts = stats['IPouts']
        self.H = stats['H']
        self.ER = stats['ER']
        self.BB = stats['BB']
        self.SO = stats['SO']
        self.ERA = stats['ERA']
        self.WHIP = stats['WHIP']

class PitcherCareerStats(db.Model):
    playerID = db.Column(db.String(9), primary_key=True)
    W = db.Column(db.Integer, nullable=False)
    L = db.Column(db.Integer, nullable=False)
    G = db.Column(db.Integer, nullable=False)
    SV = db.Column(db.Integer, nullable=False)
    IPouts = db.Column(db.Integer, nullable=False)
    H = db.Column(db.Integer, nullable=False)
    ER = db.Column(db.Integer, nullable=False)
    BB = db.Column(db.Integer, nullable=False)
    SO = db.Column(db.Integer, nullable=False)
    ERA = db.Column(db.Float, nullable=False)
    WHIP = db.Column(db.Float, nullable=False)

    def __init__(self, id, stats):
        self.playerID = id
        self.W = stats['W']
        self.L = stats['L']
        self.G = stats['G']
        self.SV = stats['SV']
        self.IPouts = stats['IPouts']
        self.H = stats['H']
        self.ER = stats['ER']
        self.BB = stats['BB']
        self.SO = stats['SO']
        self.ERA = stats['ERA']
        self.WHIP = stats['WHIP']


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

