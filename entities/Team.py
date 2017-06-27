from entities import Errors
from entities.Batter import Batter
from entities.entity_enums import Decades, LeagueType, Positions
from entities.League import League
from entities.LeagueSettings import LeagueSettings
from entities.Player import Player
from entities.Pitcher import Pitcher
from entities.User import User
from entities.Utilities import get_decade
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
        for k, v in self.players:
            for k2, v2 in v:
                decade_players[k][get_decade(v)] += 1
        return decade_players

    def add_player(self, position: Type(Positions), player: Type(Player), year: int):
        settings = self.league.league_settings
        if position not in settings.positions:
            raise Errors.InvalidPositionError("invalid position: " + position)
        max_at_position = settings.positions[position][1]
        position_players = self.players[type(player)][position]
        if len(position_players) >= max_at_position:
            raise Errors.PositionFullError("Position full", position)
        else:
            if settings.league_type == LeagueType.decades:
                decade_players = self.get_team_decades()
                decade = get_decade(player, year)
                if decade_players[type(player)][decade] >= settings.type_distribution[type(player)][decade][1]:
                    raise Errors.DecadeFullError("Decade full", decade)

            # TODO: add logic for names/teams
            self.players[position].append(player)




