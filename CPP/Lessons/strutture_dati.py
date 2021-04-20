x = 5
y = x
y = y + 1
print(x)

lista = []
lista_2 = lista
lista_2.append(1)
print(lista)

lista_2 += [2]
print(lista)

lista_2 = [1, 3, 4]
print(lista)

a = 1
b = 2
print(id(a))
print(id(b))

lista_2 = lista[:]
lista_2.append(1)
print(lista)
print(lista_2)

lista_3 = lista_2.copy()
lista_3 += [2,3,4]
print(lista_2)
print(lista_3)

d = {}
d[5] = 10
print(d)

l = []
l[5] = 10
print(l)