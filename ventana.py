import tkinter as tk
from tkinter import SUNKEN
import tkinter.ttk as ttk
import sys
class window ():
    def __init__(self):
        self.window = tk.Tk() #Creamos la ventana
        self.window.title('La cena de los filósofos')
        self.window.geometry("745x650")

        #create a button to start the game
        self.start_button = ttk.Button(self.window, text="Iniciar", command=self.run)
        #align the button to the bottom of the window
        self.start_button.place(relx=0.3, rely=0.95, anchor=tk.CENTER)
        #create a button to pause the game
        self.pause_button = ttk.Button(self.window, text="Pausar", command=self.quit)
        #align the button to the bottom of the window
        self.pause_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
        #create a button to reset the game
        self.reset_button = ttk.Button(self.window, text="Reset", command=self.quit)
        #align the button to the bottom of the window
        self.reset_button.place(relx=0.7, rely=0.95, anchor=tk.CENTER)
        #create a button to quit the game
        self.quit_button = ttk.Button(self.window, text="Quit", command=self.quit)
        #align the button to the bottom of the window
        self.quit_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)
        #create a button of the credits
        self.credits_button = ttk.Button(self.window, text="Créditos", command=self.quit)
        #align the button to the bottom of the window
        self.credits_button.place(relx=0.9, rely=0.95, anchor=tk.CENTER)

        self.checkbutton_var = tk.IntVar()
        #create a checkbutton with a ticked state
        self.checkbutton = ttk.Checkbutton(self.window, text="Crear un log", variable = self.checkbutton_var)
        #align the button to the bottom of the window
        self.checkbutton.place(relx=0.1, rely=0.95, anchor=tk.CENTER)

        #create a frame to hold the buttons
        self.frame = ttk.Frame(self.window,relief=SUNKEN,borderwidth=5)
        self.frame.grid(column=0,row=2,columnspan=4,sticky=('N','S','E','W'))
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)

        #create a frame on the first row that is 300 pixels wide and 400 pixels high
        self.frame1=ttk.Frame(self.window,width=500,height=260,relief=SUNKEN,borderwidth=5)
        self.frame1.grid(column=0,row=0,sticky=('N','S','E','W'))

        #create another frame on the second row that is 400 pixels wide and 360 pixels high
        self.frame2=ttk.Frame(self.window,width=500,height=260,relief=SUNKEN,borderwidth=5)
        self.frame2.grid(column=0,row=1,sticky=('N','S','E','W'))

        #create a frame on the second column and the first row that is 100 pixels wide and 260 pixels high
        self.frame3=ttk.Frame(self.window,width=300,height=260,relief=SUNKEN,borderwidth=5)
        self.frame3.grid(column=1,row=0,sticky=('N','S','E','W'))
        self.frame4=ttk.Frame(self.window,width=300,height=260,relief=SUNKEN,borderwidth=5)
        self.frame4.grid(column=1,row=1,sticky=('N','S','E','W'))

        #add a text on the frame on the first row and second column
        self.text0 = ttk.Label(self.frame3, text="Código de colores:",font=("Arial", 17, "bold"))
        self.text0.grid(column=0,row=0,sticky=('N','S','E','W'))

        self.text1=ttk.Label(self.frame3,text="Filósofo entra a comer",font=("Arial",15))
        self.text1.grid(column=0,row=2,sticky=('N','S','E','W'), padx = 20, pady = 10)
        self.color1 = tk.Label(self.frame3, background="pink", height = 1, width = 1)
        self.color1.place(relx=0.05, rely=0.17, anchor=tk.CENTER)
        self.color1.config(state="disable")

        self.text2=ttk.Label(self.frame3,text="Filosofo tiene un tenedor",font=("Arial",15))
        self.text2.grid(column=0,row=3,sticky=('N','S','E','W'), padx = 20, pady = 10)
        self.color2 = tk.Label(self.frame3, background="orange", height = 1, width = 1)
        self.color2.place(relx=0.05, rely=0.32, anchor=tk.CENTER)
        self.color2.config(state="disable")

        self.text3=ttk.Label(self.frame3,text="Filósofo esta comiendo",font=("Arial",15))
        self.text3.grid(column=0,row=4,sticky=('N','S','E','W'), padx = 20, pady = 10)
        self.color3 = tk.Label(self.frame3, background="blue", height = 1, width = 1)
        self.color3.place(relx=0.05, rely=0.48, anchor=tk.CENTER)
        self.color3.config(state="disable")

        self.text4=ttk.Label(self.frame3,text="Filósofo esta pensando",font=("Arial",15))
        self.text4.grid(column=0,row=5,sticky=('N','S','E','W'), padx = 20, pady = 10)
        self.color4 = tk.Label(self.frame3, background="grey", height = 1, width = 1)
        self.color4.place(relx=0.05, rely=0.62, anchor=tk.CENTER)
        self.color4.config(state="disable")

        self.text5=ttk.Label(self.frame3,text="Tenedor ocupado",font=("Arial",15))
        self.text5.grid(column=0,row=6,sticky=('N','S','E','W'), padx = 20, pady = 10)
        self.color5 = tk.Label(self.frame3, background="red", height = 1, width = 1)
        self.color5.place(relx=0.05, rely=0.77, anchor=tk.CENTER)
        self.color5.config(state="disable")

        self.text6=ttk.Label(self.frame3,text="Tenedor libre",font=("Arial",15))
        self.text6.grid(column=0,row=7,sticky=('N','S','E','W'), padx = 20, pady = 10)
        self.color6 = tk.Label(self.frame3, background="white", height = 1, width = 1)
        self.color6.place(relx=0.05, rely=0.93, anchor=tk.CENTER)



        self.texto = tk.Text(self.frame2, height=20, width=67) #texto donde va a ir los filósofos pensando
        self.scroll = tk.Scrollbar(self.frame2) #establecemos que nuestra ventana va a tener una barra deslizante
        self.texto.configure(yscrollcommand = self.scroll.set) #configuramos nuestra barra deslizante dentro de nuetro texto
        self.texto.grid(row=0, column=0, sticky='nsew')
        self.scroll.config (command= self.texto.yview)
        self.scroll.grid(row=0, column=1, sticky='ns')


    def imprimir(self, texto):
        self.texto.insert(tk.END, str(texto) + '\n')

    def quit(self):
        self.window.withdraw()
        self.window.destroy()

    def run(self):
        self.window.mainloop()
