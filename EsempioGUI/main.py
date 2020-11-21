import tkinter as tk
from Grafico import Grafico
from Punto import Punto

window = tk.Tk()

g = Grafico(window)
g.draw()

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.minsize(width=g.width()+g.padx(), height=g.height()+g.pady())
window.mainloop()   