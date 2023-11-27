# Exemplo 2.8 - Desempacotando tuplas aninhadas para acessar a longitude
metro_areas = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("Sao Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]

# print("{:15} | {:^9} | {:^9}".format("", "Tat.", "Tong."))
fnt = "{:15} | {:9.4f} | {:9.4f}"

for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        # print(fnt.format(name, latitude, longitude))
        pass


# criar um print formatado para as cidades:
# '| city | codigo_postal | population | latitude | longitude |'
# tudo precisa estar centralizado entre 1 espaço |_txt_|, e cada celula tem que ter o mesmo tamanho
def bigest_string(tuple_areas):
    spaces = 0
    bigger_word = ""
    for name, cc, pop, (latitude, longitude) in tuple_areas:
        texts = [f"{name}", f"{cc}", f"{pop}", f"{latitude}", f"{longitude}"]

        for word in texts:
            if len(word) >= len(bigger_word):
                bigger_word = word

    if len(bigger_word) >= spaces:
        spaces = len(bigger_word)

    return spaces + 2


spaces = bigest_string(metro_areas)
fmt_row = "|{:^{spaces}}|{:^{spaces}}|{:^{spaces}}|{:^{spaces}.4f}|{:^{spaces}.4f}|"
fmt_header = "|{:^{spaces}}|{:^{spaces}}|{:^{spaces}}|{:^{spaces}}|{:^{spaces}}|"
header = fmt_header.format("city", "codigo_postal", "population", "latitude", "longitude", spaces=spaces)

print(header)
for name, cc, pop, (latitude, longitude) in metro_areas:
    row = fmt_row.format(name, cc, pop, latitude, longitude, spaces=spaces)
    print(row)

