from tkinter import filedialog
import pandas as pd
import gc

class Arquivo():
    def __init__(self):
        self.arquivo = filedialog.askopenfile(title= 'Selecione um arquivo', filetypes=[('Arquivos Excel', '*.xls;*.xlsx;*.csv')])
        print('Arquivo selecionado: ', self.arquivo.name)
        try:
            self.xls = pd.ExcelFile(str(self.arquivo.name))
        except Exception as e:
            print('Não foi possível importar dados!\nErro:', e)
        else:
            pass
    
    def fechar_app(self):
        self.arquivo.close()
        self.xls.close()
        gc.collect()
        
    def get_brasifort(self):
        aba = 'BRASIFORT'

        for abas in self.xls.sheet_names:
            if aba.upper() == abas.upper():
                aba_selecionada = abas
                #print(aba_selecionada)
                break
        try:
            df = pd.read_excel(self.arquivo.name, sheet_name=aba_selecionada)
        except:
            print('Não existe essa aba no arquivo')
        else:
            nomes = list()
            valores = list()
            conjunto = list()

            if aba == 'BRASIFORT' :
                for a in range(0, len(df['Usuário Nome']), 1):
                    name = f'{df['Usuário Nome'].values[a]} {df['Usuário Sobrenome'].values[a]}'
                    nomes.append(name)
                    
                    valor = f'{df['Total Valor Automático'].values[a]}'
                    valores.append(valor)

                    conjunto.append({f'{name}': f'{valor}'})

                return nomes, conjunto
            else:       
                print('não existe essa aba')

    
    def get_brinks(self):
        aba = 'BRINKS'

        for abas in self.xls.sheet_names:
            if aba.upper() == abas.upper():
                aba_selecionada = abas
                #print(aba_selecionada)
                break
        try:
            df = pd.read_excel(self.arquivo.name, sheet_name=aba_selecionada)
        except:
            print('Não existe essa aba no arquivo')

        else:
            nomes = list()
            valores = list()
            conjunto = list()

            if aba == 'BRINKS' :
                for a in range(0, len(df['Depositante']), 1):
                    name = f'{df['Depositante'].values[a]}'
                    nomes.append(name)
                    
                    valor = f'{df['Valor do Depósito'].values[a]}'.replace(',', '.')

                    valores.append(valor)

                    conjunto.append({f'{name}': f'{valor}'})
                    #print({f'{name}': f'{valor}'})
                    
                return nomes, conjunto
            else:       
                print('não existe essa aba')



    def get_depositos(self):
        aba = 'DEPOSITOS'

        nomes_d = list()
        valores_d = list()
        conjunto_d = list()

        for abas in self.xls.sheet_names:
            if aba.upper() == abas.upper():
                aba_selecionada = abas
                #print(aba_selecionada)
                break
        try:
            df = pd.read_excel(self.arquivo.name, sheet_name=aba_selecionada)
        except:
            print('Não existe essa aba')
        else:
            if aba == 'DEPOSITOS' :
                for a in range(0, len(df['OPERADOR'.capitalize()]), 1):
                    name = f'{df['OPERADOR'.capitalize()].values[a]}'
                    nomes_d.append(name)
                    
                    valor = f'{df['VALOR'.capitalize()].values[a]}'
                    valores_d.append(valor)

                    conjunto_d.append({f'{name}': f'{valor}'})

                return nomes_d, conjunto_d
                
            else:       
                print('Não existe essa aba')


    def get_especies(self):
        aba = 'ESPECIE'

        nomes_e = list()
        valores_e = list()
        conjunto_e = list()

        for abas in self.xls.sheet_names:
            if aba.upper() == abas.upper():
                aba_selecionada = abas
                #print(aba_selecionada)
                break
        try:
            df = pd.read_excel(self.arquivo.name, sheet_name=aba_selecionada)
        except:
            print('Não existe essa aba')
        else:
            if aba == 'ESPECIE' :
                for a in range(0, len(df['OPERADOR'.capitalize()]), 1):
                    name = f'{df['OPERADOR'.capitalize()].values[a]}'
                    nomes_e.append(name)
                    
                    valor = f'{df['VALOR'.capitalize()].values[a]}'
                    valores_e.append(valor)

                    conjunto_e.append({f'{name}': f'{valor}'})
                
                return nomes_e, conjunto_e
            
            else:       
                print('Não existe essa aba')

    def run(self):
        brasifort_nomes, brasifort_valores = self.get_brasifort()
        depositos_nomes, depositos_valores = self.get_depositos()
        especies_nomes, especies_valores = self.get_especies()

        print(brasifort_valores)
        print(depositos_valores)
        print(especies_valores)

    def brasifort(self):
        brasifort_nomes, brasifort_valores = self.get_brasifort()
        for i in brasifort_valores:
            for nome in i:
                print(f'{nome}:', end=' ')
                for i in brasifort_valores:
                    if nome in i:
                        print(f'R$ {float(i[nome]):.2f}', end='; ')
            print('')


