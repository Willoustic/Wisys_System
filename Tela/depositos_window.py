import os
import tkinter as tk
from Sangrias.autom.auto import Sangrias
from Emsys.login_emsys import Emsys
from PDV_Automatico.pdv import Caixa, Caixas
from functions.tela import tela_na_resolução
from functions.caminho import resource_path


def depositos_window(master, cod_posto, usuario, password):
    from datetime import datetime
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


    def fazer_depositos():
        
        from Sangrias.backend.arquivo import Arquivo
        data_dep = periodo_entry_dep.get()
        data_dep = str(data_dep).replace('/', '')
        try:
            if len(data_dep) > 4:
                dia = data_dep[:2]
                mes = data_dep[2:4] 
                ano = data_dep[-4:]
            elif len(data_dep) == 2:
                dia = data_dep[:2]
                mes = data_dep[2:4]
                ano = datetime.today().year
        except:
            pass

        if len(data_dep) >= 4:
            win_dep.destroy()
            dados = Arquivo()
            Emsys(posto=cod_posto, name=usuario, password=password).run()
            Emsys.abrir_pdv()
            Caixa.select_data(data_dep)
            Sangrias.run(dados, cod_posto, f'{dia}{mes}{ano}')
            dados.fechar_app()
    


    win_dep = tk.Toplevel(master)
    win_dep.title('Ajustar Depositos')
    win_dep.geometry(tela_na_resolução(width=400, height=150))
    win_dep.resizable(False, False) 

    win_dep.transient(master)
    win_dep.grab_set()

    win_dep.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))
    photo = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'depositos_window.png'))
    photo_label = tk.Label(win_dep, image=photo)
    photo_label.image = photo
    photo_label.pack()
    
    periodo_entry_dep = tk.Entry(win_dep)
    periodo_entry_dep.bind('<KeyRelease>', data_format)
    periodo_entry_dep.configure(background='dodgerblue4', fg='white', border=2, font=('Times, 15 italic'))
    periodo_entry_dep.place(x=130, y=58, width=110)
    
    depositos_run = tk.Button(win_dep, text='Ajustar Depósitos', bg='dodgerblue3', fg='white', font=('Times, 12 italic'), command=fazer_depositos)
    depositos_run.place(x=250, y=100)
        