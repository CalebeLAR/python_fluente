# Exemplo 2.14 - Uma charada
import dis


t = (1, 2, [30, 40])
print(t)

t[2] += [50, 60]
print(t)

dis.dis()
