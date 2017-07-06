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

    @staticmethod
    def assign_points(stats):
        group = []
        output = []
        value = len(stats)

        for i in range(0, len(stats)):
            if len(group) == 0 or group[0][1] == stats[i][1]:
                group.append(stats[i])
            else:
                for j in range(0, len(group)):
                    output.append((group[j], value - .5 * (len(group) - 1)))
                value -= len(group)
                group = [stats[i]]

        for j in range(0, len(group)):
            output.append((group[j], value - .5 * (len(group) - 1)))

        return output

    def calculate_standings(self):
        standings = {"Overall": {k: 0 for k in self.teams}, Batter: {"Career": {"Overall": {k: 0 for k in self.teams}}, "BY": {"Overall": {k: 0 for k in self.teams}}, "Overall": {k: 0 for k in self.teams}}, Pitcher: {"Career": {"Overall": {k: 0 for k in self.teams}}, "BY": {"Overall": {k: 0 for k in self.teams}}, "Overall": {k: 0 for k in self.teams}}}
        batting_cats = self.league_settings.batting_categories
        pitching_cats = self.league_settings.pitching_categories
        for k in batting_cats:
            standings[Batter]["Career"][k] = []
            standings[Batter]["BY"][k] = []
        for k in pitching_cats:
            standings[Pitcher]["Career"][k] = []
            standings[Pitcher]["BY"][k] = []
        for team in self.teams:
            stats = team.generate_stats()
            for cat in batting_cats:
                standings[Batter]["Career"][cat].append((team, float(stats[Batter]["Career"][cat.value]) or 0))
                standings[Batter]["BY"][cat].append((team, float(stats[Batter]["BY"][cat.value]) or 0))
            for cat in pitching_cats:
                standings[Pitcher]["Career"][cat].append((team, float(stats[Pitcher]["Career"][cat.value]) or 0))
                standings[Pitcher]["BY"][cat].append((team, float(stats[Pitcher]["BY"][cat.value]) or 0))
        for cat in batting_cats:
            standings[Batter]["Career"][cat].sort(key=lambda entry: entry[1], reverse=True)
            standings[Batter]["Career"][cat] = self.assign_points(standings[Batter]["Career"][cat])
            for entry in standings[Batter]["Career"][cat]:
                standings[Batter]["Career"]["Overall"][entry[0][0]] += entry[1]
                standings[Batter]["Overall"][entry[0][0]] += entry[1]
                standings["Overall"][entry[0][0]] += entry[1]
            standings[Batter]["BY"][cat].sort(key=lambda entry: entry[1], reverse=True)
            standings[Batter]["BY"][cat] = self.assign_points(standings[Batter]["BY"][cat])
            for entry in standings[Batter]["BY"][cat]:
                standings[Batter]["BY"]["Overall"][entry[0][0]] += entry[1]
                standings[Batter]["Overall"][entry[0][0]] += entry[1]
                standings["Overall"][entry[0][0]] += entry[1]
        for cat in pitching_cats:
            standings[Pitcher]["Career"][cat].sort(key=lambda entry: entry[1], reverse=cat not in ["ERA", "WHIP"])
            standings[Pitcher]["Career"][cat] = self.assign_points(standings[Pitcher]["Career"][cat])
            for entry in standings[Pitcher]["Career"][cat]:
                standings[Pitcher]["Career"]["Overall"][entry[0][0]] += entry[1]
                standings[Pitcher]["Overall"][entry[0][0]] += entry[1]
                standings["Overall"][entry[0][0]] += entry[1]
            standings[Pitcher]["BY"][cat].sort(key=lambda entry: entry[1], reverse=cat not in ["ERA", "WHIP"])
            standings[Pitcher]["BY"][cat] = self.assign_points(standings[Pitcher]["BY"][cat])
            for entry in standings[Pitcher]["BY"][cat]:
                standings[Pitcher]["BY"]["Overall"][entry[0][0]] += entry[1]
                standings[Pitcher]["Overall"][entry[0][0]] += entry[1]
                standings["Overall"][entry[0][0]] += entry[1]
        return standings










