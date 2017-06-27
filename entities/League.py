from enum import Enum
from entities.LeagueSettings import LeagueSettings
from entities.Team import Team
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

