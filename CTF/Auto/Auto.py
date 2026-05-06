import pyautogui as px
from time import sleep
import ctypes
from PDV_Automatico.pdv import Caixa
from PDV_Automatico.processos import *
import pyperclip as pc
import pandas as pd
import datetime as dt

def caps_lock_ativado():
    # 0x14 é o código da tecla Caps Lock
    return bool(ctypes.WinDLL("User32.dll").GetKeyState(0x14) & 1)


class Caixa_CTF():
    def __init__(self, lista):
        # caixas a verificar
        self.inicial = 1
        self.lista = lista
        self.qtd = len(lista)
        self.operadores = []
        self.pst = imagens_pdv('ctf')
        self.dados = {'Placa': [], 'Valor': [], 'Operador': [], 'Situação': []}

    def dados_get(self, placa, valor, operador, situação):
        self.dados['Placa'].append(placa)
        self.dados['Valor'].append(valor)
        self.dados['Operador'].append(operador)
        self.dados['Situação'].append(situação)

    def criar_relatorio(self):
        self.df_dados = pd.DataFrame(self.dados)
        os.makedirs('Relatorios CTF', exist_ok=True)
        
        contador = 1
        data = str(dt.datetime.today())[:16].replace(':', 'h')
        arquivo_rel = os.path.join('Relatorios CTF', f'relatorio ctf {data}.xlsx')
        while True:
            if not os.path.exists(arquivo_rel):
                arquivo_rel = arquivo_rel
                with pd.ExcelWriter(arquivo_rel, engine='openpyxl') as writer:
                    #self.df_na.to_excel(writer, sheet_name='Não Achados', index=False)
                    self.df_dados.to_excel(writer, sheet_name='Visão Geral', index=False)
                    #self.df_achados.to_excel(writer, sheet_name='Achados', index=False)
                break
            else:
                arquivo_rel = os.path.join('Relatorios CTF', f'relatorio ctf {data}_{contador}.xlsx')
                contador += 1

        os.startfile(arquivo_rel)

    def inicial_inside(self):
        
        operador = self.pst.join('operador.png')
        
        print('=+'*30)
        print('')
        print(f'Placas a pesquisar: {self.qtd}')
        pc.copy('')
        sleep(0.5)
        #pegar operador
        operador_x, operador_y = Img.coordenadas(operador, precisão=0.9)
        px.doubleClick(operador_x+90, operador_y)
        self.operador_cod = pc.copy('')
        px.hotkey('ctrl', 'c')
        self.operador_cod = pc.paste()
        print(self.operador_cod)


        print('Operador:', self.operador_cod)


    def ir_ate_cartao(self):
        
        recebimento = self.pst.join('recebimento.png')
        duplicatas = self.pst.join('duplicatas.png')
        cartoes = self.pst.join('cartoes.png')
        setinha = self.pst.join('setinha.png')
        cod_sacado = self.pst.join('cod_sacado.png')
        hora = self.pst.join('hora.png')
        nome_sacado = self.pst.join('nome_sacado.png')

        if self.inicial == 1:
            # clicar + recebimento
            while Img.verifica_na_tela(duplicatas, 0.9) == False:
                Img.DoubleClick(recebimento, 0.9)
                break

            sleep(0.5)
            #clicar em duplicatas
            while Img.verifica_na_tela(cartoes, 0.9) == False:
                Img.DoubleClick(duplicatas, 0.9)
                break

            # cartão de crédito
            Img.click(cartoes, 0.9)
            sleep(1)
            # clicar na setinha do campo
            Img.click(setinha, 0.9)
            sleep(0.2)
            # digitar 'C' para ir para "Código Sacado"
            px.write('C')
            px.press('enter')
            sleep(0.2)
            
            # IR ATE A TABELA
            tab = 5
            for i in range(0,tab):
                px.hotkey('shift', 'tab')

            for i in range(0,13):
                px.hotkey('left')

            while Img.verifica_na_tela(nome_sacado, 0.99) == False:
                px.press('right')
            
            Img.click(nome_sacado, 0.9)
            sleep(0.5)
            Img.click(cod_sacado, 0.9)
            sleep(0.5)
        else:
            Img.click(recebimento, 0.9)
            sleep(0.5)


    def auto_ctf(self):
        alterar_button = self.pst.join('alterar_button.png')
        valor_campo = self.pst.join('valor_campo.png')
        localizar_button = self.pst.join('localizar_button.png')
        alterar_warning = self.pst.join('alterar_warning.png')
        alterar_duplicata = self.pst.join('alterar_duplicata.png')
        sacado_cod = self.pst.join('sacado_cod.png')
        aut_cod = self.pst.join('aut_cod.png')
        valor_cupom = self.pst.join('valor_cupom.png')
        incluir = self.pst.join('incluir.png')
        erro = self.pst.join('erro.png')
        
        def alterar():
                Img.click(alterar_button, 0.9)
                sleep(0.5)

        self.diferencas = list()

        cont = 1
        aut_antiga = ''
        valor_antigo = ''
        while True:

            if Img.verifica_na_tela(alterar_button, 0.99) == False:
                print(f'Quantidade de CTF ACHADO: {cont-1}')
                return False

            if cont == 1:
                #clicar no campo valor
                sleep(0.5)
                Img.click(valor_campo, 0.9)
                sleep(0.5)
                #digitar o código do ctf
                px.write('1073', interval=0.01)
                sleep(0.5)
                #clicar em pesquisar
                Img.click(localizar_button, 0.9)
                sleep(0.3)
                #caso não for encontrado (tratamento de erros)
                px.press('enter')
                sleep(0.5)

            if cont > 1:
                Img.verificar_até_achar(localizar_button, 0.9)
                Img.click(localizar_button, 0.9)
                # IR ATE A TABELA
                tab = 3
                for i in range(0,tab):
                    px.hotkey('shift', 'tab')
                px.press('down')

            alterar()
            sleep(0.5)
            #clicar no yes de warning
            while Img.verifica_na_tela(alterar_warning, 0.9) == False:
                if Img.verifica_na_tela(alterar_duplicata, 0.9) == False:
                    pass
                else:
                    break
            
            if Img.verifica_na_tela(alterar_warning, 0.9) == True:
                px.write('y')
                sleep(0.5)
                #clicar ok para desbugar
                """px.press('enter')
                sleep(0.5)"""
                Img.verificar_até_achar(alterar_duplicata, 0.9)
                sleep(0.5)
                
            #clicar no sacado
            sac = Img.verifica_na_tela(sacado_cod, 0.9)
            
            # verificar se é ctf
            
            if sac == True:
                #clicar na autorização
                x1, y1 = Img.coordenadas(aut_cod, 0.9)
                px.doubleClick(x1+75, y1)
                sleep(0.5)
                px.hotkey('ctrl', 'c')
                sleep(0.5)
                aut = pc.paste()
                #clicar no valor
                x1, y1 = Img.coordenadas(valor_cupom, 0.9)
                px.doubleClick(x1+75, y1)
                sleep(0.5)
                px.hotkey('ctrl', 'c')
                sleep(0.5)
                valor_novo = pc.paste()
                # verificar se tem virgula no valor
                if ',' in valor_novo:
                    valor_novo = valor_novo.replace(',', '.')
                    valor_novo = float(valor_novo)

                if str(aut) == str(aut_antiga):
                    if str(valor_novo) == str(valor_antigo):
                        condição = False
                        px.click(x1+400, y1)
                        Img.verificar_até_sair(alterar_duplicata, 0.9)   
                        print(f'Quantidade de CTF ACHADO: {cont-1}')
                        return False
                else:
                    self.diferencas = list()
                    condição = True
                    for placa in self.lista:
                        if aut.upper() == str(placa['Placa']).upper():
                            diferenca = float(placa['Valor']) - float(valor_novo)
                            diferenca = float(f'{diferenca:.2f}')
                            if float(diferenca) < 50 and float(diferenca) > -50:
                                #adicionar nome do operador na coluna ao lado da placa
                                placa['Operador'] = self.operador_cod
                                if self.operador_cod in self.operadores:
                                    pass
                                else:
                                    self.operadores.append(self.operador_cod)

                                px.write(str(placa['Valor']).replace('.', ','), interval=0.01)
                                valor_antigo = str(placa['Valor'])
                                aut_antiga = aut
                                self.diferencas.append(diferenca)
                                placa['Diferenca'] = diferenca
                                print(f'Operador: {self.operador_cod} // Valor na planilha {placa['Valor']}')
                                print(f'Placa: {placa['Placa']} // Valor no sistema {valor_novo}')
                                self.qtd -= 1
                                condição = True
                                break

                if condição == True:
                    sleep(0.3)
                    #clicar em incluir
                    Img.DoubleClick(incluir, 0.9)
                    #sleep(2)
                    Img.verificar_até_sair(alterar_duplicata, 0.9)
                    cont += 1

                else:
                    #fechar a 'alterar duplicata'
                    x1, y1 = Img.coordenadas(alterar_duplicata, 0.9)
                    sleep(0.3)
                    px.doubleClick(x1+400, y1)
                    #sleep(3)
                    Img.verificar_até_sair(alterar_duplicata, 0.9)
                    
                    
            else:
                #fechar a 'alterar duplicata'
                x1, y1 = Img.coordenadas(alterar_duplicata, 0.9)
                sleep(0.3)
                px.doubleClick(x1+400, y1)
                #sleep(3)
                Img.verificar_até_sair(alterar_duplicata, 0.9)

                print(f'Quantidade de CTF ACHADO: {cont-1}')
                return False
               

    def relatorio_ctf_individual(self):
            #repita o processo
            print('')
            print(f'Operador {self.inicial}º: {self.operador_cod} finalizado.')

            diferencas_caixas = list()
            for dados in self.lista:
                if self.operador_cod == dados['Operador']:
                    try:
                        diferencas_caixas.append(dados['Diferenca'])
                    except:
                        print('Não existe diferença')

            try:
                print(f'Com a diferença total de {sum(diferencas_caixas):.2f}')
            except:
                print('Não existe diferença')

            print("")
            

    def relatorio_ctf_total(self):

        for op in self.operadores:
            print(f'Operador: {op}')
            diferencas_caixas = list()
            for dados in self.lista:
                if op == dados['Operador']:
                    try:
                        diferencas_caixas.append(dados['Diferenca'])
                    except:
                        print('Não existe diferença')
                    print(f'Aut: {dados['Placa']} // Valor mudado: {dados['Valor']} // Diferença total: {dados['Diferenca']}')
                    self.dados_get(placa=dados['Placa'], valor=dados['Valor'], operador=dados['Operador'], situação='Achado')
            try:
                print(f'Com a diferença total de {sum(diferencas_caixas):.2f}')
            except:
                print('Não existe diferença')
            
            print('=+' * 20, '=')
            print('')
        

        contador = 0
        print('Valores não achados:')
        for dados in self.lista:
            if dados['Operador'] == '':
                print(f'Aut: {dados['Placa']} // Valor: {dados['Valor']}')
                self.dados_get(placa=dados['Placa'], valor=dados['Valor'], operador='', situação='Não achado')
                contador += 1

        self.criar_relatorio()

        print(f'Qtd de autorização não achada: {contador}')
        print('=+' * 20)
        print('')


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
        self.inicial += 1


class CTF():

    def mudar(vendas):
        pdvs = Caixa_CTF(vendas)
        cont = 1
        while True:
            if cont > 1:
                Caixa.clicar_resumo()
            cont += 1
            ultimo_caixa = imagens_pdv('rateio').join('ultimo_Caixa.png')
            pendencia = imagens_pdv('pendencia').join('pendencia.png')

            if Img.verifica_na_tela(ultimo_caixa, 0.98) == True:
                break

            if Img.verifica_na_tela(pendencia, 0.98) == True:
                pdvs.proximo()
                sleep(0.5)
            else:
                pdvs.inicial_inside()
                pdvs.ir_ate_cartao()
                pdvs.auto_ctf()
                sleep(0.5)
                pdvs.salvar()
                pdvs.relatorio_ctf_individual()        
                sleep(0.5)
                pdvs.proximo()
                sleep(0.5)
            
        pdvs.relatorio_ctf_total()
        print('Fim da execução!')



