import os
import pyautogui as px
from time import sleep
import sys
import mss
import pyscreeze
from PIL import Image
from pyscreeze import Box

MONITOR_ALVO = 0  # 1 = primeiro monitor, 2 = segundo, 0 = todos juntos


def listar_monitores():
    """Rode uma vez para ver qual número é cada monitor."""
    with mss.mss() as sct:
        for i, m in enumerate(sct.monitors):
            print(i, m)


def localizar(imagem, precisão, monitor=None):
    monitor = MONITOR_ALVO if monitor is None else monitor
    with mss.mss() as sct:
        mon = sct.monitors[monitor]
        shot = sct.grab(mon)

    tela = Image.frombytes('RGB', shot.size, shot.rgb)
    box = pyscreeze.locate(imagem, tela, confidence=precisão)
    if box is None:  # versões antigas do pyscreeze retornam None
        raise LookupError('Imagem não encontrada')

    # Converte da posição dentro do monitor para a posição real na tela
    return Box(box.left + mon['left'], box.top + mon['top'], box.width, box.height)


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
                achar = localizar(imagem, precisão)
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
                achar = localizar(imagem, precisão)
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
                achar = localizar(imagem, precisão)
                #print(f'Procurando Img:', imagem)
            except Exception as e:
                pass
            else:
                #print('achou')
                break

    def verifica_na_tela(imagem, precisão):
        try: 
            achar = localizar(imagem, precisão)
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
                achar = localizar(imagem, precisão)
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
                achar = localizar(imagem, precisão)
                #print(f'Procurando Img:', imagem)
            except Exception as e:
                pass
            else:
                #print('achou')
                center = px.center(achar)
                return center.x, center.y