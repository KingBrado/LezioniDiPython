import matplotlib.pyplot as plt


def disegna(x, y):
    plt.plot(x, y, 'o-', markersize=10)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()