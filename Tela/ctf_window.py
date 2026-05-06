import os
import tkinter as tk
from CTF.Auto_Planilha.Verificar_Planilha import pegar_lista, verificar_dados
from Emsys.login_emsys import Emsys
from PDV_Automatico.pdv import Caixa, Caixas
from functions.tela import tela_na_resolução
from CTF.ctf_config import Auto_CTF
from functions.caminho import resource_path

def ctf_window(master, cod_posto, usuario, password):
    def data_format(event):
        data = periodo_entry.get().replace('/', '')
        data = ''.join(filter(str.isdigit, data))[:8]

        nova_data = ""
        if len(data) >= 1:
            nova_data += data[:2]
        if len(data) >= 3:
            nova_data = data[:2] + '/' + data[2:4]

        if len(data) >= 5:
            nova_data = data[:2] + '/' + data[2:4] + '/' + data[4:]

        periodo_entry.delete(0, tk.END)
        periodo_entry.insert(0, nova_data)

#tentar abrir a planilha da automação
    def abrir_planilha():
        ctf_planilha = os.path.join('CTF', 'Planilha da Automação.xlsx')
        try:
            os.startfile(ctf_planilha)
        except:
            pass

#automatizar os ctf
    def automatizar():
        def pegar_dados():
            lista = pegar_lista()
            #verificar_dados(lista=lista)
            return lista

        data_total = periodo_entry.get()
        data_total = str(data_total).replace('/', '')
        vendas = pegar_dados()
        if len(data_total) >= 4:
            Emsys(posto=cod_posto, name=usuario, password=password).run()
            Emsys.abrir_pdv()
            Caixa.select_data(data=data_total)
            Auto_CTF.run(vendas)

    win_ctf = tk.Toplevel(master)
    #win_ctf.configure(bg='gray10')
    win_ctf.title('Automatizar CTF')
    win_ctf.resizable(False, False)
    win_ctf.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))
    win_ctf.geometry(tela_na_resolução(width=450, height=150))
    photo = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'ctf_window.png'))
    photo_label = tk.Label(win_ctf, image=photo)
    photo_label.image = photo
    photo_label.pack()

    win_ctf.transient(master)
    win_ctf.grab_set()

    periodo_entry = tk.Entry(win_ctf)
    periodo_entry.bind('<KeyRelease>', data_format)
    periodo_entry.place(y=25, x=113, width=145)
    periodo_entry.configure(border=1, font=('Times, 20 italic'))

    planilha = tk.Button(win_ctf, text='Abrir Planilha', bg='dodgerblue3', fg='white', command=abrir_planilha)
    planilha.place(x=19, y=80, width=120, height=40)

    automatizar_ctf = tk.Button(win_ctf, text='Automatizar', bg='dodgerblue3', fg='white', command=automatizar)
    automatizar_ctf.place(x=147, y=80, width=120, height=40)


