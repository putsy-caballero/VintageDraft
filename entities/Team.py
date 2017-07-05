from entities import Errors
from entities.Batter import Batter
from entities.entity_enums import Decades, LeagueType, Positions
from entities.League import League
from entities.LeagueSettings import LeagueSettings
from entities.Player import Player
from entities.Pitcher import Pitcher
from entities.User import User
from entities.Utilities import Utilities
from typing import Type
import uuid


class Team(object):

    def __init__(self, league: Type(League), name: str, user: Type(User)):
        self.uuid = uuid.uuid4()
        self.league = league
        self.name = name
        self.user = user
        self.players = {Batter: {}, Pitcher: {}}
        self.players[Batter] = {key: [] for key in league.league_settings.positions}
        del self.players[Batter][Positions.pitcher]
        self.players[Pitcher] = {Positions.pitcher: []}

    def get_team_decades(self):
        decade_players = {Batter: {}, Pitcher: {}}
        decade_players[Batter] = {key: 0 for key in Decades}
        decade_players[Pitcher] = {key: 0 for key in Decades}
        for k in self.players:
            for k2 in self.players[k]:
                for player in self.players[k][k2]:
                    decade_players[k][Utilities.get_decade(player[0], player[1])] += 1
        return decade_players

    def add_player(self, player: Type(Player), position: Type(Positions), year: int):
        settings: LeagueSettings = self.league.league_settings
        if position not in settings.positions:
            raise Errors.InvalidPositionError("invalid position", position)
        if not player.valid_year(year, settings):
            raise Errors.InvalidYearError("invalid best year", year)
        if not player.pos_qual_career(position, settings):
            raise Errors.InvalidPositionError("not enough games at position", position)
        max_at_position = settings.positions[position][1]
        position_players = self.players[type(player)][position]
        if len(position_players) >= max_at_position:
            raise Errors.PositionFullError("position full", position)
        else:
            if settings.league_type == LeagueType.decades:
                decade_players = self.get_team_decades()
                decade = Utilities.get_decade(player, year)
                if decade_players[type(player)][decade] >= settings.type_distribution[type(player)][decade][1]:
                    raise Errors.DecadeFullError("decade full", decade)

            # TODO: add logic for names/teams
            self.players[type(player)][position].append((player, year))

    @staticmethod
    def calculate_obp(stats: dict):
        reached = stats["H"] + stats["BB"]
        pa = stats["AB"] + stats["BB"]
        if "HBP" in stats:
            reached += int(stats["HBP"] or 0)
            pa += int(stats["HBP"] or 0)
        if "SF" in stats:
            pa += int(stats["SF"] or 0)
        return reached / pa

    def generate_stats(self):
        overall_stats = {}
        overall_stats[Batter] = {}
        overall_stats[Batter]["BY"] = {}
        overall_stats[Batter]["Career"] = {}
        overall_stats[Pitcher] = {}
        overall_stats[Pitcher]["BY"] = {}
        overall_stats[Pitcher]["Career"] = {}

        batters = False
        for k in self.players[Batter]:
            for player in self.players[Batter][k]:
                batters = True
                for stat in player[0].stats.batting_career_stats:
                    overall_stats[Batter]["Career"][stat] = overall_stats[Batter]["Career"].get(stat, 0) + int(player[0].stats.batting_career_stats[stat] or 0)
                    overall_stats[Batter]["BY"][stat] = overall_stats[Batter]["BY"].get(stat, 0) + int(player[0].stats.batting_year_stats[player[1]][stat] or 0)
        if batters:
            overall_stats[Batter]["Career"]["AVG"] = overall_stats[Batter]["Career"]["H"] / overall_stats[Batter]["Career"]["AB"]
            overall_stats[Batter]["Career"]["OBP"] = Team.calculate_obp(overall_stats[Batter]["Career"])
            overall_stats[Batter]["BY"]["AVG"] = overall_stats[Batter]["BY"]["H"] / overall_stats[Batter]["BY"]["AB"]
            overall_stats[Batter]["BY"]["OBP"] = Team.calculate_obp(overall_stats[Batter]["BY"])

        pitchers = False
        for k in self.players[Pitcher]:
            for player in self.players[Pitcher][k]:
                pitchers = True
                for stat in player[0].stats.pitching_career_stats:
                    overall_stats[Pitcher]["Career"][stat] = overall_stats[Pitcher]["Career"].get(stat, 0) + int(player[0].stats.pitching_career_stats[stat] or 0)
                    overall_stats[Pitcher]["BY"][stat] = overall_stats[Pitcher]["BY"].get(stat, 0) + int(player[0].stats.pitching_year_stats[player[1]][stat] or 0)
        if pitchers:
            overall_stats[Pitcher]["Career"]["ERA"] = overall_stats[Pitcher]["Career"]["ER"] * 27 / overall_stats[Pitcher]["Career"]["IPOuts"]
            overall_stats[Pitcher]["Career"]["WHIP"] = 3 * (overall_stats[Pitcher]["Career"]["H"] + overall_stats[Pitcher]["Career"]["BB"]) / overall_stats[Pitcher]["Career"]["IPOuts"]
            overall_stats[Pitcher]["BY"]["ERA"] = overall_stats[Pitcher]["BY"]["ER"] * 27 / overall_stats[Pitcher]["BY"]["IPOuts"]
            overall_stats[Pitcher]["BY"]["WHIP"] = 3 * (overall_stats[Pitcher]["BY"]["H"] + overall_stats[Pitcher]["BY"]["BB"]) / overall_stats[Pitcher]["BY"]["IPOuts"]

        return overall_stats






