from tkinter import Canvas, FIRST, LAST, N, W, E, S, Label
from tkinter.constants import CENTER

from Punto import Punto

class Grafico:
    """
    Classe Grafico, wrapper di tkinter.Canvas, che serve a creare grafici su piano cartesiano.
    La classe richiede una istanza di tkinter.Tk().
    Esempio:
        window = tk.Tk()
        g = Grafico(window)
        g.draw()

        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        window.minsize(width=g.width()+g.padx(), height=g.height()+g.pady())
        window.mainloop()

    Questo esempio aprirà una finestra con un grafico vuoto e un piano cartesiano.
    :param parent: Widget genitore (Tk nel esempio).
    :param width: Larghezza del Grafico (in pixel).
    :param height: Altezza del Grafico (in pixel).
    :param padx: Padding orizzontale.
    :param pady: Padding verticale.
    """
    def __init__(self, parent, width=800, height=600, padx=10, pady=10):
        self.__width = width
        self.__height = height
        self.__padx = padx
        self.__pady = pady
        self.__origin = Punto(width/2, height/2)
        self.__canvas = Canvas(parent, width=width, height=height, background='gray90')

    
    def __create_axis(self):
        self.__canvas.create_line(0, self.__origin.y(), self.__width, self.__origin.y(), 
                                  arrow=LAST, dash=(5, ))
        self.__canvas.create_line(self.__origin.x(), 0, self.__origin.x(), self.__height, 
                                  arrow=FIRST, dash=(5, ))
        self.__x_label = Label(self.__canvas, text='x', bg='gray90')
        self.__y_label = Label(self.__canvas, text='y', bg='gray90')


    def draw(self):
        """
        Questo metodo crea un grafico vuoto, con solo gli assi cartesiani.
        """
        self.__create_axis()
        self.__canvas.grid(column=0, row=0, 
                           sticky=(N, W, E, S), padx=self.__padx, pady=self.__pady)
        self.__x_label.place(x=self.width()-10, y=self.__origin.y()-15, anchor=CENTER)
        self.__y_label.place(x=self.__origin.x()-15, y=10, anchor=CENTER)


    def draw_punti(self, punti):
        """
        Questo metodo crea un grafico con punti presi da una lista di Punti.
        :param punti: Lista di oggetti di tipo Punto.
        """
        for idx, punto in enumerate(punti):
            coordinates = Punto(self.__origin.x() + punto.x(), self.__origin.y() - punto.y())
            self.__canvas.create_oval(coordinates.x()-2, coordinates.y()-2, 
                                      coordinates.x()+2, coordinates.y()+2, 
                                      fill='black')
            self.__canvas.create_text(coordinates.x()+5, coordinates.y(), text=f'P{idx+1}', anchor=W)
        self.draw()

    def draw_vettori(self, vettori):
        """
        Questo metodo crea un grafico con vettori presi da una lista di Punti.
        :param punti: Lista di oggetti di tipo Punto.
        """
        for idx, vettore in enumerate(vettori):
            coordinates = Punto(self.__origin.x() + vettore.x(), self.__origin.y() - vettore.y())
            self.__canvas.create_line(self.__origin.x(), self.__origin.y(), 
                                      coordinates.x(), coordinates.y(),
                                      arrow=LAST)
            self.__canvas.create_text(coordinates.x()+5, coordinates.y(), text=f'V{idx+1}', anchor=W)
        self.draw()

    def width(self):
        """
        Larghezza del Grafico.
        :return: Larghezza del grafico.
        """
        return self.__width

    def height(self):
        """
        Altezza del Grafico.
        :return: Altezza del grafico.
        """
        return self.__height

    def padx(self):
        """
        Padding orizzontale del Grafico.
        :return: Padding orizzontale del Grafico.
        """
        return self.__padx

    def pady(self):
        """
        Padding verticale del Grafico.
        :return: Padding verticale del Grafico.
        """
        return self.__pady