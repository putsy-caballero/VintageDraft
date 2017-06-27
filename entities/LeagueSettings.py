from entities.Batter import Batter
from entities.entity_enums import LeagueType, ScoringType, Positions, AvgObp, Decades, Categories
from entities.Pitcher import Pitcher
import uuid

class LeagueSettings(object):

    def __init__(self, league_type, scoring_type, positions, pos_qual_career, avgobp, min_ab_year, min_ip_year, team_career_ip, type_distribution):
        self.uuid = uuid.uuid4()
        if (isinstance(league_type, LeagueType)):
            self.league_type = league_type
        else:
            self.league_type = LeagueType.decades
        if (isinstance(scoring_type, ScoringType)):
            self.scoring_type = scoring_type
        else:
            self.scoring_type = ScoringType.additive
        if (isinstance(positions, dict) and len(dict) > 0):
            self.positions = positions
        else:
            positions = {
                Positions.catcher: (2, 2),
                Positions.first_base: (1, 1),
                Positions.second_base: (1, 1),
                Positions.shortstop: (1, 1),
                Positions.third_base: (1, 1),
                Positions.corner_infield: (1, 1),
                Positions.middle_infield: (1, 1),
                Positions.outfield: (5, 5),
                Positions.hitter_utility: (2, 2),
                Positions.pitcher: (12, 12),
            }
        self.pos_qual_career = pos_qual_career
        if (isinstance(avgobp, AvgObp)):
            self.avg_obp = avgobp
        else:
            self.avg_obp = AvgObp.avg
        self.min_ab_year = min_ab_year
        self.min_ip_year = min_ip_year
        self.team_career_ip = team_career_ip
        if type_distribution == None:
            if self.type == LeagueType.decades:
                batter_decades = {
                    Decades.dec_1870s: (0, 1),
                    Decades.dec_1880s: (0, 1),
                    Decades.dec_1890s: (0, 1),
                    Decades.dec_1900s: (0, 1),
                    Decades.dec_1910s: (0, 1),
                    Decades.dec_1920s: (0, 1),
                    Decades.dec_1930s: (0, 1),
                    Decades.dec_1940s: (0, 1),
                    Decades.dec_1950s: (0, 1),
                    Decades.dec_1960s: (0, 1),
                    Decades.dec_1970s: (0, 1),
                    Decades.dec_1980s: (0, 1),
                    Decades.dec_1990s: (0, 1),
                    Decades.dec_2000s: (0, 1),
                    Decades.dec_2010s: (0, 1)
                }
                pitcher_decades = {
                    Decades.dec_70_90: (0, 1),
                    Decades.dec_1890s: (0, 1),
                    Decades.dec_1900s: (0, 1),
                    Decades.dec_1910s: (0, 1),
                    Decades.dec_1920s: (0, 1),
                    Decades.dec_1930s: (0, 1),
                    Decades.dec_1940s: (0, 1),
                    Decades.dec_1950s: (0, 1),
                    Decades.dec_1960s: (0, 1),
                    Decades.dec_1970s: (0, 1),
                    Decades.dec_1980s: (0, 1),
                    Decades.dec_1990s: (0, 1),
                    Decades.dec_2000s: (0, 1),
                    Decades.dec_2010s: (0, 1)
                }
                self.type_distribution = {
                    Batter: batter_decades,
                    Pitcher: pitcher_decades
                }
        else:
            self.type_distribution = type_distribution

