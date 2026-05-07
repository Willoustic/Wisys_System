import tkinter as tk
from .Login import Tela_Login
from .Select_posto import Tela_Select, Banco
from functions.caminho import resource_path
from .warning import warning_box

class Tela:
    def __init__(self, root, nome: None, senha: None, cod: None, posto: None, tipo: None, classe: None):
        self.app = tk.Toplevel(root)
        self.usuario = str(nome)
        self.senha = str(senha)
        if posto == None:
            self.posto = 'Sem Posto Selecionado'
        else:
            self.posto = str(posto)
        self.tipo = str(tipo)
        self.classe = str(classe)
        self.id = cod
        self._resultado = None
        self.app.protocol("WM_DELETE_WINDOW", self.fechar)
        self._configurado = False
        self.configure_app()
        warning_box()

    def fechar(self):
        self._resultado = 'close'
        self.app.destroy()

# funções gerais
    def configure_app(self):
        self.app.title('Wisys')
        largura = self.app.winfo_screenwidth()
        altura = self.app.winfo_screenheight()
        x = (largura // 2) - (500 // 2)
        y = (altura // 2) - (500 // 2)

        self.app.geometry(f'{500}x{500}+{x}+{y-50}')
        self.app.resizable(False, False)
        self.configure_background_principal()
        self.app.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))
        self.configure_tela()

    def configure_background_principal(self):
        caminho = resource_path('Images', 'configure_tela', 'main.png')
        self.photo_bg = tk.PhotoImage(file=caminho)
        self.label_bg = tk.Label(self.app, image=self.photo_bg)
        self.label_bg.image = self.photo_bg
        self.label_bg.pack()
        
    def configure_tela(self):
        self.acessos()
        self.alinhar_nome_posto()
        self.show_nome_usuario()
        self.botao_login()
        

# definir acessos
    def acessos(self):
        def acesso_all():
            if self.tipo == 'All':                
                self.botão_ctf()                
                self.botao_depositos()                
                self.botao_pdv()                 
                self.botao_nf()                
                self.botao_contapagar()  
                self.botao_cte()
                             

        def acesso_admin():
            if self.classe == 'Admin':
                acesso_all()
                self.admin_freatures()

        def acesso_car():
            if self.tipo == 'CaP':
                self.botao_contapagar()
                pass

        if self.usuario != 'None':
            self.app.title('Wisys - Carregando...')
            self.mudar_senha() 
            acesso_car()
            acesso_all()
            acesso_admin()
            self.botao_select()
            self.app.title('Wisys')
        else:
            self.app.title('Wisys - Carregando...')
            self.app.title('Wisys')
        
    


# funções especificas
    def alinhar_nome_posto(self):
        self.posto_name = tk.Label(self.app, text=str(self.posto), bg='white', fg='black')
        self.posto_name.place(relx=0.165, rely=0.1, relwidth=0.7)
        self.posto_name.configure(justify='center')

    # botoes de funções
    def botão_ctf(self):
        from .ctf_window import ctf_window
        
        def ctf():
            ctf_window(self.app, cod_posto=self.id, usuario=self.usuario, password=self.senha)
            
        self.img_ctf = tk.PhotoImage(file=(resource_path('Images', 'buttons', 'ctf.png')))
        self.ctf_button = tk.Button(self.app, image=self.img_ctf, highlightthickness=100, command=ctf)
        self.ctf_button.image = self.img_ctf
        self.ctf_button.place(relx=0.1, rely=0.25, height=50, width=100)

    def botao_pdv(self):
        from .pdv_window import pdv_window
        def pdv():
            pdv_window(self.app, cod_posto=self.id, usuario=self.usuario, senha=self.senha)
        self.pdv_img = tk.PhotoImage(file=(resource_path('Images', 'buttons', 'pdv.png')))
        self.pdv_button = tk.Button(self.app, image=self.pdv_img, highlightthickness=100, command=pdv)
        self.pdv_button.image = self.pdv_img
        self.pdv_button.place(relx=0.4, rely=0.25, height=50, width=100)

    def botao_depositos(self):
        from .depositos_window import depositos_window
        def depositos():
            depositos_window(self.app, self.id, self.usuario, self.senha)
        self.dep_img = tk.PhotoImage(file=(resource_path('Images', 'buttons', 'depositos.png')))
        self.dep_button = tk.Button(self.app, image=self.dep_img, highlightthickness=100, command=depositos)
        self.dep_button.image = self.dep_img
        self.dep_button.place(relx=0.7, rely=0.25, height=50, width=100)

    def botao_nf(self):
        from .nf_window import App
        def nf():
            App(master=self.app)
        self.nf_img = tk.PhotoImage(file=(resource_path('Images', 'buttons', 'nf_button.png')))
        self.nf_button = tk.Button(self.app, image=self.nf_img, highlightthickness=100, command=nf)
        self.nf_button.img = self.nf_img
        self.nf_button.place(relx=0.1, rely=0.40, height=50, width=100)

    def botao_contapagar(self):
        from .cap_window import cap_window
        def cap():
            cap_window(self.app, self.id)
        self.cap_img = tk.PhotoImage(file=(resource_path('Images', 'buttons', 'cap.png')))
        self.cap_button = tk.Button(self.app, image=self.cap_img, highlightthickness=100, command=cap)
        self.cap_button.image = self.cap_img
        self.cap_button.place(relx=0.4, rely=0.40, height=50, width=100)

    def botao_cte(self):
        from .cte_window import Cte_window
        def cte():
            Cte_window(master=self.app)
        self.cap_img = tk.PhotoImage(file=(resource_path('Images', 'buttons', 'cte.png')))
        self.cap_button = tk.Button(self.app, image=self.cap_img, highlightthickness=100, command=cte)
        self.cap_button.image = self.cap_img
        self.cap_button.place(relx=0.7, rely=0.40, height=50, width=100)


    # configurações na tela

    def show_nome_usuario(self):
        self.nome = tk.Label(self.app, text=f'usuário: {str(self.usuario)}'.upper(), bg='white', fg='black')
        self.nome.configure(justify='left')
        self.nome.place(relx=0.04, rely=0.912, width=150)

    def botao_login(self):
        def logout():
            self._resultado = "logout"
            self.app.destroy()

        if str(self.usuario) == 'None':    
            img_login = tk.PhotoImage(file=resource_path('Images', 'buttons', 'login_1.png'))
        elif str(self.usuario) != 'None':
            img_login = tk.PhotoImage(file=resource_path('Images', 'buttons', 'logout.png'))

        logar = tk.Button(self.app, image=img_login, command=logout, highlightthickness=0, borderwidth=0.4)
        logar.image = img_login
        logar.place(x=313, y=450, height=40, width=80)

    def botao_select(self):
        def trocar_postos():
            #self.app.withdraw()
            posto, tipo, cod = Tela_Select(self.app).run()
            if posto:
                self.posto = posto
                self.tipo = tipo
                self.id = cod

            self.app.deiconify()
            self.refresh()

        img = tk.PhotoImage(file=resource_path('Images', 'buttons', 'alterar.png'))
        trocar_button = tk.Button(self.app, image=img, highlightthickness=0, border=0.4, command=trocar_postos)
        trocar_button.image = img
        trocar_button.place(x=400, y=450, height=40, width=80)

    def admin_freatures(self):
        def admin():    
            from .admin.admin_window import Admin_app
            Admin_app(self.app)
        
        img = tk.PhotoImage(file=resource_path('Images', 'buttons', 'admin.png'))
        admin = tk.Button(self.app, image=img, command=admin, highlightthickness=0, borderwidth=0.4)
        admin.image = img
        admin.place(x=400, y=400, height=40, width=80)

    def mudar_senha(self):
        def mudar():
            from .senha_window import Alterar_Senha
            Alterar_Senha(self.app, self.usuario).run()

        img = tk.PhotoImage(file=resource_path('Images', 'buttons', 'alterar_senha.png'))
        btn_mudar = tk.Button(self.app, image=img, highlightthickness=0, borderwidth=0, command=mudar)
        btn_mudar.image = img
        btn_mudar.place(x=226, y=450, height=40, width=80)


# funções de tela
    def wait(self):
        self.app.wait_window()
        return self._resultado
    
    def refresh(self):
        for widget in self.app.winfo_children():
            widget.destroy()
        self.configure_app()

        



def Programa():
    from backend.get_usuarios import Usuarios

    root = tk.Tk()
    root.withdraw()
    while True:
        nome = senha = posto = tipo_posto = cod = classe = None
        
        nome, senha = Tela_Login(root).run()
        if nome and senha:
            classe = Usuarios().get_tipo(str(nome).capitalize())
            posto, tipo_posto, cod = Tela_Select(root).run()
        

        tela = Tela(root, nome, senha, cod, posto, tipo_posto, classe)
        resultado = tela.wait()

        if resultado == 'logout':
            continue
        else:
            break 
        
    root.destroy()

    


def teste():
    Tela('nome', 'senha', '2', 'Posto Vitória', 'All')