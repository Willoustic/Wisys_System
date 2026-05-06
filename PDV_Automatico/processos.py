import os
import pyautogui as px
from time import sleep
import sys

class imagens_pdv():
    def __init__(self, pasta):
        self.pasta = pasta
        
    def join(self, arquivo):
        arquivo_mudado = os.path.join('Images', 'PDV_Automatico', f'{self.pasta}', f'{arquivo}')
        return arquivo_mudado

class imagens():
    def __init__(self, *pasta):
        self.pasta = pasta

    def join(self, arquivo):
        arquivo_mudado = os.path.join('Images', *self.pasta, f'{arquivo}')
        return arquivo_mudado
    
class imagens_Emsys():
    def join(self, arquivo):
        arquivo_mudado = os.path.join('Images', 'Emsys', f'{arquivo}')
        return arquivo_mudado

def cancelar_operacao():
    sleep(0.1)
    try:
        px.moveTo()
    except:
        x = False
    else:
        x = True

    return x


class Img:    
    def click(imagem, precisão):
        while True:
            try: 
                x = cancelar_operacao()
                if not x:
                    break
                achar = px.locateOnScreen(imagem, confidence=precisão)
                #print(f'Procurando Img:', imagem)
                
            except Exception as e:
                pass
            else:
                #print('achou')
                center = px.center(achar)
                #print(center)
                px.click(center.x, center.y, duration=0.1)
                #print('clicou')
                break

    def DoubleClick(imagem, precisão):
        while True:
            try: 
                x = cancelar_operacao()
                if not x:
                    break
                achar = px.locateOnScreen(imagem, confidence=precisão)
                #print(f'Procurando Img:', imagem)
            except Exception as e:
                pass
            else:
                #print('achou')
                center = px.center(achar)
                px.doubleClick(center.x, center.y, duration=0.1)
                break

    def verificar_até_achar(imagem, precisão):
        while True:
            try: 
                x = cancelar_operacao()
                if not x:
                    break
                achar = px.locateOnScreen(imagem, confidence=precisão)
                #print(f'Procurando Img:', imagem)
            except Exception as e:
                pass
            else:
                #print('achou')
                break

    def verifica_na_tela(imagem, precisão):
        try: 
            achar = px.locateOnScreen(imagem, confidence=precisão)
            #print(f'Procurando Img:', imagem)
        except Exception as e:
            pass
            return False
        else:
            #print('achou')
            return True
        
    def verificar_até_sair(imagem, precisão):
        while True:
            try: 
                x = cancelar_operacao()
                if not x:
                    break
                achar = px.locateOnScreen(imagem, confidence=precisão)
                #print(f'Procurando Img:', imagem)
            except Exception as e:
                #print('não achou')
                pass
                break
            else:
                #print('achou)
                pass
                
    def coordenadas(imagem, precisão):
        while True:
            try: 
                x = cancelar_operacao()
                if not x:
                    break
                achar = px.locateOnScreen(imagem, confidence=precisão)
                #print(f'Procurando Img:', imagem)
            except Exception as e:
                pass
            else:
                #print('achou')
                center = px.center(achar)
                return center.x, center.y
