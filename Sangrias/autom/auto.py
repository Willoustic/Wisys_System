from PDV_Automatico.processos import imagens_pdv, Img
from Sangrias.backend.valores import Valores
import pyperclip as pc
from PDV_Automatico.pdv import Caixa
import ctypes
import pyautogui as px


def caps_lock_ativado():
    # 0x14 é o código da tecla Caps Lock
    return bool(ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1)


class Sangrias():
    def __init__(self, arquivo, empresa):
        self.pst = imagens_pdv('Sangrias')
        self.dados = arquivo
        self.posto = empresa

        if str(self.posto) == '1':
            self.banco_bradesco = str('BRA799-4').upper()
            self.banco_brasifort = str('BRAZIFORT').upper()
            self.banco_brinks = str('BRINKS_ZN').upper()
        elif str(self.posto) == '3':
            self.banco_brasifort = str('BRAZIFO_VI').upper()
            self.banco_brinks = str('BRINKS_VIT').upper()
    
    def pegar_operador(self):
        operador = self.pst.join('operador.png')

        pc.copy('')

        operador_x, operador_y = Img.coordenadas(operador, precisão=0.9)
        px.doubleClick(operador_x+100, operador_y)
        px.hotkey('ctrl', 'c')
        
        cod_operador = pc.paste()
        if len(str(cod_operador)) < 1:
            cod_operador = None

        #print(cod_operador)
        self.frentista = Valores(cod_operador, self.dados, posto=self.posto)
        if self.frentista.operador == None:
            return False
        else:
            self.especies = self.frentista.dados_especies()
            self.brasifort = self.frentista.dados_brasifort()
            self.depositos = self.frentista.dados_depositos()
            self.brinks = self.frentista.dados_brinks()
            return True
         

    def clicar_sangrias(self):
        #clicar para entrar em sangrias
        aba_sangrias = self.pst.join('aba_sangrias.png')
        
        Img.verifica_na_tela(aba_sangrias, 0.99)
        x, y = Img.coordenadas(aba_sangrias, 0.99)
        px.moveTo(x-50, y)
        px.click()


    def clicar_no_primeiro(self):
        especie_dinheiro = self.pst.join('especie_dinheiro.png')
        alterar = self.pst.join('alterar.png')
        without_alterar = self.pst.join('without_alterar.png')

        x, y = Img.coordenadas(especie_dinheiro, 0.9)
        px.moveTo(x, y+40)
        px.click()

        if Img.verifica_na_tela(alterar, 0.98) == False:
            return False
        else:
            return True


    def verificar_valor(self):
        documento = self.pst.join('documento.png')
        alterar = self.pst.join('alterar.png')

        Img.click(alterar, 0.98)

        x, y = Img.coordenadas(documento, 0.9)        

        px.moveTo(x-65, y)
        px.doubleClick()
        
        px.hotkey('ctrl', 'c')

        self.valor_sangria = pc.paste()
        self.valor_sangria = self.valor_sangria.replace(',', '.')

        px.hotkey('alt', 'f4')
        Img.verificar_até_sair(documento, 0.9)
        return self.valor_sangria
    

    def excluir_sangria(self):
        excluir = self.pst.join('excluir.png')
        confirm = self.pst.join('confirm.png')

        Img.click(excluir, 0.9)
        Img.verificar_até_achar(confirm, 0.9)
        Img.click(confirm, 0.9)
        px.press('enter')
        

    def abrir_aba_dep(self):
        aba_dep = self.pst.join('depositos_em_conta.png')
        recib_1 = self.pst.join('recib_1.png')
        recib_2 = self.pst.join('recib_2.png')
        tela_dep = self.pst.join('tela_dep.png')
        incluir = self.pst.join('incluir_dep.png')
        self.tela_incluir = self.pst.join('incluir_tela.png')
    
        while Img.verifica_na_tela(aba_dep, 0.9) == False:
            Img.DoubleClick(recib_1, 0.9)
            Caixa.clicar_resumo()

        Img.click(aba_dep, 0.9)
        Img.click(incluir, 0.9)
        Img.verificar_até_achar(self.tela_incluir, 0.9)
        Img.click(self.tela_incluir, 0.9)
        


    def adicionar_brasifort(self, sangria, data):
        if int(sangria) in self.brasifort:
            self.abrir_aba_dep()
            #adicionar no depositos
            px.press('tab')
            px.press('tab')
            px.write(data)
            px.write(sangria)
            px.press('tab')
            px.write(self.banco_brasifort)
            px.press('insert')
            Img.verificar_até_sair(self.tela_incluir, 0.9)

    def adicionar_brinks(self, sangria, data):
        if int(sangria) in self.brinks:
            self.abrir_aba_dep()
            #adicionar no depositos
            px.press('tab')
            px.press('tab')
            px.write(data)
            px.write(sangria)
            px.press('tab')
            px.write(self.banco_brinks)
            px.press('insert')
            Img.verificar_até_sair(self.tela_incluir, 0.9)

    def adicionar_depositos(self, sangria, data):
        if int(sangria) in self.depositos:
            self.abrir_aba_dep()
             #adicionar no depositos
            px.press('tab')
            px.press('tab')
            px.write(data)
            px.write(sangria)
            px.press('tab')
            px.write(self.banco_bradesco)
            px.press('insert')
            Img.verificar_até_sair(self.tela_incluir, 0.9)


    def salvar(self):
        salvar_button = self.pst.join('salvar.png')
        salvo = self.pst.join('salvo.png')

        Img.click(salvar_button, 0.9)
        Img.verificar_até_achar(salvo, 0.9)
        px.press('enter')
        Img.verificar_até_sair(salvo, 0.9)


    def proximo(self):
        proximo_button = self.pst.join('proximo.png')
        Img.click(proximo_button, 0.9)


    def run(arquivo, posto, data):
        dados = arquivo
        pdv = 1
        if caps_lock_ativado() == True:
            px.press('CAPSLOCK')
        while True:
            if pdv > 1:
                Caixa.clicar_resumo()

            ultimo_caixa = imagens_pdv('rateio').join('ultimo_Caixa.png')
            if Img.verifica_na_tela(ultimo_caixa, 0.98) == True:
                break
            
            app = Sangrias(dados, posto)
            condition = app.pegar_operador()
            
            if Caixa.verifica_pendencia() == False:
                print('')
                print('Valores encontrados: ', end='')
                if condition == True:
                    cont = 0
                    cont_brasifort = 0
                    cont_dep = 0
                    cont_brinks = 0

                    qtd = 0
                    while True:
                        
                        if qtd == (len(app.especies) + len(app.depositos) + len(app.brasifort) + len(app.brinks)):
                                app.salvar()
                                app.proximo()
                                pdv += 1
                                break
                         
                        app.clicar_sangrias()
                        if app.clicar_no_primeiro() == True:
                            from time import sleep
                            sleep(1)
                            if cont > 0:
                                for i in range(0, cont):
                                    #print(cont)
                                    px.press('down')
                                    sleep(1)                              

                            sangria = app.verificar_valor()
                            print(f'R$ {float(str(sangria).replace(',','.')):.2f} ; ', end='')
                            sangria_sistema = float(str(sangria).replace(',','.'))
                            if float(sangria) in app.especies and cont < len(app.especies):
                                #print('deu certo especie')
                                cont += 1
                            else:
                                app.excluir_sangria()
                                if float(sangria) in app.brasifort and cont_brasifort < len(app.brasifort):
                                    #print('deu certo brasifort')
                                    app.adicionar_brasifort(sangria, f'{data}')
                                    cont_brasifort += 1

                                elif float(sangria) in app.depositos and cont_dep < len(app.depositos):
                                    #print('deu certo depositos')
                                    app.adicionar_depositos(sangria, f'{data}')
                                    cont_dep += 1
                                
                                elif float(sangria) in app.brinks and cont_brinks < len(app.brinks):
                                    #print('deu certo brinks')
                                    app.adicionar_brinks(sangria, f'{data}')
                                    cont_brinks += 1

                                else:
                                    print('deu erro ao inserir sangria')
                            qtd += 1

                        else:
                            # salva, e pro próximo
                            print('Nenhum valor encontrado!')
                            app.salvar()
                            app.proximo()
                            pdv += 1
                            break
                else:
                    print('Nenhum valor encontrado!')
                    app.salvar()
                    app.proximo()
                    pdv += 1
            else:
                print('Caixa com Pendência!')
                app.proximo()
                pdv += 1

                    

                
                    