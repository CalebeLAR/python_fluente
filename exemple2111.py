# Atribuição de valores a fatias
l = list(range(10))

l[2:5] = [20, 30]

print(l)
del l[5:7]
print(l)

l[3::2] = [11, 22]
print(l)

l[2:5] = [100]
print(l)


my_list = [[]] * 3
print(my_list)
my_list[1].append("A")
print(my_list)


print(id(my_list[1]))
print(id(my_list[0]))
print(id(my_list[2]))
