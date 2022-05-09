import tkinter as tk


class window ():
    def __init__(self):
        self.window = tk.Tk() #Creamos la ventana
        self.window.title('La cena de los filósofos')

        self.texto = tk.Text(self.window, height=30, width = 80) #texto donde va a ir los filósofos pensando
        self.scroll = tk.Scrollbar(self.window) #establecemos que nuestra ventana va a tener una barra deslizante
        self.texto.configure(yscrollcommand = self.scroll.set) #configuramos netsra barra deslizante dentro de nuetro texto
        self.texto.pack()
        self.scroll.config (command= self.texto.yview)
        self.scroll.pack(side = tk.RIGHT, fill=tk.Y)