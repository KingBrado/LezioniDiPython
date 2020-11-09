from base_di_dati import leggi_base_di_dati, salva_base_di_dati
from gestore_eventi import gestisci_eventi

def main():
    base_di_dati = leggi_base_di_dati()

    gestisci_eventi(base_di_dati)

    salva_base_di_dati(base_di_dati)

if __name__ == '__main__':
    main()