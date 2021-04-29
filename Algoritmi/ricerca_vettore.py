from typing import List, Tuple, Optional

def ricerca_vettore(valore: int, lista: List[int]) -> bool:
    """
    Codice di seguito:
    Regole:
    - Niente if ... in lista
    - Niente while
    """
    for elemento in lista:
        if elemento == valore:
            return True
    return False
    #     if elemento == valore:
    #         break
    # else:
    #     return False
    # return True

def ricerca_vettore_con_indice(valore: int, lista: List[int]) -> Tuple[bool, Optional[int]]:
    for indice, elemento in enumerate(lista):
        if elemento == valore:
            return True, indice
    return False, None

if __name__ == '__main__':
    una_lista = [1, 3, 5, 4, 5]
    assert ricerca_vettore(5, una_lista) == True, "Test 1 fallito"
    assert ricerca_vettore(19, una_lista) == False, "Test 2 fallito"