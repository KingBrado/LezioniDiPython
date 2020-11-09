import json
import datetime

with open('database.json', 'r') as stream:
    base_di_dati = json.load(stream)


while(True):
    
    messaggio = 'Scegli una delle seguenti opzioni:\n'
    messaggio += '-Per nuova iscrizione premi N\n'
    messaggio += "-Per stampare lo stato dell'iscritto premi S\n"
    messaggio += '-Per restituzione premi R\n'
    messaggio += '-Per prestito premi P\n'
    messaggio += "-Per cancellare una iscrizione premi C\n"
    messaggio += "-Per uscire premi U\n"

    scelta = input(messaggio)

    if scelta.upper() == 'N':
        nome = input('Inserisci il nome completo e premi Invio\n')
        cognome = input('Inserisci il cognome completo e premi Invio\n')
        while True:
            data_di_nascita = input('Inserisci la data di nascita nel formato DD/MM/YYYY\n')
            try:
                data_di_nascita = datetime.datetime.strptime(data_di_nascita, '%d/%m/%Y')
                break
            except ValueError:
                print('Formato invalido!!!')
        
        base_di_dati.append({'Nome': nome, 
                             'Cognome': cognome, 
                             'Data Di Nascita': data_di_nascita, 
                             'Libri': []})
    elif scelta.upper() == 'S':
        nome = input('Inserisci il nome della persona da cercare\n')
        for persona in base_di_dati:
            if persona['Nome'].lower() == nome.lower():
                print(persona)
                break
        else:
            print('Persona non trovata')

    elif scelta.upper() == 'P':
        nome = input('Inserisci il nome della persona che richiede il prestito\n')
        for persona in base_di_dati:
            if persona['Nome'].lower() == nome.lower():
                if len(persona['Libri']) >= 5:
                    print('Questa persona ha raggiunto il numero massimo di libri '
                          'che può prendere in prestito')
                else:
                    nome_libro = input('Inserisci il nome del libro\n')
                    persona['Libri'].append(nome_libro)
                break
        else:
            print('Persona non trovata')
    elif scelta.upper() == 'R':
        nome = input('Inserisci il nome della persona che restituisce il libro\n')
        for persona in base_di_dati:
            if persona['Nome'].lower() == nome.lower():
                stringa_libri = '\n'.join(f'{idx+1} - {libro}' for idx, libro in enumerate(persona['Libri']))
                while True:
                    scelta_libro = input(f'{nome} ha in prestito i seguenti libri:\n{stringa_libri}\n'
                                        f'Quale resituisce (scegli un numero)?\n')
                    try:
                        scelta_libro = int(scelta_libro) - 1
                        if scelta_libro >= len(persona['Libri']):
                            raise ValueError
                        del persona['Libri'][scelta_libro]
                        break
                    except ValueError:
                        print('Scelta non valida!')
                break
        else:
            print('Persona non trovata')
    elif scelta.upper() == 'C':
        nome = input('Inserisci il nome della persona da cancellare\n')
        for idx, persona in enumerate(base_di_dati):
            if persona['Nome'].lower() == nome.lower():
                del base_di_dati[idx]
                break
        else:
            print('Persona non trovata')
    elif scelta.upper() == 'U':
        break
    else:
        print('Opzione Invalida, ritenta')

with open('database.json', 'w') as stream:
    json.dump(base_di_dati, stream, indent=4)