import pyautogui as px
from time import sleep
import pyperclip as pc
from PDV_Automatico.processos import imagens, Img

class Nota():
    def __init__(self):
        self.pst = imagens('NF')

    def verificar_NOP(self):
        nop_errado = self.pst.join('nop_errado.png')
        nop_certo = self.pst.join('nop_certo.png')

        if Img.verifica_na_tela(nop_errado, 0.99) == True:
            Img.click(nop_errado, 0.99)
            Img.click(nop_certo, 0.99)


    def clicar_gerar_nota(self):
        gerar_nota = self.pst.join('gerar_nota.png')
        confirm_nota = self.pst.join('confirm_nota.png')
        confirm_transmitir = self.pst.join('confirm_transmitir.png')

        Img.click(gerar_nota, 0.9)
        Img.verificar_até_achar(confirm_nota, 0.9)
        Img.click(confirm_nota, 0.9)
        px.press('enter')

        Img.verificar_até_achar(confirm_transmitir, 0.9)
        Img.click(confirm_transmitir, 0.9)
        px.press('enter')


    def pegar_dados_nota(self):
        numero_serie = self.pst.join('numero_serie.png')
        gerenc_nfe = self.pst.join('gerenc_nfe.png')

        pc.copy('')
        Img.verificar_até_achar(gerenc_nfe, 0.89)
        x, y = Img.coordenadas(numero_serie, 0.9)
        px.click(x, y+15)
        px.hotkey('ctrl', 'c')
        copia = pc.paste()
        copia = copia.split()

        """for i, a in enumerate(copia):
            print(i, a)"""

        nr_nota = copia[20]
        nome_nota = copia[24]
        valor_nota = copia[-6]

        #print(nome_nota, valor_nota)
        return nr_nota, nome_nota, valor_nota


    def transmitir(self):
        transmitir_nfe = self.pst.join('transmitir_nfe.png')
        opera_conc = self.pst.join('opera-conc.png')
        emi_cod_sit = self.pst.join('emissao_cod_sit.png')
        fechar_transm = self.pst.join('fechar_transm.png')

        Img.click(transmitir_nfe, 0.9)
        Img.verificar_até_achar(opera_conc, 0.9)
        Img.click(opera_conc, 0.9)
        px.press('enter')
        Img.verificar_até_achar(emi_cod_sit, 0.9)
        Img.click(fechar_transm, 0.9)


    def exportar_nfe(self):
        exportar_nfe = self.pst.join('exportar_nfe.png')
        escolha_arq = self.pst.join('escolha_arq.png')
        downloads = self.pst.join('downloads.png')
        gerenc_nfe = self.pst.join('gerenc_nfe.png')
        export_ok = self.pst.join('export_ok.png')
        assinar_transm = self.pst.join('assinar_transm.png')

        Img.verificar_até_achar(gerenc_nfe, 0.89)
        Img.click(exportar_nfe, 0.9)
        Img.click(escolha_arq, 0.9)
        sleep(1)
        px.hotkey('winleft', 'right')
        px.hotkey('winleft', 'up')
        px.hotkey('winleft', 'up')
        px.hotkey('winleft', 'down')
        x, y = Img.coordenadas(escolha_arq, 0.9)
        px.click(x+50, y+100)
        while True:
            if Img.verifica_na_tela(downloads, 0.9) == True:
                break
            px.press('up')
        Img.click(downloads, 0.9)
        px.press('enter')
        Img.verificar_até_achar(assinar_transm, 0.9)
        Img.click(assinar_transm, 0.9)
        px.write('n')
        Img.verificar_até_achar(export_ok, 0.9)
        Img.click(export_ok, 0.9)
        px.press('enter')


    def imprimir_danfe(self):
        imprimir_danfe = self.pst.join('imprimir_danfe.png')
        danfe_aba = self.pst.join('danfe_aba.png')
        select_diretory = self.pst.join('select_diretory.png')
        setinha_da_aba_1 = self.pst.join('setinha_da_aba_1.png')
        setinha_da_aba_2 = self.pst.join('setinha_da_aba_2.png')
        downloads = self.pst.join('downloads_danfe.png')
        selecionar_pasta = self.pst.join('selecionar_pasta.png')
        processo_ok = self.pst.join('processo_ok.png')

        Img.click(imprimir_danfe, 0.9)
        Img.verificar_até_achar(danfe_aba, 0.9)
        Img.click(danfe_aba, 0.9)
        px.write('p')
        px.press('tab')
        px.press('enter')
        Img.verificar_até_achar(select_diretory, 0.9)

        while Img.verifica_na_tela(downloads, 0.9) == False:
            if Img.verifica_na_tela(setinha_da_aba_2, 0.98) == True:
                Img.click(setinha_da_aba_2, 0.98)
            else:
                Img.click(setinha_da_aba_1, 0.98)

        Img.click(downloads, 0.9)
        Img.click(selecionar_pasta, 0.9)
        Img.click(processo_ok, 0.9)
        px.press('enter')

        Img.click(danfe_aba, 0.9)
        px.hotkey('alt', 'f4')


    def gerar(self):
        self.verificar_NOP()
        self.clicar_gerar_nota()
        nr_nota, nome, valor = self.pegar_dados_nota()
        self.transmitir()
        self.exportar_nfe()

        return nr_nota, nome, valor


class Ticket():
    def __init__(self):
        self.pst = imagens('NF')

    def clicar_chrome(self):
        chrome = self.pst.join('chrome.png')
        Img.click(chrome, 0.9)


    def verifica_aba(self):
        enviar_aba = self.pst.join('enviar_aba.png')
        Img.verificar_até_achar(enviar_aba, 0.8)
        sleep(1)


    def select_serviço(self):
        servico = self.pst.join('servico.png')
        serv_comb = self.pst.join('serv_comb.png')

        Img.click(servico, 0.8)
        Img.click(serv_comb, 0.8)


    def digitar_nota(self, numero):
        numero_nota_fiscal = self.pst.join("numero_nota_fiscal.png")

        Img.click(numero_nota_fiscal, 0.8)
        px.write(str(numero))


    def escolher_arquivo(self):
        escolher_aba = self.pst.join('escolher_aba.png')
        escolher_arquivo = self.pst.join('escolher_arquivo.png')
        escolher_aba_1 = self.pst.join('escolher_aba_1.png')

        Img.click(escolher_arquivo, 0.8)
        while True:
            if Img.verifica_na_tela(escolher_aba, 0.9) == True:
                x, y = Img.coordenadas(escolher_aba, 0.9)
                break
            if Img.verifica_na_tela(escolher_aba_1, 0.9) == True:
                x, y = Img.coordenadas(escolher_aba_1, 0.9)
                break
            
        px.click(x, y)
        sleep(1)
        for i in range(0, 2):
            px.hotkey('shift', 'tab')
        px.press('up')
        px.press('down')
        px.press('enter')
        sleep(0.9)
        


    def confirmar(self):
        continuar_button = self.pst.join('continuar_button.png')
        Img.click(continuar_button, 0.8)


    def enviar_nota(self, nr_nota):
        self.clicar_chrome()
        self.verifica_aba()
        self.select_serviço()
        self.digitar_nota(numero=nr_nota)
        self.escolher_arquivo()
        self.confirmar()


class Valecard():
    def __init__(self, valor_nota):
        self.pst = imagens('NF')
        self.valor_nota = valor_nota

    def clicar_chrome(self):
        chrome = self.pst.join('chrome.png')
        Img.click(chrome, 0.9)

    def upload_tela(self):
        selecione_opcao = self.pst.join('selecione_opcao.png')
        selecione_opcao_1 = self.pst.join('selecione_opcao_1.png')
        xml = self.pst.join('xml.png')
        escolher_xml = self.pst.join('escolher_xml.png')
        valor_valecard = self.pst.join('valor_valecard.png')
        adicionar = self.pst.join('adicionar.png')
        salvar = self.pst.join('salvar.png')

        while True:
            if Img.verifica_na_tela(selecione_opcao, 0.9) == True:
                Img.click(selecione_opcao, 0.9)
                break
            if Img.verifica_na_tela(selecione_opcao_1, 0.9) == True:
                Img.click(selecione_opcao_1, 0.9)
                break
        Img.click(xml, 0.9)
        sleep(1)
        while Img.verifica_na_tela(escolher_xml, 0.9) == False:
            px.press('pagedown')
        Img.click(escolher_xml, 0.9)

        self.renomear_escolher_arquivo()

        while Img.verifica_na_tela(valor_valecard, 0.9) == False:
            px.press('pageup')

        Img.click(valor_valecard, 0.9)
        print(self.valor_nota)
        px.write('1')

        while Img.verifica_na_tela(adicionar, 0.9) == False:
            px.press('pagedown')

        Img.click(adicionar, 0.9)
        Img.click(salvar, 0.9)
        

    def renomear_escolher_arquivo(self):
        from os.path import expanduser, join
        escolher_aba = self.pst.join('escolher_aba.png')
        escolher_aba_1 = self.pst.join('escolher_aba_1.png')
        data_mod = self.pst.join('data_mod.png')
        hoje = self.pst.join("hoje.png")
        nome = self.pst.join("nome.png")


        caminho = str(join(expanduser("~"), 'Downloads'))
        while True:
            if Img.verifica_na_tela(escolher_aba, 0.9) == True:
                Img.click(escolher_aba, 0.9)
                break
            elif Img.verifica_na_tela(escolher_aba_1, 0.9) == True:
                Img.click(escolher_aba_1, 0.9)
                break   

        x1, y1 = Img.coordenadas(nome, 0.92)
        px.click(x1+120, y1)
        px.hotkey('ctrl', 'a')
        px.press('del')
        
        px.write(caminho)
        px.press('enter')
        cont = 0
        while True:
            if cont >= 2:
                if Img.verifica_na_tela(hoje, 0.9) != True:
                    Img.click(data_mod, 0.9)
                    cont += 1
            else:
                break
            Img.click(data_mod, 0.9)
            cont += 1
            sleep(0.2)
            if Img.verifica_na_tela(hoje, 0.9) != True:
                Img.click(data_mod, 0.9)
                cont += 1
            else:
                break
            
        x, y = Img.coordenadas(hoje, 0.9)
        px.click(x, y+20)
        px.hotkey('f2')
        px.press('end')
        for i in range(0, 11):
            px.press('backspace')
        px.press('enter')
        sleep(1)
        px.press('up')
        px.press('down')
        px.press('enter')


    def upload(self):
        self.clicar_chrome()
        self.upload_tela()



class Nota_Fiscal():
    def emitir_ticket():
        nr, nome, valor = Nota().gerar()
        print(nr, nome, valor)
        Ticket().enviar_nota(nr_nota=nr)

    def emitir_padrão():
        nr, nome, valor = Nota().gerar()
        print(nr, nome, valor)

    def emitir_pdf():
        nr, nome, valor = Nota().gerar()
        print(nr, nome, valor)
        Nota().imprimir_danfe()
        
    def emitir_valecard():
        nr, nome, valor = Nota().gerar()
        print(nr, nome, valor)
        Valecard(valor_nota=valor).upload()


