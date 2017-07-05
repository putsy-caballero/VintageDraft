from enum import Enum
from entities.Batter import Batter
from entities.LeagueSettings import LeagueSettings
from entities.Pitcher import Pitcher
from typing import Type
import uuid


class Status(Enum):
    setup = 1
    drafting = 2
    paused = 3
    complete = 4

class League(object):

    def __init__(self, name: str, settings: Type(LeagueSettings), timeout: int):
        self.uuid = uuid.uuid4()
        self.name = name
        self.league_settings = settings
        self.timeout = timeout
        self.teams = []
        self.status = Status.setup

    def calculate_standings(self):
        standings = {Batter: {"Career": {}, "BY": {}}, Pitcher: {"Career": {}, "BY": {}}}
        batting_cats = [self.league_settings.avg_obp.value, "HR", "RBI", "R", "SB"]
        pitching_cats = ["ERA", "WHIP", "W", "SO", "SV"]
        for k in batting_cats:
            standings[Batter]["Career"][k] = []
            standings[Batter]["BY"][k] = []
        for k in pitching_cats:
            standings[Pitcher]["Career"][k] = []
            standings[Pitcher]["BY"][k] = []
        for team in self.teams:
            stats = team.generate_stats()
            for cat in batting_cats:
                standings[Batter]["Career"][cat].append((team, float(stats[Batter]["Career"][cat]) or 0))
                standings[Batter]["BY"][cat].append((team, float(stats[Batter]["BY"][cat]) or 0))
            for cat in pitching_cats:
                standings[Pitcher]["Career"][cat].append((team, float(stats[Pitcher]["Career"][cat]) or 0))
                standings[Pitcher]["BY"][cat].append((team, float(stats[Pitcher]["BY"][cat]) or 0))
        for cat in batting_cats:
            standings[Batter]["Career"][cat].sort(key=lambda entry: entry[1], reverse=True)
            standings[Batter]["BY"][cat].sort(key=lambda entry: entry[1], reverse=True)
        for cat in pitching_cats:
            standings[Pitcher]["Career"][cat].sort(key=lambda entry: entry[1], reverse=cat not in ["ERA", "WHIP"])
            standings[Pitcher]["BY"][cat].sort(key=lambda entry: entry[1], reverse=cat not in ["ERA", "WHIP"])

