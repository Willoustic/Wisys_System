import os

class Operadores:
    def __init__(self, posto):
        if str(posto) == '1':
            arquivo = os.path.join('Sangrias', 'operador', 'zn.txt')
        if str(posto) == '3':
            arquivo = os.path.join('Sangrias', 'operador', 'pv.txt')

        operadores = arquivo
        #print(operadores)

        linhas = open(operadores, 'r+')
        self.dados_geral = list()

        for a in linhas.readlines():
            dados = a.replace('\n', '')
            dados = dados.split(';')
            self.dados_geral.append(dados)

    def get(self, cod):
        for i in self.dados_geral:
            if str(cod) == i[0]:
                return i
        
        print(f'Não existe frentista cód: {str(cod)}')
        return None
        
    
