from .arquivo import Arquivo
from .operadores import Operadores

class Valores():
    def __init__(self, cod, dados, posto: int):
        self.operador_cod = str(cod)

        try:
            self.nomes_brasifort, self.valores_brasifort = dados.get_brasifort()
        except:
            pass

        try:
            self.nomes_especies, self.valores_especies = dados.get_especies()
        except:
            pass

        try:
            self.nomes_depositos, self.valores_depositos = dados.get_depositos()
        except:
            pass

        try:
            self.nomes_brinks, self.valores_brinks = dados.get_brinks()
        except:
            pass

        print()
        print('='*40)
        print()

        self.operador = Operadores(posto).get(self.operador_cod)
        try:
            print(f'Operador: {self.operador[0]} | {self.operador[1]} | {self.operador[2]} | {self.operador[3]}')
        except:
            print(f'Operador: {self.operador}')

        self.brasifort = list()
        self.brinks = list()
        self.bradesco = list()
        self.dinheiro = list()

        


    def dados_brasifort(self):
        print('Valores na Brasifort: ', end='')
        if self.operador != None:
            try:
                if self.operador[1] in self.nomes_brasifort:
                    for valor in self.valores_brasifort:
                        if self.operador[1] in valor:
                            print(f'R$ {float(valor[self.operador[1]]):.2f}', end='; ')
                            self.brasifort.append(float(valor[self.operador[1]]))
                    print()
                else:
                    print('Sem valores')   
            except:
                print('Sem valores')  
        else:
            print('Sem valores')

        return self.brasifort
    

    def dados_brinks(self):
        print('Valores na Brinks: ', end='')
        if self.operador != None:
            try:
                if self.operador[3] in self.nomes_brinks:
                    for valor in self.valores_brinks:
                        if self.operador[3] in valor:
                            print(f'R$ {float(valor[self.operador[3]]):.2f}', end='; ')
                            self.brinks.append(float(valor[self.operador[3]]))
                    print()
                else:
                    print('Sem valores')   
            except:
                print('Sem valores')  
        else:
            print('Sem valores')

        return self.brinks
    


    def dados_depositos(self):
        print('Valores em Deposito: ', end='')
        if self.operador != None:
            try:
                if str(self.operador[2]) in self.nomes_depositos:
                    
                    for valor in self.valores_depositos:
                        if str(self.operador[2]) in str(valor):
                            print(f'R$ {float(valor[self.operador[2]]):.2f}', end='; ')
                            self.bradesco.append(float(valor[self.operador[2]]))
                    print()
                else:
                    print('Sem valores')   
            except:
                print('Sem valores') 
        else:
            print('Sem valores')

        return self.bradesco
    

    def dados_especies(self):
        print('Valores em Espécie: ', end='')
        if self.operador != None:
            try:
                if self.operador[2] in self.nomes_especies:
                    for valor in self.valores_especies:
                        if self.operador[2] in valor:
                            print(f'R$ {float(valor[self.operador[2]]):.2f}', end='; ') 
                            self.dinheiro.append(float(valor[self.operador[2]]))
                    print()
                else:
                    print('Sem valores')       
            except:
                print('Sem valores')             
        else:
            print('Sem valores')

        return self.dinheiro


"""dados = Arquivo()
frentista = Valores(2281, dados, '1')
especies = frentista.dados_especies()
depositos = frentista.dados_depositos()
brasifort = frentista.dados_brasifort()

dados.fechar_app()

print(f'{especies}\n{depositos}\n{brasifort}')"""