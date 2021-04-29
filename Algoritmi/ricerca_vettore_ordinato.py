from typing import List, Tuple, Optional

def ricerca_vettore_ordinato(valore: int, lista: List[int], length: int) -> bool:
    """
    Codice di seguito:
    Regole:
    - Niente if ... in lista
    - Niente while
    """
    if length == 1:
        return valore == lista[0]
    elemento_medio = length // 2
    if valore < lista[elemento_medio]:
        return ricerca_vettore_ordinato(valore, lista[:elemento_medio], elemento_medio)
    else:
        return ricerca_vettore_ordinato(valore, lista[elemento_medio:], length-elemento_medio)
    

def ricerca_vettore_con_indice(valore: int, lista: List[int]) -> Tuple[bool, Optional[int]]:
    for indice, elemento in enumerate(lista):
        if elemento == valore:
            return True, indice
    return False, None

if __name__ == '__main__':
    una_lista = [2, 3, 5, 7, 12, 19, 154, 1990]
    assert ricerca_vettore_ordinato(5, una_lista, len(una_lista)) == True, "Test 1 fallito"
    assert ricerca_vettore_ordinato(21, una_lista, len(una_lista)) == False, "Test 2 fallito"