from CTF.Auto.Auto import CTF
from CTF.Auto_Planilha.Verificar_Planilha import *
from time import sleep
from CTF.Auto.Rateio_CTF import rateio_ctf
import pyautogui as px
from PDV_Automatico.processos import Img, imagens_Emsys, imagens_pdv

class Auto_CTF():
    def run(cartoes):
        pst = imagens_pdv('voltar')
        voltar = pst.join('voltar.png')

        CTF.mudar(cartoes)
        sleep(1)

        # voltar do inicio
        Img.click(voltar, 0.99)
        sleep(1)
        rateio_ctf()