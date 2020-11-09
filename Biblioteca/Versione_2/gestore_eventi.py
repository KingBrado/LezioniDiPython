import datetime

def inserisci_nuovo_registrato(base_di_dati):
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

def trova_persona(nome, base_di_dati):
    for idx, persona in enumerate(base_di_dati):
        if persona['Nome'].lower() == nome.lower():
            return idx, persona
    return -1, ''

def restituisci_libro(persona):
    if not persona['Libri']:
        print('Questa persona non ha libri in prestito')
        return
    stringa_libri = '\n'.join(f'{idx+1} - {libro}' for idx, libro in enumerate(persona['Libri']))
    while True:
        scelta_libro = input(f'{persona["Nome"]} ha in prestito i seguenti libri:\n{stringa_libri}\n'
                            f'Quale resituisce (scegli un numero)?\n')
        try:
            scelta_libro = int(scelta_libro) - 1
            if scelta_libro >= len(persona['Libri']):
                raise ValueError
            del persona['Libri'][scelta_libro]
            break
        except ValueError:
            print('Scelta non valida!')

def gestisci_scelta(scelta, base_di_dati):
    if scelta.upper() == 'N':
        inserisci_nuovo_registrato(base_di_dati)

    elif scelta.upper() == 'S':
        _, persona = trova_persona(input('Inserisci il nome della persona da cercare\n'), base_di_dati)
        if persona:
            print(persona)
        else:
            print('Persona non trovata')
    elif scelta.upper() == 'P':
        _, persona = trova_persona(input('Inserisci il nome della persona che richiede il prestito\n'), 
                                      base_di_dati)
        
        if persona:
            if len(persona['Libri']) >= 5:
                print('Questa persona ha raggiunto il numero massimo di libri '
                    'che può prendere in prestito')
            else:
                nome_libro = input('Inserisci il nome del libro\n')
                persona['Libri'].append(nome_libro)
        else:
            print('Persona non trovata')
    elif scelta.upper() == 'R':
        _, persona = trova_persona(input('Inserisci il nome della persona che restituisce il libro\n'), 
                                      base_di_dati)
        if persona:
            restituisci_libro(persona)
        else:
            print('Persona non trovata')
    elif scelta.upper() == 'C':
        idx, _ = trova_persona(input('Inserisci il nome della persona da cancellare\n'),
                                     base_di_dati)
        if idx != -1:
            del base_di_dati[idx]
        else:
            print('Persona non trovata')
    elif scelta.upper() == 'U':
        return False
    else:
        print('Opzione Invalida, ritenta')
    return True


def gestisci_eventi(base_di_dati):
    
        messaggio = 'Scegli una delle seguenti opzioni:\n'
        messaggio += '-Per nuova iscrizione premi N\n'
        messaggio += "-Per stampare lo stato dell'iscritto premi S\n"
        messaggio += '-Per restituzione premi R\n'
        messaggio += '-Per prestito premi P\n'
        messaggio += "-Per cancellare una iscrizione premi C\n"
        messaggio += "-Per uscire premi U\n"

        scelta = input(messaggio)
        while(gestisci_scelta(scelta, base_di_dati)):
            scelta = input('\n'+messaggio)
        