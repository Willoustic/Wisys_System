import pyautogui as px
from NF.Arquivo.get_arquivo_ticket import Arquivo_Ticket
from PDV_Automatico.processos import imagens, Img
import pyperclip as pc
from time import sleep
import os
import pandas as pd
import datetime as dt
from functions.caminho import resource_path



class Cupom():
    def __init__(self):
        self.arq = Arquivo_Ticket()
        self.lista, self.conjuntos = self.arq.get_arquivo()
        self.nome_arquivo = self.arq.get_nome_arquivo()
        self.datas = self.arq.datas()
        self.não_achados = list()
        self.achados = list()
        self.soma = 0
        self.valor_novo = 0
        self.valor_antigo = 0

        self.dados_achados = {'Transação': [], 'Valor da Transação': [], 'Litros': [], 'Combustível': [], 'Data da Transação': [],'Situação': []}
        self.dados = {'Transação': [], 'Valor da Transação': [], 'Litros': [], 'Combustível': [], 'Data da Transação': [],'Situação': []}
        self.dados_na = {'Transação': [], 'Valor da Transação': [], 'Litros': [], 'Combustível': [], 'Data da Transação': [], 'Situação': []}

        os.system('cls')


    def dados_achados_get(self, transação, valor, combustivel, litros, data, situação):
        self.dados_achados['Transação'].append(transação)
        self.dados_achados['Valor da Transação'].append(valor)
        self.dados_achados['Combustível'].append(combustivel)
        self.dados_achados['Litros'].append(litros)
        self.dados_achados['Data da Transação'].append(data)
        self.dados_achados['Situação'].append(situação)       
        
    def dados_na_get(self, transação, valor, combustivel, litros, data, situação):
        self.dados_na['Transação'].append(transação)
        self.dados_na['Valor da Transação'].append(valor)
        self.dados_na['Combustível'].append(combustivel)
        self.dados_na['Litros'].append(litros)
        self.dados_na['Data da Transação'].append(data)
        self.dados_na['Situação'].append(situação)

    def dados_get(self, transação, valor, combustivel, litros, data, situação):
        self.dados['Transação'].append(transação)
        self.dados['Valor da Transação'].append(valor)
        self.dados['Combustível'].append(combustivel)
        self.dados['Litros'].append(litros)
        self.dados['Data da Transação'].append(data)
        self.dados['Situação'].append(situação)


    def criar_relatorio(self):
        self.df_achados = pd.DataFrame(self.dados_achados)
        self.df_na = pd.DataFrame(self.dados_na)
        self.df_dados = pd.DataFrame(self.dados)
        os.makedirs(resource_path('Arquivos', 'Relatórios NF'), exist_ok=True)
        
        contador = 0
        data = str(dt.datetime.today())[:16].replace(':', 'h')
        arquivo_rel = os.path.join('Arquivos', 'Relatórios NF', f'relatorio {data}.xlsx')
        while True:
            if not os.path.exists(arquivo_rel):
                arquivo_rel = arquivo_rel
                with pd.ExcelWriter(arquivo_rel, engine='openpyxl') as writer:
                    #self.df_na.to_excel(writer, sheet_name='Não Achados', index=False)
                    self.df_dados.to_excel(writer, sheet_name='Visão Geral', index=False)
                    #self.df_achados.to_excel(writer, sheet_name='Achados', index=False)
                break
            else:
                arquivo_rel = os.path.join('Arquivos', 'Relatórios NF', f'relatorio {data}_{contador}.xlsx')
                contador += 1

        os.startfile(arquivo_rel)
        self.arq.xls.close()
        self.arq.arquivo.close()



    def verificar_transação(self):
        Bot().digitar_periodo(data_inicial=self.datas[0], data_final=self.datas[-1])
        Bot().digitar_forma_de_pagto()
        Bot().clicar_pesquisar()
        Bot().clicar_setinha()
        px.press('end')
        px.press('enter')
        self.valor_antigo = Bot().verificar_valor_total()

        for transação in self.lista:
            for valores in self.conjuntos:
                try:
                    valor = float(valores[f'{transação}'][0])
                    combustivel = valores[f'{transação}'][1]
                    litragem = float(valores[f'{transação}'][2])
                    data = str(valores[f'{transação}'][3])[0:10]
                except:
                    pass
            
            if '.0' in str(transação)[-2:]: 
                print('Autorização:', str(transação)[:-2], '| Valor: R$', valor , '| ', end='')
                Bot().clicar_campo_valor(str(transação)[:-2])    
            else:
                print(f'Autorização: {transação} | Valor: R$ {float(valor):.2f} | ', end='')
                Bot().clicar_campo_valor(str(transação))

            Bot().clicar_localizar()

            if Bot().verificar_não_localizado() == True:
                print('Não achado!')
                self.dados_na_get(transação, valor, combustivel, litragem, data, situação='Não Achado')
                self.dados_get(transação, valor, combustivel, litragem, data, situação='Não Achado')
                self.não_achados.append(f'Autorização: {transação} | Comb: {combustivel} | Valor: R$ {valor:.2f} | Litragem: {litragem}')
                pass
            else:
                Bot().incluir()
                self.valor_total = Bot().verificar_valor_total()
                diferença_valor_total = float(float(self.valor_total) - float(self.valor_antigo))
                diferenca = diferença_valor_total - valor
                if -1 <= diferenca < 1:
                    self.soma += valor
                    self.valor_antigo = float(self.valor_total)
                    print(f'Achado no valor de R$ {diferença_valor_total:.2f} | Diferença de R$ {(diferenca):.2f} | Soma planilha R$ {float(self.soma):.2f} | Sistema: R$ {float(self.valor_antigo):.2f}')
                    self.dados_achados_get(transação, valor, combustivel, litragem, data, situação='Achado')
                    self.dados_get(transação, valor, combustivel, litragem, data, situação='Achado')
                    self.achados.append(transação)
                else:
                    Bot().clicar_excluir()
                    print(f'Achado no valor de R$ {diferença_valor_total:.2f} | Diferença de R$ {(diferenca):.2f} | Obs: Não é um cupom válido!')
                    self.dados_get(transação, valor, combustivel, litragem, data, situação='Não Achado')
                    self.dados_na_get(transação, valor, combustivel, litragem, data, situação='Não Achado')
                    self.não_achados.append(f'Autorização: {transação} | Comb: {combustivel} | Valor: R$ {valor:.2f} | Litragem: {litragem}' )

        print()
        print('=+' * 20)
        print('Não achados: ', end='')
        if len(self.não_achados) == 0:
            print('Nenhum')
        else:
            print('')
            for i in self.não_achados:
                print(i)

        self.criar_relatorio()
        try:
            self.arq.arquivo.close()
        except:
            pass

    def verificar_transação_4digit(self, digit):
        Bot().digitar_periodo(data_inicial=self.datas[0], data_final=self.datas[-1])
        Bot().digitar_forma_de_pagto()
        Bot().clicar_pesquisar()
        Bot().clicar_setinha()
        print('passou')
        px.press('end')
        px.press('enter')
        self.valor_antigo = Bot().verificar_valor_total()

        for transação in self.lista:
            for valores in self.conjuntos:
                try:
                    valor = float(valores[f'{transação}'][0])
                    combustivel = valores[f'{transação}'][1]
                    litragem = float(valores[f'{transação}'][2])
                    data = str(valores[f'{transação}'][3])[0:10]
                except:
                    pass
            
            if '.0' in str(transação)[-2:]: 
                print('Autorização:', str(transação)[:-2], '| Valor: R$', valor , '| ', end='')
                Bot().clicar_campo_valor(str(transação)[:-2])    
            else:
                print(f'Autorização: {transação} | Valor: R$ {float(valor):.2f} | ', end='')
                Bot().clicar_campo_valor_4digit(str(transação), digit=digit)

            Bot().clicar_localizar()

            if Bot().verificar_não_localizado() == True:
                print('Não achado!')
                self.dados_na_get(transação, valor, combustivel, litragem, data, situação='Não Achado')
                self.dados_get(transação, valor, combustivel, litragem, data, situação='Não Achado')
                self.não_achados.append(f'Autorização: {transação} | Comb: {combustivel} | Valor: R$ {valor:.2f} | Litragem: {litragem}')
                pass
            else:
                Bot().incluir()
                self.valor_total = Bot().verificar_valor_total()
                diferença_valor_total = float(float(self.valor_total) - float(self.valor_antigo))
                diferenca = diferença_valor_total - valor
                if -1 <= diferenca < 1:
                    self.soma += valor
                    self.valor_antigo = float(self.valor_total)
                    print(f'Achado no valor de R$ {diferença_valor_total:.2f} | Diferença de R$ {(diferenca):.2f} | Soma planilha R$ {float(self.soma):.2f} | Sistema: R$ {float(self.valor_antigo):.2f}')
                    self.dados_achados_get(transação, valor, combustivel, litragem, data, situação='Achado')
                    self.dados_get(transação, valor, combustivel, litragem, data, situação='Achado')
                    self.achados.append(transação)
                else:
                    Bot().clicar_excluir()
                    print(f'Achado no valor de R$ {diferença_valor_total:.2f} | Diferença de R$ {(diferenca):.2f} | Obs: Não é um cupom válido!')
                    self.dados_get(transação, valor, combustivel, litragem, data, situação='Não Achado')
                    self.dados_na_get(transação, valor, combustivel, litragem, data, situação='Não Achado')
                    self.não_achados.append(f'Autorização: {transação} | Comb: {combustivel} | Valor: R$ {valor:.2f} | Litragem: {litragem}' )

        print()
        print('=+' * 20)
        print('Não achados: ', end='')
        if len(self.não_achados) == 0:
            print('Nenhum')
        else:
            print('')
            for i in self.não_achados:
                print(i)

        self.criar_relatorio()
        self.arq.xls.close()
        self.arq.arquivo.close()


class Bot():
    def __init__(self):
        self.pasta = imagens('NF')


    def clicar_setinha(self):
        setinha = self.pasta.join('setinha.png')
        Img.click(setinha, 0.9)
    
    
    def clicar_campo_valor_4digit(self, aut, digit):
        campo_valor = self.pasta.join('campo_valor.png')
        x, y, = Img.coordenadas(campo_valor, 0.9)
        px.doubleClick(x+100, y)
        px.write(str(aut)[-int(digit):], interval=0)


    def clicar_campo_valor(self, aut):
        campo_valor = self.pasta.join('campo_valor.png')
        x, y, = Img.coordenadas(campo_valor, 0.9)
        px.doubleClick(x+100, y)
        px.write(str(aut), interval=0)


    def clicar_localizar(self):
        localizar_button = self.pasta.join('localizar_button.png')
        Img.click(localizar_button, 0.9)


    def verificar_não_localizado(self):
        verificar = self.pasta.join('verificar.png')
        sleep(2)
        bool_teste = Img.verifica_na_tela(verificar, 0.9)
        if bool_teste == True:
            Img.click(verificar, 0.9)
            px.press('enter')

        return bool_teste


    def incluir(self):
        incluir_button = self.pasta.join('incluir_button.png')
        Img.click(incluir_button, 0.9)


    def clicar_ok(self):
        ok_button = self.pasta.join('ok_button.png')
        Img.click(ok_button, 0.9)


    def clicar_excluir(self):
        excluir_button = self.pasta.join('excluir_button.png')
        Img.click(excluir_button, 0.9)


    def verificar_valor_total(self):
        campo_valor = self.pasta.join('cupom_selecionado.png')
        x, y = Img.coordenadas(campo_valor, 0.9)

        px.doubleClick(x+203, y-3)
        sleep(0.5)
        px.hotkey('ctrl', 'c')
        sleep(0.5)
        valor_encontrado = pc.paste().replace(',', '.')

        return valor_encontrado


    def digitar_periodo(self, data_inicial, data_final):
        periodo = self.pasta.join('periodo.png')
        x, y = Img.coordenadas(periodo, 0.9)
        px.click(x+50, y)
        px.write(str(data_inicial))
        px.write(str(data_final))


    def digitar_forma_de_pagto(self):
        form_pgto = self.pasta.join('form_pgto.png')
        x, y = Img.coordenadas(form_pgto, 0.9)
        px.click(x+99, y)
        px.write('4')
        px.press('enter')


    def clicar_pesquisar(self):
        pesquisar = self.pasta.join('pesquisar.png')
        vazio = self.pasta.join('vazio.png')

        Img.click(pesquisar, 0.9)
        Img.verificar_até_sair(vazio, 0.9)
