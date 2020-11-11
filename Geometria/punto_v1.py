from math import sqrt

class Punto:

    def __init__(self, x, y): # <- Qui stiamo dicendo "Un punto è costruito usando due coordinate."
        self.x = x
        self.y = y


class Segmento:

    def __init__(self, xa, xb, ya, yb): # <- Qui stiamo dicendo "Un segmento è costruito usando 4 coordinate."
        self.xa = xa
        self.xb = xb
        self.ya = ya
        self.yb = yb

    def lunghezza(self):
        return sqrt((self.xa-self.xb)**2+(self.ya-self.yb)**2)


p = Punto(1, 2)

s = Segmento(0, 1, 0, 2) # Qui l'ordine è (xa, ya, xb, yb) o (xa, xb, ya, yb)?

print(s.lunghezza())

