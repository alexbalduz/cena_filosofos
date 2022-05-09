import tkinter as tk


class window ():
    def __init__(self):
        self.window = tk.Tk() #Creamos la ventana
        self.window.title('La cena de los filósofos')
        self.window.geometry("745x650")

        #create a button to start the game with grid
        self.start_button = tk.Button(self.window, text="Iniciar", command=self.run)
        #align the button to the bottom of the window
        self.start_button.place(relx=0.3, rely=0.95, anchor=tk.CENTER)
        #create a button to pause the game
        self.pause_button = tk.Button(self.window, text="Pausar", command=self.quit)
        #align the button to the bottom of the window
        self.pause_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
        #create a button to reset the game
        self.reset_button = tk.Button(self.window, text="Reset", command=self.quit)
        #align the button to the bottom of the window
        self.reset_button.place(relx=0.7, rely=0.95, anchor=tk.CENTER)
        #create a button to quit the game
        self.quit_button = tk.Button(self.window, text="Quit", command=self.quit)
        #align the button to the bottom of the window
        self.quit_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
        #create a button of the credits
        self.credits_button = tk.Button(self.window, text="Créditos", command=self.quit)
        #align the button to the bottom of the window
        self.credits_button.place(relx=0.9, rely=0.95, anchor=tk.CENTER)

        self.checkbutton_var = tk.IntVar()
        #create a checkbutton with a ticked state
        self.checkbutton = tk.Checkbutton(self.window, text="Crear un log", variable = self.checkbutton_var)
        #align the button to the bottom of the window
        self.checkbutton.place(relx=0.1, rely=0.95, anchor=tk.CENTER)




        self.texto = tk.Text(self.window, height=30, width = 80) #texto donde va a ir los filósofos pensando
        self.scroll = tk.Scrollbar(self.window) #establecemos que nuestra ventana va a tener una barra deslizante
        self.texto.configure(yscrollcommand = self.scroll.set) #configuramos netsra barra deslizante dentro de nuetro texto
        self.texto.pack()
        self.scroll.config (command= self.texto.yview)
        self.scroll.pack(side = tk.RIGHT, fill=tk.Y)


    def imprimir(self, texto):
        self.texto.insert(tk.END, str(texto) + '\n')

    def quit(self):
        self.window.withdraw()

    def run(self):
        self.window.mainloop()
