import tkinter as tk
import os
from tkinter import messagebox
from backend.get_postos import Banco
from functions.caminho import resource_path

class Tela_Select():
    def __init__(self, master):
        self.select = tk.Toplevel(master)
        self.banco = Banco()
        self._configurado = False
        self.select.protocol("WM_DELETE_WINDOW", self.fechar)
        self.select.grab_set()

    def fechar(self):
        self.selecionado = self.tipo = self.cod = None
        self.select.destroy()


# funções gerais
    def configure_app(self, ):
        self.select.title('Wisys Login')
        largura = self.select.winfo_screenwidth()
        altura = self.select.winfo_screenheight()
        x = (largura // 2) - (500 // 2)
        y = (altura // 2) - (200 // 2)
        

        self.select.geometry(f'{500}x{200}+{x}+{y-50}')
        self.select.resizable(False, False)
        self.configure_background_posto()
        self.select.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))
        self.config_tela()


    def configure_background_posto(self):
        self.photo_sp = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'select.png'))
        self.label_sc = tk.Label(self.select, image=self.photo_sp)
        self.label_sc.image = self.photo_sp
        self.label_sc.pack()

    def config_tela(self):
        self.selecionar()

    def selecionar(self):
        def pegar_selecao():
            sel = lista.curselection()
            if not sel:
                return
            self.selecionado = lista.get(sel[0])
            #print(self.selecionado)
            self.tipo = self.banco.get_class(self.selecionado)
            self.cod = self.banco.get_id(self.selecionado)
            #print(self.tipo)
            self.select.destroy()

        lista = tk.Listbox(self.select, selectmode=tk.SINGLE)
        
        lista.place(x=20, y=50, width=460, height=80)
        lista.configure(bg='dodgerblue4', fg='white', font='Times, 11 bold')

        for item in self.banco.get_nomes():
            lista.insert(tk.END, item)
        
        self.img_select = tk.PhotoImage(file=(resource_path('Images', 'buttons', 'SELECIO.png')))
        btn = tk.Button(self.select, image=self.img_select, highlightthickness=100, borderwidth=0, command=pegar_selecao)
        btn.image = self.img_select
        btn.place(x=380, y=145, width=100, height=40)


    def run(self):
        if not self._configurado:
            self.configure_app()
            self._configurado = True

        self.select.wait_window()
        return self.selecionado, self.tipo, self.cod