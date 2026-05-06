import tkinter as tk
from functions.tela import tela_na_resolução
from functions.caminho import resource_path
from backend.get_usuarios import Usuarios


class Alterar_Senha():
    def __init__(self, master, usuario):
        self.tela = tk.Toplevel(master)
        self._config = False
        self.usuario = str(usuario)
        self.tela.protocol("WM_DELETE_WINDOW", self.fechar)

    def run(self):
        self.configure_app()
        self.tela.master.wait_window()
    
    def fechar(self):
        self.tela.destroy()

    def configure_app(self):
        self.tela.title('Alterar Senha')
        self.tela.grab_set()
        self.tela.geometry(tela_na_resolução(300, 300))
        self.tela.resizable(False, False)
        self.configure_bg()
        self.alterar_senha()

    def configure_bg(self):
        img = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'senha_window.png'))
        self.bg = tk.Label(self.tela, image=img)
        self.bg.image = img
        self.bg.pack()

    def alterar_senha(self):    
        def alterar():
            self.senha_1 = str(nome_entry.get())
            self.senha_2 = str(senha_entry.get())
            id_usuario = Usuarios().get_id(usuario=self.usuario)
            from tkinter import messagebox
            if len(self.senha_1) >= 6:
                if self.senha_1 == self.senha_2:
                    try:
                        Usuarios().update_senha(senha=self.senha_1, id_cod=int(id_usuario))
                    except Exception as e:
                        messagebox.showerror(parent=self.tela.master, title='Erro!', message=f'Não foi possível alterar senha\nErro: {e}')
                        self._config = False
                    else:
                        messagebox.showinfo(parent=self.tela.master, title='Sucesso!', message=f'Alteração de senha sucedida!')
                        self._config = True
                        self.tela.destroy()
                else:
                    messagebox.showerror(parent=self.tela.master, title='Erro!', message=f'Dados informados incorretamente')
                    self._config = False
            else:
                messagebox.showerror(parent=self.tela.master, title='Erro!', message=f'Dados informados incorretamente')
                self._config = False

        # nome
        nome_entry = tk.Entry(self.tela)
        nome_entry.configure(show='*', bg='white', fg='black', borderwidth=0, highlightthickness=0,
                             font='Times, 12 italic')
        nome_entry.place(x=41, y=127,
                        width=210)

        # senha
        senha_entry = tk.Entry(self.tela)
        senha_entry.configure(show='*', bg='white', fg='black', borderwidth=0, highlightthickness=0,
                             font='Times, 12 italic')
        senha_entry.place(x=41, y=183,
                          width=210)
        
        #botão entrar
        self.img_senha = tk.PhotoImage(file=resource_path('Images', 'buttons', 'change_senha.png'))
        botao_entrar = tk.Button(self.tela, image=self.img_senha, highlightthickness=100, borderwidth=0, bg='green', command=alterar)
        botao_entrar.image = self.img_senha
        botao_entrar.place(x=109, y=230, width=100, height=40)