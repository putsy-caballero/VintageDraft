from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, playerID: str, firstname: str, lastname: str, stats):
        self.playerID = playerID
        self.firstname = firstname
        self.lastname = lastname
        self.stats = stats

    @abstractmethod
    def valid_year(self, year, league_settings):
        pass

    @abstractmethod
    def pos_qual_career(self, position, league_settings):
        pass

