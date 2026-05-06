import pyautogui as px
from PDV_Automatico.processos import *
import pyperclip as pyc

class Contas_a_pagar():
    def __init__(self, data, banco):
        self.data = data
        self.banco = banco
        self.ad = imagens('CaP')
        self.configure_bot()
        
# config geral
    def configure_bot(self):
        self.get_n_titulo()
        self.clicar_liquidação()
        self.clicar_banco()
        self.digitar_data()
        self.pegar_valor_liquid()
        self.digitar_documento()
        self.escolher_banco()
        self.pegar_rs_valor()
        self.liquidar_fatura()


# ações
    def get_n_titulo(self):
        pyc.copy('')
        n_titulo = self.ad.join(arquivo='n_titulo.png')
        x, y = Img.coordenadas(n_titulo, 0.9)
        px.doubleClick(x+50, y)
        sleep(0.2)
        px.hotkey('ctrl', 'c')
        self.doc = pyc.paste()


    def clicar_liquidação(self):
        liquid_aba = self.ad.join('liquid.png')
        Img.click(liquid_aba, 0.9)


    def clicar_banco(self):
        banco_aba = self.ad.join('banco_aba.png')
        Img.click(banco_aba, 0.9)

    def digitar_data(self):
        data_liquid = self.ad.join('data_liquid.png')
        x, y = Img.coordenadas(data_liquid, 0.9)
        px.click(x+40, y+20)
        px.write(str(self.data))

    def pegar_valor_liquid(self):
        valor_liquid = self.ad.join('valor_liquid.png')
        x, y = Img.coordenadas(valor_liquid, 0.9)
        px.click(x+153, y)

    def pegar_rs_valor(self):
        rs_valor = self.ad.join('rs_valor.png')
        x, y = Img.coordenadas(rs_valor, 0.9)
        px.click(x+135, y)

    def digitar_documento(self):
        documento = self.ad.join('documento.png')
        x, y = Img.coordenadas(documento, 0.9)
        px.click(x+80, y)
        px.write(self.doc)

    def escolher_banco(self):
        mnemonico = self.ad.join('mnemonico.png')
        x, y = Img.coordenadas(mnemonico, 0.9)
        px.click(x+50, y)
        px.write(str(self.banco))
        px.press('tab')

    def liquidar_fatura(self):
        liquidar = self.ad.join('liquidar.png')
        Img.click(liquidar, 0.9)