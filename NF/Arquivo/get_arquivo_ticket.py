from tkinter import filedialog
import pandas as pd
from datetime import datetime
import os
import gc

class Arquivo_Ticket():
    def __init__(self):
        self.arquivo = filedialog.askopenfile(title= 'Selecione um arquivo', filetypes=[('Arquivos Excel', '*.xls;*.xlsx;*.csv')])
        print('Arquivo selecionado: ', self.arquivo.name)
        
        try:
            self.xls = pd.ExcelFile(self.arquivo.name)
        except:
            print('Não foi possível importar dados!')
        else:
            pass

        self.transações = list()
        self.conjunto = list()

    def get_nome_arquivo(self):
        nome = self.arquivo.name
        self.arquivo.close()
        self.xls.close()
        return nome

    def get_arquivo(self):
        df = pd.read_excel(self.arquivo.name)

        for i in range(0, len(df['Transação']), 1):
            transação = f'{df['Transação'].values[i]}'
            valor = f'{df['Valor da Transação'].values[i]}'
            combustivel = f'{df['Combustível'].values[i]}'
            litragem = f'{df['Litros'].values[i]}'
            data = f'{df['Data da Transação'].values[i]}'[0:10]
            data = data.split('-')
            data = f'{data[2]}.{data[1]}.{data[0]}'.replace('.', '/')

            self.transações.append(str(transação))
            self.conjunto.append({f'{transação}': [f'{valor}', f'{combustivel}', f'{litragem}', f'{data}']})

        self.arquivo.close()
        self.xls.close()
        return self.transações, self.conjunto
    
    def datas(self):
        datas = []
        #datas_normal = []
        for dados in self.conjunto:
            for i in dados:
                datas.append(dados[i][-1].replace('/', ''))
                #datas_normal.append(dados[i][-1])

        datas_ordenadas = sorted(datas, key=lambda x: datetime.strptime(x, "%d%m%Y"))
        self.arquivo.close()
        self.xls.close()
        #print(datas_normal)
        return datas_ordenadas