from typing import List     

def ricerca_vettore(valore: int, lista: List[int]) -> List[int]:
    """
    Codice di seguito:
    Regole:
    - Niente if ... in lista
    - Niente while
    """
    trovato = False
    return trovato


if __name__ == '__main__':
    una_lista = [1, 3, 5, 4, 5]
    assert ricerca_vettore(5, una_lista) == True, "Test 1 fallito"
    assert ricerca_vettore(19, una_lista) == False, "Test 2 fallito"