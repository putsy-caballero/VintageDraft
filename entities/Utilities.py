from entities.Batter import Batter
from entities.entity_enums import Decades
from entities.Pitcher import Pitcher
from entities.Player import Player
from typing import Type

def get_decade(player: Type(Player)):
    decade = None
    for member in list(Decades):
        if member.value[0] <= player.year and member.value[1] >= player.year:
            decade = member
    if isinstance(player, Pitcher) and (decade == Decades.dec_1870s or decade == Decades.dec_1880s):
        decade = Decades.dec_70_90
    return decade

print(Batter)
p = Batter("foo", "joe", "bar", 1947, None, None)
print (get_decade(p))
b = Pitcher("foo", "joe", "bar", 1887, None, None)
print (get_decade(b))