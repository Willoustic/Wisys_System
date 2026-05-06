import tkinter as tk
from NF.Auto.gerar_nota import Nota_Fiscal
from NF.Auto.relatorios_ticket import Cupom
from functions.tela import tela_na_resolução
import os
from functions.caminho import resource_path

class App():
    def __init__(self, master):
        self.master = master
        self.app = tk.Toplevel(master)
        self.configure_app()
        self.configure_tela()

        
    def configure_app(self):    
        self.app.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))
        self.app.title('Nota Fiscal')
        self.app.geometry(tela_na_resolução(width=280, height=300))
        self.app.resizable(False, False)
        self.app.attributes('-topmost', True)


    def configure_tela(self):
        # comandos
        def relatorios():
            from tkinter import messagebox
            try:
                rel_pasta = resource_path('Arquivos', 'Relatórios NF')
                os.startfile(rel_pasta)
            except Exception as e:
                messagebox.showinfo(parent=self.app, title='Erro!', message='Não foi gerado nenhum relátorio!')

        def full_aut():
            try:
                Cupom().verificar_transação()
            except Exception as e:
                print(e)

        def custom_aut():
            try:
                valor = int(ticket_entry.get())
            except Exception as e:
                print(e)
            else:
                print(valor)
                if valor <= 10:
                    try:
                        Cupom().verificar_transação_4digit(valor)
                    except Exception as e:
                        print(e)

        def gerar_padrao():
            try:
                Nota_Fiscal.emitir_padrão()
            except Exception as e:
                print(e)
        
        def gerar_ticket():
            try:
                Nota_Fiscal.emitir_ticket()
            except Exception as e:
                print(e)
            
        def gerar_valecard():
            try:
                Nota_Fiscal.emitir_valecard()
            except Exception as e:
                print(e)

        def gerar_danfe():
            try:
                Nota_Fiscal.emitir_pdf()
            except Exception as e:
                print(e)

        # background
        photo_nf = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'nf_window.png'))
        self.label_nf = tk.Label(self.app, image=photo_nf)
        self.label_nf.image = photo_nf
        self.label_nf.pack()

        # inicio
        button_1 = tk.Button(self.app, text='Relátorios', bg='oldlace', font=('Times, 12 italic'), command=relatorios)
        button_1.place(relx=0.05, rely=0.07, relwidth=0.4)
       
        # procurar na ticket
        button_2 = tk.Button(self.app, text='Autorização\nCompleta', bg='dodgerblue3', fg='white', justify='center', command=full_aut)
        ticket_entry = tk.Entry(self.app, justify='center')
        button_3 = tk.Button(self.app, text='Autorização\nPersonalizada', bg='dodgerblue3', fg='white', justify='center', command=custom_aut)

        button_2.place(relx=0.05, rely=0.38, relwidth=0.43)
        ticket_entry.place(rely=0.315, relx=0.5, relwidth=0.06, relheight=0.05)
        button_3.place(relx=0.5, rely=0.38, relwidth=0.43)

        # gerar notas
        button_4 = tk.Button(self.app, text='Gerar Nota Fiscal', justify='center', bg='dodgerblue3', fg='white', command=gerar_padrao)
        button_5 = tk.Button(self.app, text='Gerar Nota + DANFE', justify='center', bg='dodgerblue3',  fg='white', command=gerar_danfe)
        button_6 = tk.Button(self.app, text='Gerar Nota + Ticket', justify='center', bg='dodgerblue3', fg='white', command=gerar_ticket)
        button_7 = tk.Button(self.app, text='Gerar Nota + Valecard', justify='center', bg='dodgerblue3', fg='white', command=gerar_valecard)

        button_4.place(relwidth=0.43, relheight=0.1, relx=0.05, rely=0.68)
        button_5.place(relwidth=0.43, relheight=0.1, relx=0.5, rely=0.68)
        button_6.place(relwidth=0.43, relheight=0.1, relx=0.05, rely=0.8)
        button_7.place(relwidth=0.43, relheight=0.1, relx=0.5, rely=0.8)
