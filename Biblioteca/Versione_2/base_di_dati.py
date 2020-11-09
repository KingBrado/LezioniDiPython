import json

def leggi_base_di_dati():
    with open('database.json', 'r') as stream:
        base_di_dati = json.load(stream)
    return base_di_dati

def salva_base_di_dati(base_di_dati):
    with open('database.json', 'w') as stream:
        json.dump(base_di_dati, stream, indent=4)