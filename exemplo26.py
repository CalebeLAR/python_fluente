# Exemplo 2.6 - Produto cartesiano em uma expressão geradora
colors = ["black", "white"]
sizes = ["S", "M", "L"]
for tshirt in ("%s %s" % (c, s) for c in colors for s in sizes):
    print(tshirt)

names = ['moto', 'carro', 'caminhão']
comidas = ['prata', 'branco', 'preto']

for name in names:
    for comida in comidas:
        print("%s de cor %s" % (name, comida))
