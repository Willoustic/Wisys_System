import tkinter as tk
from functions.tela import tela_na_resolução
from functions.caminho import resource_path
from backend.get_usuarios import Usuarios

class Info_window():
    def __init__(self, master, nome, cod, tipo):
        self.tela = tk.Toplevel(master)
        self.nome = nome
        self.cod = cod
        self.tipo = tipo
        self._config = False
        self.tela.protocol("WM_DELETE_WINDOW", self.fechar)

    
    def run(self):
        self.configure_app()
        self.tela.master.wait_window()
        return self._config
    
    def fechar(self):
        self._config = False
        self.tela.destroy()

    def configure_app(self):
        self.tela.title(f'Dados de {str(self.nome).upper()}')
        self.tela.grab_set()
        self.tela.geometry(tela_na_resolução(300, 150))
        self.tela.resizable(False, False)
        self.configure_bg()
        self.configure_visual()

    def configure_bg(self):
        img = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'user_info.png'))
        self.bg = tk.Label(self.tela, image=img)
        self.bg.image = img
        self.bg.pack()

    def configure_visual(self):
        def update():
            from tkinter import messagebox
            escolha = messagebox.askyesno(title='Atualização de Usuário', message=f'Confirma a atualização para o usuário: "{str(nome_entry.get())}"?', parent=self.tela)
            if escolha:
                try:
                   Usuarios().update(self.cod, str(nome_entry.get()), str(tipo_entry.get()).capitalize())
                except Exception as e:
                    messagebox.showerror(parent=self.tela.master, title='Erro!', message=f'Não foi possível atualizar usuário\nErro: {e}')
                    self._config = True
                else:
                    messagebox.showinfo(parent=self.tela.master, title='Sucesso!', message=f'Atualização concluida do usuario: {str(nome_entry.get())}!')
                    self.tela.destroy()
                    self.tela.master.destroy()
                    self._config = True


        # id label
        id_label = tk.Label(self.tela, text=f"{self.cod}", font='times, 8', justify='center')
        id_label.place(rely=0.22, relx=0.315, width=18)

        # nome entry (com o nome)
        nome = tk.StringVar(value=str(self.nome))

        nome_entry = tk.Entry(self.tela, textvariable=nome, font='times, 8', justify='center')
        nome_entry.place(relx=0.40, rely=0.37, width=100)

        # tipo entry (já com o tipo)

        tipo = tk.StringVar(value=str(self.tipo))

        tipo_entry = tk.Entry(self.tela, textvariable=tipo, font='times, 8', justify='center')
        tipo_entry.place(relx=0.36, rely=0.52, width=100)

        
        # botoes
        self.button_delete()

        btn_button = tk.Button(self.tela, text='Atualizar', highlightthickness=100, font='times, 8', borderwidth=0, command=update)
        btn_button.configure(fg='white', bg='green')
        btn_button.place(relx=0.57, rely=0.8, width=55, height=20)


    def button_delete(self):
        def delete():
            from tkinter import messagebox
            escolha = messagebox.askyesno(title='Exclusão de Usuário', message=f'Confirma a exclusão do usuário: "{self.nome}"?', parent=self.tela)
            if escolha:
                try:
                    Usuarios().del_nomes(self.cod)
                except Exception as e:
                    messagebox.showerror(parent=self.tela.master, title='Erro!', message=f'Não foi possível excluir usuário\nErro: {e}')
                    self._config = False
                else:
                    messagebox.showinfo(parent=self.tela.master, title='Sucesso!', message=f'Exclusão sucedida do usuario: {self.nome}!')
                    self._config = True
                    self.tela.destroy()
                    self.tela.master.destroy()
                    

        btn_button = tk.Button(self.tela, text='Deletar', highlightthickness=100, font='times, 8', borderwidth=0, command=delete)
        btn_button.configure(fg='white', bg='red')
        btn_button.place(relx=0.77, rely=0.8, width=55, height=20)

        

class Add_window():
    def __init__(self, master):
        self.tela = tk.Toplevel(master)
        self._config = False
        self.tela.protocol("WM_DELETE_WINDOW", self.fechar)

    def run(self):
        self.configure_app()
        self.tela.master.wait_window()
        return self._config
    
    def fechar(self):
        self._config = False
        self.tela.destroy()

    def configure_app(self):
        self.tela.title('Adicionar Usuário')
        self.tela.grab_set()
        self.tela.geometry(tela_na_resolução(300, 300))
        self.tela.resizable(False, False)
        self.configure_bg()
        self.nome_senha()

    def configure_bg(self):
        img = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'cadastro.png'))
        self.bg = tk.Label(self.tela, image=img)
        self.bg.image = img
        self.bg.pack()

    def nome_senha(self):    
        def cadastrar():
            self.nome = str(nome_entry.get()).capitalize()
            self.senha = str(senha_entry.get())
            tipo = 'All'
            #print(self.nome, self.senha)
            from tkinter import messagebox
            escolha = messagebox.askyesno(title='Inclusão de Usuário', message=f'Confirma a inclusão do usuário: "{self.nome}"?', parent=self.tela)
            if escolha:
                try:
                    Usuarios().add_single(nome=self.nome, senha=self.senha, tipo=tipo)
                except Exception as e:
                    messagebox.showerror(parent=self.tela.master, title='Erro!', message=f'Não foi possível criar usuário\nErro: {e}')
                    self._config = False
                else:
                    messagebox.showinfo(parent=self.tela.master, title='Sucesso!', message=f'Criação sucedida do usuario: {self.nome}!')
                    self._config = True
                    self.tela.destroy()
                    self.tela.master.destroy()

        # nome
        nome_entry = tk.Entry(self.tela)
        nome_entry.configure(bg='white', fg='black', borderwidth=0, highlightthickness=0,
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
        self.img_cad = tk.PhotoImage(file=resource_path('Images', 'buttons', 'cadastrar.png'))
        botao_entrar = tk.Button(self.tela, image=self.img_cad, highlightthickness=100, borderwidth=0, bg='green', command=cadastrar)
        botao_entrar.image = self.img_cad
        botao_entrar.place(x=109, y=230, width=100, height=40)