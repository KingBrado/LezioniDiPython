from math import sqrt

#!!! Concetto nuovo

class Punto:

    def __init__(self, x, y): # <- Qui stiamo dicendo "Un punto è costruito usando due coordinate."
        self.x = x
        self.y = y

    def __sub__(self, altro): # <- __sub__ è un metodo speciale che permette di ridefinire il simbolo -
        return Punto(self.x-altro.x, self.y-altro.y)


class Segmento:

    def __init__(self, pa, pb): # <- Qui stiamo dicendo "Un segmento è costruito usando 2 punti."
        self.pa = pa
        self.pb = pb

    def lunghezza(self):
        differenza = self.pb - self.pa
        return sqrt(differenza.x**2+differenza.y**2)


pa = Punto(1, 2)
pb = Punto(0, 0)

# Ora è lecito fare pb - pa
print(pb-pa)
s = Segmento(pa, pb) # Non c'è il problema dell'ordine

print(s.lunghezza())

# Va bene anche 

s = Segmento(Punto(1, 2), Punto(0, 0))

print(s.lunghezza())