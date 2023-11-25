# Exemplo 2.5 -Inicializando uma tupla e um array a partir de uma expressão geradora
import array

symbols = '$¢£¥€¤'

tup = tuple(ord(symbol) for symbol in symbols)
print(tup)

arr = array.array('I', (ord(symbol) for symbol in symbols))
print(arr)