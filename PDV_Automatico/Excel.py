import pandas as pd
import os

class Excel:
    def csv_to_excel(arquivo_csv):
        df = pd.read_csv(arquivo_csv, sep=';')
        df.to_excel(arquivo_csv.replace('.csv', '.xlsx'), index=False)

        arquivo_csv = arquivo_csv.replace('.csv', '.xlsx')

        return arquivo_csv


    def ler_excel(arquivo_excel):
        df = pd.read_excel(arquivo_excel)
        return df
    

    def ajustar(planilha, nome):
        for i in planilha.columns:
            try:
                if i == 'dta_vencimento':
                    planilha = planilha.drop(columns=['dta_vencimento'])
            except:
                pass

        qtd_de_valores = 0
        for i in planilha['cod_pessoa'].items():
            qtd_de_valores += 1
        

        for i in planilha.columns:
            try:
                if i == 'dta_vencimento':
                    planilha = planilha.drop(columns=['dta_vencimento'])
            except:
                pass
            try:
                if i == 'dta_vencimento':
                    planilha = planilha.rename(columns=['dta_vencimento'])
            except:
                pass

        qtd_de_valores = len(planilha)
        

        planilha['Total bancos'] = [f"=SUM(F{i+2}:H{i+2})" for i in range(qtd_de_valores)]
        planilha['DIF'] = [f"=C{i+2}-D{i+2}" for i in range(qtd_de_valores)]

        planilha['Stone'] = [0] * qtd_de_valores 
        planilha['Cielo'] = [0] * qtd_de_valores
        planilha['Sites'] = [0] * qtd_de_valores

        planilha.to_excel(nome, index=False)


    def run(arquivo_inicial):
        arquivo_final = Excel.csv_to_excel(arquivo_csv=arquivo_inicial)    
        rel = Excel.ler_excel(arquivo_final)

        Excel.ajustar(rel, arquivo_final)
        if os.path.exists(arquivo_inicial):
            os.remove(arquivo_inicial)



