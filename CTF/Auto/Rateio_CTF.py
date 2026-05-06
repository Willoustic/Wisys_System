import pyautogui as px
from time import sleep
import shutil, os
from pyperclip import paste
from PDV_Automatico.processos import Img, imagens_Emsys, imagens_pdv
from PDV_Automatico.pdv import Caixa
import pyperclip as pc

def rateio_ctf():
    pst = imagens_pdv('rateio_ctf')
    proximo = pst.join('proximo.png')
    responsaveis = pst.join('responsaveis.png')
    salvar = pst.join('salvar.png')
    salvo = pst.join('salvo.png')
    ultimo_Caixa = pst.join('ultimo_Caixa.png')
    valor_rateio = pst.join('valor_rateio.png')
    valor_a_ratear = pst.join('valor_a_ratear.png')
    incluir_icon = pst.join('incluir_icon.png')
    incluir_rateio = pst.join('incluir_rateio.png')
    incluir_app = pst.join('incluir_app.png')
    #on_proximo = pst.join('on_proximo.png') #obsoleto
    posto = pst.join('1661.png')
    excluir = pst.join('excluir.png')
    excluir_registro = pst.join('excluir_registro.png')
    pendencia = imagens_pdv('pendencia').join('pendencia.png')
    cont = 1
    while True:

        if cont > 1:
            Caixa.clicar_resumo()

        cont += 1

        if Img.verifica_na_tela(ultimo_Caixa, precisão=0.99) == True:
            break

        if Img.verifica_na_tela(pendencia, precisão=0.99) == True:
            Img.click(proximo, precisão=0.9)
        else:
            sleep(0.5)
            #responsaveis
            Img.click(responsaveis, precisão=0.99)
            #rateio
            Img.verificar_até_achar(valor_rateio, precisão=0.9)
            if Img.verifica_na_tela(valor_rateio, precisão=0.9) == True:
                if Img.verifica_na_tela(posto, precisão=0.9):
                    Img.click(posto, 0.9)
                    Img.click(excluir, 0.9)
                    Img.click(excluir_registro, 0.9)
                    px.write('y')
                    sleep(1)

                rateio_x, rateio_y = Img.coordenadas(valor_rateio, 0.9)
                rateio = pc.copy('')
                px.doubleClick(rateio_x+130, rateio_y)
                px.hotkey('ctrl', 'c')
                rateio = pc.paste()
                print("Caixa Nº", cont-1, ":",  rateio)

                if str(rateio) != '0':
                    #incluir
                    Img.click(incluir_rateio, precisão=0.9)

                    Img.verificar_até_achar(incluir_app, precisão=0.9)
                    ratear_x, ratear_y = Img.coordenadas(valor_a_ratear, precisão=0.9)
                    px.click(ratear_x+100, ratear_y)
                    px.write(rateio)
                    px.press('tab')
                    # inserir codigo 1661
                    px.write('1661')
                    px.press('enter')
                    #observarção
                    px.press('tab')
                    px.write('REF A VENDA CTF')
                    #incluir
                    Img.click(incluir_icon, precisão=0.9)
                    Img.click(incluir_app, precisão=0.9)
                    #fechar aba:
                    px.hotkey('alt', 'f4')
                    Img.verificar_até_sair(incluir_app, precisão=0.9)

            #clicar salvar
            Img.click(salvar, precisão=0.9)
            Img.verificar_até_achar(salvo, precisão=0.9)
            px.press('enter')

            Img.click(proximo, precisão=0.9)
        
            
