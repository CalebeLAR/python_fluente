# Exemplo 23 - A mesma lista criada por uma listeomp e uma composição de map/filter
symbols = "$Ç£¥€n"
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
beyond_ascii

# O script 02-array-seq/listcomp_speed.py (http://bit.lyZl Vm6R3n) no repositório de
# código do livro Python fluente (https://github.com/fluentpython/example-code) é um teste
# simples de velocidade que compara a listcomp com filter/nap.

import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *("{:.3f}".format(x) for x in res))


clock("listcomp        :", "[ord(s) for s in symbols if ord(s) > 127]")
clock("listcomp + func :", "[ord(s) for s in symbols if non_ascii(ord(s))]")
clock("filter + lambda :", "list(filter(lambda c: c > 127, map(ord, symbols)))")
clock("filter + func   :", "list(filter(non_ascii, map(ord, symbols)))")
