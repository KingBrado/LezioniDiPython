from typing import List

def popola_vettore(a: List):
    a.append(1)
    a.append(2)
    a.append(3)

v = []
popola_vettore(v)
print(v)

def somma(a, b):
    a = a + b
    return a


x = 1
y = 2
z = somma(x, y)
print(x)

c = 1
popola_vettore(c)
