from entities.entity_enums import Decades, Positions
from typing import Type

class Error(Exception):
    pass

class InvalidPositionError(Error):
    def __init__(self, message, position: Positions):
        self.message = message
        self.position = position

class InvalidYearError(Error):
    def __init__(self, message, year: int):
        self.message = message
        self.year = year

class PositionFullError(Error):
    def __init__(self, message, position: Positions):
        self.message = message
        self.position = position

class DecadeFullError(Error):
    def __init__(self, message, decade: Type(Decades)):
        self.message = message
        self.decade = decade