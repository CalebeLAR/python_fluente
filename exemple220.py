# Exemplo 2.20 - Criando, salvando e carregando um array grande de números de ponto flutuante
from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
print(floats2)

fp = open('floats.bin','rb')
floats2.fromfile(fp, 10**7)
fp.close()

print(floats[-1])
print(floats2 == floats)
