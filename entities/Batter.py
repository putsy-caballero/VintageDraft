from entities import db
from entities.entity_enums import Positions
from entities.Player import Player

class BatterYearStats(db.Model):
    playerID = db.Column(db.String(9), primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    G = db.Column(db.Integer, nullable=False)
    AB = db.Column(db.Integer, nullable=False)
    R = db.Column(db.Integer, nullable=False)
    H = db.Column(db.Integer, nullable=False)
    DOUBLES = db.Column(db.Integer, nullable=False)
    TRIPLES = db.Column(db.Integer, nullable=False)
    HR = db.Column(db.Integer, nullable=False)
    RBI = db.Column(db.Integer, nullable=False)
    SB = db.Column(db.Integer, nullable=False)
    CS = db.Column(db.Integer, nullable=False)
    BB = db.Column(db.Integer, nullable=False)
    SO = db.Column(db.Integer, nullable=False)
    IBB = db.Column(db.Integer, nullable=False)
    HBP = db.Column(db.Integer, nullable=False)
    SH = db.Column(db.Integer, nullable=False)
    SF = db.Column(db.Integer, nullable=False)
    AVG = db.Column(db.Float, nullable=False)
    OBP = db.Column(db.Float, nullable=False)
    SLG = db.Column(db.Float, nullable=False)

    def __init__(self, id, year, stats):
        self.playerID = id
        self.year = year
        self.G = stats['G']
        self.AB = stats['AB']
        self.R = stats['R']
        self.H = stats['H']
        self.DOUBLES = stats['2B']
        self.TRIPLES = stats['3B']
        self.HR = stats['HR']
        self.RBI = stats['RBI']
        self.SB = stats['SB']
        self.CS = stats['CS']
        self.BB = stats['BB']
        self.SO = stats['SO']
        self.IBB = stats['IBB']
        self.HBP = stats['HBP']
        self.SH = stats['SH']
        self.SF = stats['SF']
        self.AVG = stats['AVG']
        self.OBP = stats['OBP']
        self.SLG = stats['SLG']

class BatterCareerStats(db.Model):
    playerID = db.Column(db.String(9), primary_key=True)
    G = db.Column(db.Integer, nullable=False)
    AB = db.Column(db.Integer, nullable=False)
    R = db.Column(db.Integer, nullable=False)
    H = db.Column(db.Integer, nullable=False)
    DOUBLES = db.Column(db.Integer, nullable=False)
    TRIPLES = db.Column(db.Integer, nullable=False)
    HR = db.Column(db.Integer, nullable=False)
    RBI = db.Column(db.Integer, nullable=False)
    SB = db.Column(db.Integer, nullable=False)
    CS = db.Column(db.Integer, nullable=False)
    BB = db.Column(db.Integer, nullable=False)
    SO = db.Column(db.Integer, nullable=False)
    IBB = db.Column(db.Integer, nullable=False)
    HBP = db.Column(db.Integer, nullable=False)
    SH = db.Column(db.Integer, nullable=False)
    SF = db.Column(db.Integer, nullable=False)
    AVG = db.Column(db.Float, nullable=False)
    OBP = db.Column(db.Float, nullable=False)
    SLG = db.Column(db.Float, nullable=False)

    def __init__(self, id, stats):
        self.playerID = id
        self.G = stats['G']
        self.AB = stats['AB']
        self.R = stats['R']
        self.H = stats['H']
        self.DOUBLES = stats['2B']
        self.TRIPLES = stats['3B']
        self.HR = stats['HR']
        self.RBI = stats['RBI']
        self.SB = stats['SB']
        self.CS = stats['CS']
        self.BB = stats['BB']
        self.SO = stats['SO']
        self.IBB = stats['IBB']
        self.HBP = stats['HBP']
        self.SH = stats['SH']
        self.SF = stats['SF']
        self.AVG = stats['AVG']
        self.OBP = stats['OBP']
        self.SLG = stats['SLG']

class FielderPositionStats(db.Model):
    playerID = db.Column(db.String(9), primary_key=True)
    pos = db.Column(db.Enum(Positions), primary_key=True)
    G = db.Column(db.Integer, nullable=False)
    GS = db.Column(db.Integer, nullable=False)
    InnOuts = db.Column(db.Integer, nullable=False)

    def __init__(self, id, pos, stats):
        self.playerID = id
        self.pos = pos
        self.G = stats['G']
        self.GS = stats['GS']
        self.InnOuts = stats['InnOuts']

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
