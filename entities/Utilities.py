from entities.entity_enums import Decades
from entities.Pitcher import Pitcher
from entities.Player import Player
from typing import Type


class Utilities(object):
    @staticmethod
    def get_decade(player: Type(Player), year: int):
        decade = None
        for member in list(Decades):
            if member.value[0] <= year and member.value[1] >= year:
                decade = member
        if isinstance(player, Pitcher) and (decade == Decades.dec_1870s or decade == Decades.dec_1880s):
            decade = Decades.dec_70_90
        return decade
