from math import sqrt

class Punto:

    def __init__(self, x, y): # <- Qui stiamo dicendo "Un punto è costruito usando due coordinate."
        self.x = x
        self.y = y


class Segmento:

    def __init__(self, pa, pb): # <- Qui stiamo dicendo "Un segmento è costruito usando 2 punti."
        self.pa = pa
        self.pb = pb

    def lunghezza(self):
        return sqrt((self.pa.x-self.pb.x)**2+(self.pa.y-self.pb.y)**2)


pa = Punto(1, 2)
pb = Punto(0, 0)
s = Segmento(pa, pb) # Non c'è il problema dell'ordine

print(s.lunghezza())

# Va bene anche 

s = Segmento(Punto(1, 2), Punto(0, 0))

print(s.lunghezza())