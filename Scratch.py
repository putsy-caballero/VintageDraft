from entities.Batter import Batter
from entities.entity_enums import Decades
from entities.Utilities import Utilities
from test.entities.TestSampleEntities import *

a = ("foo", 3)
a.append("bar")
print(a)

#
# l = [None, 3]
# l.sort()
# print(l)
#
# settings = TestSampleEntities.get_league_settings()
# print(settings.avg_obp.value)
#
# print (TestSampleEntities.get_user())
#
# p = TestSampleEntities.get_putsy()
# print (Utilities.get_decade(p, 1947))
#
# r = TestSampleEntities.get_slim()
# print (Utilities.get_decade(r, 1922))
# p = { Decades.dec_70_90: (0, 1)}
# print (p[Decades.dec_70_90][1])
#
# b = {}
# b["a"] = b.get("a", 0) + 10
# b["b"] = None
# print (b)
#
# q = {
#     "d": {
#         "c": 4
#     }
# }
#
# print(q)
#
# j = [b, q]
# print(j)