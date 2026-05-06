import tkinter as tk
from functions.tela import tela_na_resolução
from backend.get_bancos import Mnemonicos
from datetime import datetime
import os
from functions.caminho import resource_path
from CaP.cap_auto import Contas_a_pagar

def cap_window(master, cod):
    app = tk.Toplevel(master)
    bancos = Mnemonicos()
    
    # Comandos
    def data_format(event):
        data = periodo_entry_dep.get().replace('/', '')
        data = ''.join(filter(str.isdigit, data))[:8]

        nova_data = ""
        if len(data) >= 1:
            nova_data += data[:2]
        if len(data) >= 3:
            nova_data = data[:2] + '/' + data[2:4]

        if len(data) >= 5:
            nova_data = data[:2] + '/' + data[2:4] + '/' + data[4:]

        periodo_entry_dep.delete(0, tk.END)
        periodo_entry_dep.insert(0, nova_data)

    def get_dados():
        data_dep = periodo_entry_dep.get()
        data_dep = str(data_dep).replace('/', '')
        try:
            if len(data_dep) > 4:
                dia = data_dep[:2]
                mes = data_dep[2:4] 
                ano = data_dep[-4:]
            elif len(data_dep) == 4:
                dia = data_dep[:2]
                mes = data_dep[2:4]
                ano = datetime.today().year
                data_dep = f'{dia}{mes}{ano}'
        except:
            pass
        
        if len(data_dep) >= 4:
            print(data_dep)
            sel = lista.curselection()
            if not sel:
                return
            print('passa')
            banco_selecionado = lista.get(sel[0])
            print(banco_selecionado)
            Contas_a_pagar(data_dep, banco_selecionado)
        
        else:
            from tkinter import messagebox
            messagebox.showerror(parent=app, title='Erro', message='Digite a data corretamente!')



    # Configuração geral
    app.title('Contas a Pagar')
    app.geometry(tela_na_resolução(280, 200))
    app.attributes('-topmost', True)
    app.resizable(False, False)
    app.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))

    # BACKGROUND
    img = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'cap.png'))
    bg = tk.Label(app, image=img)
    app.image = img
    bg.place(x=0, y=0, relheight=1, relwidth=1)


    # Interface
    lista = tk.Listbox(app, selectmode=tk.SINGLE)

    for item in bancos.get_bancos(cod):
            lista.insert(tk.END, item)

    lista.place(x=20, y=79, width=240, height=70)
    lista.configure(bg='dodgerblue4', fg='white', font='Times, 13 bold')

    periodo_entry_dep = tk.Entry(app)
    periodo_entry_dep.bind('<KeyRelease>', data_format)
    periodo_entry_dep.configure(background='dodgerblue4', fg='white', border=2, font=('Times, 14 italic'))
    periodo_entry_dep.place(x=85, y=38, width=108)

    button = tk.Button(app, text='Executar', bg='dodgerblue4', fg='white', command=get_dados)
    button.place(relx=0.73, rely=0.8)
    