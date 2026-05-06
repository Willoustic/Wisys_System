import pyautogui as px
import os
from time import sleep

class Extra_excel():
    def __init__(self, arquivo):
        # Pegar arquivo
        self.arquivo = arquivo
        print(self.arquivo)
        # Iniciar Arquivo
        os.startfile(self.arquivo)

        # Comandos 
        self.esperar_o_excel_abrir()
        self.transformar_em_tabela()
        self.fazer_resumo()
        self.criar_tabela()
        sleep(1)
        self.transf_tabel_contabil()
        self.pintar_celulas()
        self.ajeitar_planilha()
        self.voltar_inicio()
        self.ajeitar_valores()
        sleep(1)
        self.salvar()
        sleep(2)
        self.fechar()


    def esperar_o_excel_abrir(self):
        sleep(3)

    def transformar_em_tabela(self):
        px.press('alt')
        px.write('tta')
        px.press('enter')

    def fwrite(self, write):
        px.press('tab')
        px.write(write)
        px.press('enter')

    def fazer_resumo(self):
        sleep(1)
        px.hotkey('ctrl', 'home')
        px.press('right')
        px.press('right')
        px.hotkey('ctrl', 'down')
        px.press('down')
        px.hotkey('alt', '=')
        px.hotkey('ctrl', 'z')
        self.fwrite('CARTOES')
        px.write('0')
        self.fwrite('DEPOSITOS')
        px.write('0')
        self.fwrite('DIF DE CAIXA')
        px.write('0')
        self.fwrite('NOTAS A PRAZO')
        px.write('0')
        self.fwrite('SANGRIAS')
        px.write('=soma(')
        px.press('up')
        px.write(':')
        for i in range(0, 4):
            px.press('up')
        px.write(')')
        px.press('tab')
        px.write('TOTAL')
        px.press('enter')

    # fazer tabela no resumo e transformar em contabil
    def criar_tabela(self):
        px.press('up')
        px.hotkey('ctrl', 't')
        px.press('alt')
        px.write('cbt')

    def transf_tabel_contabil(self):
        px.press('alt')
        px.write('can')
        px.press('enter')

    def pintar_celulas(self):
        px.hotkey('ctrl', 'down')
        px.hotkey('ctrl', 'down')
        px.hotkey('ctrl', 'up')

        px.press('alt')
        px.write('cr')
        px.press('right')
        px.press('enter')

        px.press('alt')
        px.write('cfc')
        px.press('down')
        px.press('enter')

        px.hotkey('ctrl', 'c')
        px.press('right')
        px.hotkey('ctrl', 'v')
        sleep(0.5)
        px.press('ctrl')
        px.write('ff')
        px.press('enter')
        px.press('esc')

    def voltar_inicio(self):
        px.hotkey('ctrl', 'home')
        px.hotkey('ctrl', 'home')

    def ajeitar_valores(self):
        px.press('right')
        px.press('right')
        px.press('down')
        px.hotkey('ctrl', 't')
        sleep(0.5)
        px.press('ctrl')
        sleep(0.5)
        px.press('down')
        px.press('enter')

    def ajeitar_planilha(self):
        px.hotkey('ctrl', 't')
        px.hotkey('ctrl', 't')
        px.press('alt')
        px.write('cot')

    def salvar(self):
        px.hotkey('ctrl', 'b')

    def fechar(self):
        px.hotkey('alt', 'f4')



