import string
import bisect

letras = list(string.ascii_lowercase)
numeros = [n for n in range(len(letras))]
print(bisect.bisect(letras, "kk"))
print(bisect.bisect_left(letras, "kk"))
print(bisect.bisect_right(letras, "kk"))


print(letras)
print(numeros)




