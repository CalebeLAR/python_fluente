from collections import namedtuple
from exemple29 import City

# Exemplo 2.10 - Atributos e métodos de uma tupla nomeada (continuação do exemplo anterior)
print(City._fields)

LatLong = namedtuple("LatLong", "Lat long")

delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(28.613889, 77.208889))

delhi = City._make(delhi_data)
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ":", value)
