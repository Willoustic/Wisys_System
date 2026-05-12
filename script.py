from datetime import datetime
from time import sleep
import os

def formatacao(valor):
    if len(str(valor)) == 1:
        valor = f'0{valor}'

    return valor

class Data():
    def __init__(self):
        
        dia_anterior = int(datetime.today().day) - 1
        dia_atual = int(datetime.today().day)

        if dia_atual == 1 and dia_anterior > 28:
            mes = int(datetime.today().month) - 1
            #print("É o primeiro dia do mês, e o dia anterior é maior que 28.")
        else:
            mes = int(datetime.today().month)

        self.ano = datetime.today().year 
        self.dia = formatacao(dia_atual)
        self.mes = formatacao(mes)

        self.data = f'{self.dia}/{self.mes}/{self.ano}'
        #print(self.dia, self.mes, self.ano, self.data)
    
    def hora_atual():
        hora = formatacao(str(datetime.now().hour))
        minuto = formatacao(str(datetime.now().minute))
        segundos = formatacao(str(datetime.now().second))
        return f'{hora}:{minuto}:{segundos}'
    
class Script():
    def __init__(self):
        from PDV_Automatico.pdv import Caixa, Caixas
        from Emsys.login_emsys import Emsys

        dia = Data().dia
        mes = Data().mes
        ano = Data().ano
        while True:
            sleep(1)
            hora = Data.hora_atual() 
            print(hora)
            
            if hora == '05:00:00':
                Emsys(posto=1, name='usuario', password='password').run()
                Caixas(dia=dia, mes=mes, ano=ano, posto=1).Iniciar()
                sleep(10)
                Emsys(posto=2, name='usuario', password='password').run()
                Caixas(dia=dia, mes=mes, ano=ano, posto=2).Iniciar()
                sleep(10)
                Emsys(posto=3, name='usuario', password='password').run()
                Caixas(dia=dia, mes=mes, ano=ano, posto=3).Iniciar()
                sleep(10)
                os.system("shutdown /s /t 0")

Script()