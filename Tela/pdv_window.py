from functions.tela import tela_na_resolução
import tkinter as tk
from PDV_Automatico.pdv import Caixa, Caixas
from Emsys.login_emsys import Emsys
from Sangrias.autom.auto import Sangrias
from functions.caminho import resource_path
import os

def pdv_window(master, cod_posto, usuario, senha):
    from datetime import datetime
    def data_format(event):
        data = periodo_entry_pdv.get().replace('/', '')
        data = ''.join(filter(str.isdigit, data))[:8]

        nova_data = ""
        if len(data) >= 1:
            nova_data += data[:2]
        if len(data) >= 3:
            nova_data = data[:2] + '/' + data[2:4]

        if len(data) >= 5:
            nova_data = data[:2] + '/' + data[2:4] + '/' + data[4:]

        periodo_entry_pdv.delete(0, tk.END)
        periodo_entry_pdv.insert(0, nova_data)


    def pdv_incializar():
        data_pdv = periodo_entry_pdv.get()
        data_pdv = str(data_pdv).replace('/', '')
        try:
            if len(data_pdv) > 4:
                dia = data_pdv[:2]
                mes = data_pdv[2:4] 
                ano = data_pdv[-4:]
            elif len(data_pdv) < 4:
                dia = data_pdv[:2]
                mes = data_pdv[2:4] 
                ano = str(datetime.today().year)
        except:
            pass

        if len(data_pdv) >= 4:
            Emsys(posto=cod_posto, name=usuario, password=senha).run()
            Caixas(dia=dia, mes=mes, ano=ano, posto=cod_posto).Iniciar()


    def pdv_fechamento():
        data_pdv = periodo_entry_pdv.get()
        data_pdv = str(data_pdv).replace('/', '')
        try:
            if len(data_pdv) > 4:
                dia = data_pdv[:2]
                mes = data_pdv[2:4] 
                ano = data_pdv[-4:]
            elif len(data_pdv) < 4:
                dia = data_pdv[:2]
                mes = data_pdv[2:4] 
                ano = str(datetime.today().year)
        except:
            pass

        if len(data_pdv) >= 4:
            Emsys(posto=cod_posto, name=usuario, password=senha).run()
            Caixas(dia=dia, mes=mes, ano=ano, posto=cod_posto).Finalizar()


    def pdv_rateio():
        data_pdv = periodo_entry_pdv.get()
        data_pdv = str(data_pdv).replace('/', '')     
        
        if len(data_pdv) >= 4:         
            Emsys(posto=cod_posto, name=usuario, password=senha).run()
            Emsys.abrir_pdv()
            Caixa.select_data(data_pdv)
            Caixa.inserir_rateio()


    def pdv_confirmar():
        data_pdv = periodo_entry_pdv.get()
        data_pdv = str(data_pdv).replace('/', '')

        if len(data_pdv) >= 4:
            Emsys(posto=cod_posto, name=usuario, password=senha).run()
            Emsys.abrir_pdv()
            Caixa.select_data(data_pdv)
            Caixa.confirmar()
            

    def pdv_excluir():
        data_pdv = periodo_entry_pdv.get()
        data_pdv = str(data_pdv).replace('/', '')

        if len(data_pdv) >= 4:
            Emsys(posto=cod_posto, name=usuario, password=senha).run()
            Emsys.abrir_pdv()
            Caixa.select_data(data_pdv)
            Caixa.excluir_sangria()

    win_pdv = tk.Toplevel()
    win_pdv.configure(bg='gray10')
    win_pdv.title('PDV Fechamento de Caixa')
    win_pdv.geometry(tela_na_resolução(width=500, height=200))
    win_pdv.resizable(False, False)  

    win_pdv.iconbitmap(resource_path('Images', 'configure_tela', 'icon.ico'))  
    photo = tk.PhotoImage(file=resource_path('Images', 'configure_tela', 'pdv_window.png'))
    photo_label = tk.Label(win_pdv, image=photo)
    photo_label.image = photo
    photo_label.pack()

    win_pdv.transient(master)
    win_pdv.grab_set()

    periodo_entry_pdv = tk.Entry(win_pdv)
    periodo_entry_pdv.bind('<KeyRelease>', data_format)
    periodo_entry_pdv.configure(background='gray30', fg='white', border=2, font=('Times, 17 italic'), justify='left')
    periodo_entry_pdv.place(x=195, y=60, width=125)
    
    # funções do caixa
    inicializar = tk.Button(win_pdv, text='Inicializar', bg='dodgerblue3', fg='white', font=('Times, 16 italic'), command=pdv_incializar)
    inicializar.place(x=210, y=140, width=130, height=40)
    
    fechamento = tk.Button(win_pdv, text='Fechamento', bg='dodgerblue3', fg='white', font=('Times, 16 italic'), command=pdv_fechamento)
    fechamento.place(x=350, y=140, width=130, height=40)

    # abrir pasta dos relatórios
    relatorios_button = tk.Button(win_pdv, text='Relátorios', bg='white', fg='black', font=('Times, 16 italic'), command=lambda: os.startfile(resource_path('Arquivos', 'Relatorios')))
    relatorios_button.place(x=70, y=140, width=130, height=40)

    
    
