# Classe Persona, niente di nuovo
class Persona:

    def __init__(self, nome: str, eta: int):
        self.__nome = nome
        self.__eta = eta
        self.maggiorenne = eta >= 18

    def nome(self) -> str:
        return self.__nome

    def eta(self) -> int:
        return self.__eta
    

# Classe Impiegato eredita da Persona, per questo 'Persona' è tra parentesi
class Impiegato(Persona):

    def __init__(self, nome: str, eta: int, impiego: str):
        # Super chiama la classe al di sopra nell'albero genealogico delle classi (Persona in questo caso).
        # Passiamo gli argomenti al costruttore di Persoan.
        super().__init__(nome, eta)
        self.__impiego = impiego
        self.__salario = 0

    def impiego(self) -> str:
        return self.impiego

    def set_salario(self, salario: int):
        self.__salario = salario

    def salario(self) -> int:
        return self.__salario

# Altra classe che eredita da Persona.
class Studente(Persona):

    def __init__(self, nome: str, eta: int, corso_universitario: str):
        super().__init__(nome, eta)
        self.__corso_universitario = corso_universitario

    def corso_universitario(self) -> str:
        return self.__corso_universitario


if __name__ == '__main__':

    luigi = Impiegato('Luigi', 25, 'Astronauta')
    carla = Studente('Carla', 17, 'Filosofia della Fisica')


    print(luigi.nome()) # Nota: il metodo nome() non esiste nella definizione di Impiegato, ma viene ereditato da Persona
    print(luigi.salario()) # Metodo definito in Impiegato.

    print(f'Carla è maggiorenne: {carla.maggiorenne}') # L'attributo maggiorenne di Persona viene ereditato.

    # print(carla.__nome) # Gli attributi privati non vengono ereditati. Decommentare per vedere l'errore.

    # La funzione isinstance (parte della libreria standard di Python) permette di verificare se un oggetto
    # è un'istanza di una certa classe.

    print(f'5 è un intero: {isinstance(5, int)}') # 5 è un'istanza di intero (ricorda, in Python tutto è una classe)
    print(f'5.0 è un intero: {isinstance(5.0, int)}') # 5.0 è un float, non un intero
    print(f'Luigi è un impiegato: {isinstance(luigi, Impiegato)}') # Luigi ovviamente è un impiegato, lo abbiamo creato dalla classe.
    print(f'Luigi è una persona: {isinstance(luigi,Persona)}') # Luigi è anche una Persona, perché un Impiegato è una Persona.

    print(f'5 è un oggetto: {isinstance(5, object)}') # In Python esiste la madre di tutte le classi, chiamata object. Tutte le classi,
                                 # sia di Python che nostre ereditano da object.

    print(f'Luigi è un oggetto: {isinstance(luigi, object)}')
