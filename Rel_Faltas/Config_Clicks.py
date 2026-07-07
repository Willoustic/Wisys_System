from .Load_Nomes import nomes
from os.path import join, expanduser
from PDV_Automatico.processos import imagens, Img
from functions.chrome import abrir_chrome
from functions.verificar_site_aberto import verificar_pagina_aberta
from datetime import datetime
import pyautogui as px
from time import sleep

def ajuste_data(data):
    data = datetime.today().month
    
    if len(str(data)) < 2:
        data = f'0{data}'

    return data

def get_mes_anterior(mes: int):
    if (mes == 1):
        mes_anterior = 12
    else:
        mes_anterior = (mes - 1)

    if len(str(mes_anterior)) < 2:
        mes_anterior = f'0{mes_anterior}'

    return mes_anterior

def get_ano_inicial(mes, ano_atual):
    if (mes == 1):
        ano_inicial = ano_atual - 1
    else:
        ano_inicial = ano_atual

    return ano_inicial


class Clicks_Sistema():
    def __init__(self, cod_posto):
        self.cod_posto = cod_posto
        self.pasta = imagens('Faltas')
  
        dia = datetime.today().day
        mes = datetime.today().month
        ano = datetime.today().year

        self.DIA_ATUAL = ajuste_data(dia)
        self.MES_ATUAL = ajuste_data(mes)
        self.MES_ANTERIOR = get_mes_anterior(mes)
        self.ANO_ATUAL = ano
        self.ANO_INICIAL = get_ano_inicial(mes, ano)


    def clicar_administrativo(self):
        adm = self.pasta.join('adm.png')
        Img.click(adm, 0.9)


    def clicar_funcionarios(self):
        funcionarios = self.pasta.join('funcionarios.png')
        Img.click(funcionarios, 0.9)


    def clicar_relatorios(self):
        rel_func = self.pasta.join('rel_func.png')
        Img.click(rel_func, 0.9)


    def clicar_rel_movimento(self):
        relmovfunc = self.pasta.join('relmovfunc.png')
        Img.click(relmovfunc, 0.9)


    def esperar_rel_mov(self):
        abarelmov = self.pasta.join('abarelmov.png')
        Img.verificar_até_achar(abarelmov, 0.9)
        Img.click(abarelmov, 0.9)


    def digitar_data(self):
        inicial = self.pasta.join('inicial.png')
        x, y = Img.coordenadas(inicial, 0.9)

        px.click(x+50, y)
        px.write(f'26{self.MES_ANTERIOR}{self.ANO_INICIAL}')
        px.write(f'{self.DIA_ATUAL}{self.MES_ATUAL}{self.ANO_ATUAL}')


    def selecionar_tipo_pdf(self):
        gerar_em = self.pasta.join('gerar_em.png')
        select_tela = self.pasta.join('select_tela.png')
        select_pdf = self.pasta.join('select_pdf.png')

        x, y = Img.coordenadas(gerar_em, 0.9)
        px.click(x+100, y)
        Img.verificar_até_achar(select_pdf, 0.9)
        Img.click(select_pdf, 0.9)


    def clicar_confirmar(self):
        confirmar = self.pasta.join('confirmar.png')
        Img.click(confirmar, 0.9)


    def esperar_a_tela_salvar(self):
        salvar_arq = self.pasta.join('salvar_arq.png')
        Img.verificar_até_achar(salvar_arq, 0.9)


    def digitar_nome_do_arquivo(self):
        nome_arq = self.pasta.join('nome_arq.png')
        caminho = str(join(expanduser("~"), 'Downloads'))
        self.nome_arquivo = f'FALTAS DO DIA 26.{self.MES_ANTERIOR} ATE {self.DIA_ATUAL}.{self.MES_ATUAL} - POSTO {self.cod_posto}'

        x, y = Img.coordenadas(nome_arq, 0.9)
        px.doubleClick(x+200, y)
        px.press('del')
        px.write(caminho)
        px.press('enter')
        sleep(1)
        px.write(self.nome_arquivo)


    def clicar_salvar(self):
        salvar_button = self.pasta.join('salvar_button.png')
        Img.click(salvar_button, 0.9)


    def fechar_relmov(self):
        px.hotkey('alt', 'f4')
    
    
    def config_all(self):
        self.clicar_administrativo()
        self.clicar_funcionarios()
        self.clicar_relatorios()
        self.clicar_rel_movimento()
        self.esperar_rel_mov()
        self.digitar_data()
        self.selecionar_tipo_pdf()
        self.clicar_confirmar()
        self.esperar_a_tela_salvar()
        self.digitar_nome_do_arquivo()
        self.clicar_salvar()
        self.esperar_rel_mov()
        self.fechar_relmov()


def pesquisar(texto: str):
    px.hotkey('ctrl', 'f')
    px.write(texto)
    px.press('enter')
    px.press('esc')


class MsgToWhatsapp():
    def __init__(self, cod_posto, arquivo):
        self.cod_posto = cod_posto
        self.nome = nomes[str(cod_posto)]
        self.nome_arquivo = arquivo


    def abrir_whatsapp(self):
        abrir_chrome('web.whatsapp.com')
        verificar_pagina_aberta()


    def pesquisar_selecionar_nome(self):
        pesquisar('pesquisar')
        px.press('tab')
        px.hotkey('shift', 'tab')

        px.write(str(self.nome))
        px.press('enter')
        sleep(2)

    def abrir_aba(self):
        pesquisar('digite')
        for i in range(0, 3):
            px.hotkey('shift', 'tab')
        sleep(2)

        px.press('space')
        pesquisar('documento')

        px.press('enter')
        sleep(3)


    def selecionar_arquivo(self):
        caminho = str(join(expanduser("~"), 'Downloads'))
        px.write(caminho)
        px.press('enter')
        sleep(1)
        px.write(self.nome_arquivo)
        sleep(1)
        px.press('enter')
    
    def enviar_arquivo(self):
        sleep(1)
        px.write(self.nome_arquivo)
        sleep(0.5)
        px.press('enter')

    def config(self):
        self.abrir_whatsapp()
        self.pesquisar_selecionar_nome()
        self.abrir_aba()
        self.selecionar_arquivo()
        self.enviar_arquivo()
