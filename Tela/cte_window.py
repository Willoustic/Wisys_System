import tkinter as tk
from functions.tela import tela_na_resolução
from CTe_Auto.Auto.CTe_Config import Auto_CTe
import os
from functions.caminho import resource_path

class Cte_window():
    def __init__(self, master):
        self.master = master
        self.app = tk.Toplevel(master)
        self.configure_app()
        self.configure_tela()

        
    def configure_app(self):    
        self.app.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))
        self.app.title('CTe')
        self.app.geometry(tela_na_resolução(width=200, height=200))
        self.app.resizable(False, False)
        self.app.attributes('-topmost', True)


    def configure_tela(self):
        # comandos
        def run_cte():
            Auto_CTe.run()

        # background
        photo_cte = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'cte_window.png'))
        self.label_cte = tk.Label(self.app, image=photo_cte)
        self.label_cte.image = photo_cte
        self.label_cte.pack()

        # Rodar programa cte
        button_1 = tk.Button(self.app, text='Escolher XML', bg='dodgerblue3',
                             fg='white', font=('Times, 12 italic'), command=run_cte)
        button_1.place(relx=0.17, rely=0.5, relwidth=0.7)
       