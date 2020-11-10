from datetime import date

class Persona:

    def __init__(self, name, surname, birth_date):
        self.nome = name
        self.cognome = surname
        self.data_di_nascita = birth_date
        self.libri = []

    def eta(self):
        return date.today() - self.data_di_nascita

    def aggiungi_libro(self, libro):
        if len(self.libri) >= 5:
            print('La persona ha raggiunto il limite libri')
            return
        self.libri.append(libro)

class Libro:
    nome = 'Il viaggio del mondo in 80 giorni'

x = Persona('Berardo', 'Manzi', date(1987, 5, 10))
print(x.eta())

y = Persona('Davide', 'D\'Intino', date(1990, 10, 12))

print(y.nome)
print(x.nome)

y.aggiungi_libro('Il Signore degli Anelli - versione estesa')
y.aggiungi_libro('Il Signore degli Anelli - versione estesa')
y.aggiungi_libro('Il Signore degli Anelli - versione estesa')
y.aggiungi_libro('Il Signore degli Anelli - versione estesa')
y.aggiungi_libro('Il Signore degli Anelli - versione estesa')
y.aggiungi_libro('Il Signore degli Anelli - versione estesa')

print(y.libri)
# print(dir(Persona))
# print(dir(Libro))
# print(dir(5))

s = 'Davide'

print(s.upper())