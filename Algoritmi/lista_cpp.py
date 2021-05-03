from typing import Any
class ElementoLista:

    def __init__(self, valore: Any):
        self.valore = valore
        self.prossimo_elemento = None


class Lista:
    def __init__(self):
        self.primo_elemento = None

    def aggiungi_elemento(self, elemento):
        if self.primo_elemento is None:
            self.primo_elemento = elemento
            return
        elemento_corrente = self.primo_elemento
        while elemento_corrente.prossimo_elemento is not None:
            elemento_corrente = elemento_corrente.prossimo_elemento
        elemento_corrente.prossimo_elemento = elemento

    def __repr__(self):
        elemento = self.primo_elemento
        elementi = []
        while elemento is not None:
            elementi.append(str(elemento.valore))
            elemento = elemento.prossimo_elemento
        elementi.append("None")
        return " -> ".join(elementi)

lista = Lista()
elemento_lista = ElementoLista(10)
lista.aggiungi_elemento(elemento_lista)
elemento_lista = ElementoLista(12)
lista.aggiungi_elemento(elemento_lista)
print(lista.primo_elemento.valore)
print(lista.primo_elemento.prossimo_elemento.valore)
print(lista)