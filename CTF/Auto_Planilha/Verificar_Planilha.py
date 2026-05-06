import pandas as pd
import xlrd as xl
import pyautogui as px
from time import sleep
import os

nome_planilha = os.path.join('CTF', 'Planilha da Automação.xlsx')
nome_relatorio = nome_planilha

def pegar_lista():
    lista = list()

    relatorio = pd.read_excel(nome_relatorio, index_col=False)

    placas = relatorio['Autorização']
    valores = relatorio['Valor']

    for pos_placa, placa in enumerate(placas):
        try:
            placa = str(f'{float(placa):.0f}')
        except:
            pass
        
        for pos_valor, valor in enumerate(valores):
            if pos_valor == pos_placa:
                dic = {
                    'Placa': f'{placa}',
                    'Valor': valor,
                    'Operador': ''
                }
                lista.append(dic)
    
    return lista

def verificar_dados(lista):
    from datetime import datetime
    print('=+' * 20)
    print('')
    print(f'Dados informados às {datetime.now().strftime("%H:%M:%S")} de {datetime.now().day}/{datetime.now().month}/{datetime.now().year}: ')
    print('')
    for dados in lista:
        try:
            print(f"""Aut: {dados['Placa']} | Valor: {float(dados['Valor']):.2f}""")
        except:
            print('Dados informados incorretamente')
    print('')
    print('=+' * 20)
    print('')
    print('Programa finalizado')

