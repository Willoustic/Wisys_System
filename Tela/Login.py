import tkinter as tk
import os
from tkinter import messagebox
from functions.caminho import resource_path
from backend.get_usuarios import Usuarios

class Tela_Login():
    def __init__(self, master):
        self.login = tk.Toplevel(master)
        self.login.protocol("WM_DELETE_WINDOW", self.fechar)
        self._configurado = False

    def fechar(self):
        self.nome = self.senha = None
        self.login.destroy()

# funções gerais
    def configure_app(self):
        self.login.title('Wisys Login')
        largura = self.login.winfo_screenwidth()
        altura = self.login.winfo_screenheight()
        x = (largura // 2) - (300 // 2)
        y = (altura // 2) - (300 // 2)

        self.login.geometry(f'{300}x{300}+{x}+{y-50}')
        self.login.resizable(False, False)
        self.configure_background()
        self.login.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))
        self.config_tela()


    def configure_background(self):
        self.photo = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'login.png'))
        self.label = tk.Label(self.login, image=self.photo)
        self.label.image = self.photo
        self.label.pack()

    def config_tela(self):
        self.nome_senha()

    def nome_senha(self):    
        def get_acesso():
            self.nome = str(nome_entry.get())
            self.senha = str(senha_entry.get())
            if len(self.nome) < 3:
                messagebox.showwarning(title='Dados Invalidos',
                                        message='Dados informados incorretamente!')
            elif len(self.senha) < 6:
                messagebox.showwarning(title='Dados Invalidos',
                                        message='Dados informados incorretamente!')
            else:
                login = Usuarios().autenticar(nome=self.nome.capitalize(), senha=self.senha)
                if login:
                    self.login.destroy()
                else:
                    messagebox.showwarning(parent=self.login, title='Dados Invalidos',
                                        message='Usuário e senha inválido!')
                    
        # nome
        nome_entry = tk.Entry(self.login)
        nome_entry.configure(bg='white', fg='black', borderwidth=0, highlightthickness=0,
                             font='Times, 12 italic')
        nome_entry.place(x=41, y=127,
                        width=210)

        # senha
        senha_entry = tk.Entry(self.login)
        senha_entry.configure(show='*', bg='white', fg='black', borderwidth=0, highlightthickness=0,
                             font='Times, 12 italic')
        senha_entry.place(x=41, y=183,
                          width=210)
        
        #botão entrar
        self.img_login = tk.PhotoImage(file=resource_path('Images', 'buttons', 'LOGIN.png'))
        botao_entrar = tk.Button(self.login, image=self.img_login, highlightthickness=100, borderwidth=0, bg='green', command=get_acesso)
        botao_entrar.image = self.img_login
        botao_entrar.place(x=109, y=230, width=70, height=40)
        

    def run(self):
        if not self._configurado:
            self.configure_app()
            self._configurado = True
            
        self.login.wait_window()
        return self.nome, self.senha
    
