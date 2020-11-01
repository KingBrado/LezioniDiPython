import random

def funzione_lineare(x):
    y = []
    # Calcoli qua
    return {'x': x, 'y': y}


def funzione_quadratica(x):
    y = []
    # Calcoli qua
    return {'x': x, 'y': y}


def rete_neurale(x, y, epoche=500, learning_rate=0.1, allena=True):
    a = random.random()
    b = random.random()

    # Allenamento
    if allena:
        for epoca in range(epoche):
            for in_val, out_val in zip(x, y):
                f = a * in_val + b
                a = a - learning_rate * 2 * (f - out_val) * in_val
                b = b - learning_rate * 2 * (f - out_val)

    return {'x': x, 'y': [a*val+b for val in x]}


if __name__ == '__main__':
    x, y = [1, 2, 3, 4], [5, 7, 9, 11]
    print(rete_neurale(x, y))
