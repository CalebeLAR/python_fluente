# Exemplo 2.22 - Operações básicas com linhas e colunas em um numpy.ndarray

import numpy

a = numpy.arange(12)
print(a)

print(type(a))

print(a.shape)

a.shape = 3, 4
print(a)

print(a[2])
print(a[2, 1])
print(a[:, 1])

print(a.transpose())
