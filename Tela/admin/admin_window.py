import tkinter as tk
import os
from tkinter import messagebox
from backend.get_usuarios import Usuarios
from functions.caminho import resource_path


class Tela_Admin():
    def __init__(self, master):
        self.master = master
        self.app = tk.Toplevel(master)
        self._configurado = False
        self.app.protocol("WM_DELETE_WINDOW", self.fechar)
        self.app.grab_set()

    def fechar(self):
        self.selecionado = self.tipo = self.cod = None
        self.app.destroy()

# funções gerais
    def configure_app(self, ):
        self.app.title('Wisys Admin')
        largura = self.app.winfo_screenwidth()
        altura = self.app.winfo_screenheight()
        x = (largura // 2) - (500 // 2)
        y = (altura // 2) - (200 // 2)
        
        self.app.geometry(f'{500}x{200}+{x}+{y-50}')
        self.app.resizable(False, False)
        self.configure_background_posto()
        self.app.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))
        self.config_tela()

    def configure_background_posto(self):
        self.photo_sp = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'tela_admin.png'))
        self.label_sc = tk.Label(self.app, image=self.photo_sp)
        self.label_sc.image = self.photo_sp
        self.label_sc.pack()

    def config_tela(self):
        self.selecionar()
        self.add_usuario()

        
    # select usuario
    def selecionar(self):
        def pegar_selecao():
            from .admin_freatures import Info_window
            try:
                sel = lista.curselection()
                if not sel:
                    return
                self.selecionado = lista.get(sel[0])
                self.tipo = Usuarios().get_tipo(self.selecionado)
                self.cod = Usuarios().get_id(self.selecionado)
                user_info = Info_window(self.app, self.selecionado, self.cod, self.tipo).run()
                
                if user_info == True:
                    self._configurado = False
            except:
                pass

        lista = tk.Listbox(self.app, selectmode=tk.SINGLE)
        
        lista.place(x=20, y=50, width=460, height=80)
        lista.configure(bg='dodgerblue4', fg='white', font='Times, 11 bold')

        for item in Usuarios().get_all_dados():
            lista.insert(tk.END, item[1])

        self.img_select = tk.PhotoImage(file=(resource_path('Images', 'buttons', 'selec_usuario.png')))
        btn = tk.Button(self.app, image=self.img_select, highlightthickness=100, borderwidth=0, command=pegar_selecao)
        btn.image = self.img_select
        btn.place(x=380, y=145, width=100, height=40)



    def add_usuario(self):
        def add():
            from .admin_freatures import Add_window
            try:
                user_info = Add_window(self.app).run()
                if user_info == True:
                    self._configurado = False
            except Exception as e:
                print(e)


        self.img_add = tk.PhotoImage(file=(resource_path('Images', 'buttons', 'add_usuario.png')))
        btn_add = tk.Button(self.app, image=self.img_add, highlightthickness=100, borderwidth=0, command=add)
        btn_add.image = self.img_add
        btn_add.place(x=270, y=145, width=100, height=40)


    
    def run(self):
        if not self._configurado:
            self.configure_app()
            self._configurado = True

        self.app.wait_window()
        return self._configurado


def Admin_app(master):
    while True:
        condition = Tela_Admin(master).run()
        if condition:
            break