from enum import Enum

class LeagueType(Enum):
    decades = 1


# last_names = 2
#    teams = 3

class ScoringType(Enum):
    additive = 1
    multiplicative = 2


class Positions(Enum):
    catcher = 1
    first_base = 2
    second_base = 3
    third_base = 4
    shortstop = 5
    corner_infield = 6
    middle_infield = 7
    infield = 8
    left_field = 9
    center_field = 10
    right_field = 11
    outfield = 12
    pitcher = 13
    hitter_utility = 14


class AvgObp(Enum):
    avg = "AVG"
    obp = "OBP"


class Decades(Enum):
    dec_70_90 = 1870, 1889,
    dec_1870s = 1870, 1879,
    dec_1880s = 1880, 1889,
    dec_1890s = 1890, 1899,
    dec_1900s = 1900, 1909,
    dec_1910s = 1910, 1919,
    dec_1920s = 1920, 1929,
    dec_1930s = 1930, 1939,
    dec_1940s = 1940, 1949,
    dec_1950s = 1950, 1959,
    dec_1960s = 1960, 1969,
    dec_1970s = 1970, 1979,
    dec_1980s = 1980, 1989,
    dec_1990s = 1990, 1999,
    dec_2000s = 2000, 2009,
    dec_2010s = 2010, 2019

class Categories(Enum):
    a = 1