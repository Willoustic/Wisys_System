from PDV_Automatico.processos import imagens, Img
import pyautogui as px
import pyperclip as pc
from time import sleep

cte = imagens('CTe')

class Clicks():

    # Tela Conhecimento
    def limpar_tela():
        limpar = cte.join('limpar.png')
        Img.click(limpar, 0.9)
        sleep(1)
        px.write('n')
        sleep(1)

    def digitar_n_conhecimento(n_conhecimento):
        conhecimento = cte.join('conhecimento.png')
        x, y = Img.coordenadas(conhecimento, 0.9)
        px.doubleClick(x+80, y)
        px.write(n_conhecimento)

    def digitar_serie(n_serie):
        serie = cte.join('serie.png')
        x, y = Img.coordenadas(serie, 0.9)
        px.doubleClick(x+80, y)
        px.write(n_serie)
    
    def digitar_transportadora():
        # NH TRANSPORTES: 3984
        transport = cte.join('transport.png')
        x, y = Img.coordenadas(transport, 0.9)
        px.doubleClick(x+80, y)
        px.write('3984')
        px.press('enter')

    def digitar_datas(data_emi):
        data_emissao = cte.join('data_emissao.png')
        x, y = Img.coordenadas(data_emissao, 0.9)
        px.click(x+100, y)
        sleep(0.5)
        px.click(x+100, y)
        px.write(data_emi)
        #px.press('tab')
        px.write(data_emi)

    def modelo_documento():
        modelo_doc = cte.join('modelo_doc.png')
        modelo_cte = cte.join('modelo_cte.png')

        x, y = Img.coordenadas(modelo_doc, 0.9)
        px.click(x+80, y)
        Img.click(modelo_cte, 0.9)
        

    def modal_transp():
        modalidade_transp = cte.join('modalidade_transp.png')
        x, y = Img.coordenadas(modalidade_transp, 0.9)
        px.click(x+80, y)
        px.write('Rodo')
        px.press('enter')

    def clicar_natureza_operac(tipo):
        nat_operac = cte.join('nat_operac.png')

        if tipo == 'DE':
            nat_op = cte.join('nat_op_DE.png')
        elif tipo == 'FE':
            nat_op = cte.join('nat_op_FE.png')
        
        x, y = Img.coordenadas(nat_operac, 0.9)
        px.click(x+80, y)
        Img.click(nat_op, 0.9)

    def tribut_pis():
        tribut = cte.join('tribut.png')
        x, y = Img.coordenadas(tribut, 0.9)
        px.click(x+80, y)
        px.write('56')

    def tribut_cofins():
        tributa = cte.join('tributa.png')
        x, y = Img.coordenadas(tributa, 0.9)
        px.click(x+80, y)
        px.write('64')

    def digitar_chave(chave):
        chave_cte = cte.join('chave_cte.png')
        x, y = Img.coordenadas(chave_cte, 0.9)
        px.click(x+80, y)
        px.write(str(chave))

    def selec_nat_frete():
        natureza_frete = cte.join('natureza_frete.png')
        tipo = '9'
        x, y = Img.coordenadas(natureza_frete, 0.9)
        px.click(x+100, y)
        px.write(tipo)
        px.press('enter')

    def digitar_cidade_destino(cid_destino):
        cid_dest = cte.join('cid_dest.png')
        busca = cte.join('busca.png')

        x, y = Img.coordenadas(cid_dest, 0.9)
        px.doubleClick(x+150, y)
        px.write(f'%{cid_destino}')
        px.press('enter')
        contador = 0
        while Img.verifica_na_tela(busca, 0.9) == False:
            if contador == 2:
                break
            sleep(0.5)
            contador += 1
        Img.verificar_até_sair(busca, 0.9)


    def digitar_cidade_origem(cid_origem):
        cid_orig = cte.join('cid_orig.png')
        busca = cte.join('busca.png')

        x, y = Img.coordenadas(cid_orig, 0.9)
        px.doubleClick(x+150, y)
        px.write(f'%{cid_origem}')
        px.press('enter')
        contador = 0
        while Img.verifica_na_tela(busca, 0.9) == False:
            if contador == 2:
                break
            sleep(0.5)
            contador += 1
        Img.verificar_até_sair(busca, 0.9)


    # Tela Valores

    def clicar_valores():
        valores = cte.join('valores.png')
        Img.click(valores, 0.9)
    
    def botar_total_frete(valor):
        total_frete = cte.join('total_frete.png')
        x, y = Img.coordenadas(total_frete, 0.9)
        px.doubleClick(x+80, y)
        px.press('del')
        px.write(str(valor))
        px.press('tab')

    def apagar_valor_pis():
        valor_pis = cte.join('valor_pis.png')
        x, y = Img.coordenadas(valor_pis, 0.9)
        px.doubleClick(x+100, y)
        px.press('del')

    def apagar_valor_cofins():
        valor_cofins = cte.join('valor_cofins.png')
        x, y = Img.coordenadas(valor_cofins, 0.9)
        px.doubleClick(x+100, y)
        px.press('del')


    # Tela Pagamento

    def clicar_pagamento():
        pagamento = cte.join('pagamento.png')
        pagamento_clicado = cte.join('pagamento_clicado.png')
        Img.click(pagamento, 0.9)

        # verificar se está clicado
        Img.verificar_até_achar(pagamento_clicado, 0.9)

    def verificar_se_esta_no_parcelado():
        tipo_cobranca = cte.join('tipo_cobranca.png')
        parcelado = cte.join('parcelado.png')

        if Img.verifica_na_tela(tipo_cobranca, 0.9) == False:
            Img.click(parcelado, 0.9)
        else:
            pass

    def selec_tipo_cobranc():
        # Selecionar Carteira
        Clicks.verificar_se_esta_no_parcelado()
        tipo_cobranca = cte.join('tipo_cobranca.png')
        carteira = cte.join('carteira.png')
        x, y = Img.coordenadas(tipo_cobranca, 0.9)
        px.click(x+80, y)
        px.write('car')
        Img.click(carteira, 0.9)

    def add_vencimento(data_emi):
        venc = cte.join('venc.png')
        x, y = Img.coordenadas(venc, 0.9)
        px.doubleClick(x+80, y)
        px.write(str(data_emi))

    def get_valor_cobranca():
        valor_auto = cte.join('valor_auto.png')
        Img.DoubleClick(valor_auto, 0.9)

    def incluir_vencimento():
        # Se baseando no nome juros
        juros = cte.join('juros.png')
        x, y = Img.coordenadas(juros, 0.9)
        px.click(x+120, y)

    def incluir_centro_e_rateio():
        centro = cte.join('centro.png')
        x, y = Img.coordenadas(centro, 0.9)
        px.click(x+200, y)
        px.write('adm')
        px.press('enter')
        px.write('100')
        px.press('tab')

    def inserir_rateio():
        # Se baseando no valor rateio
        valor_rateio = cte.join('valor_rateio.png')
        x, y = Img.coordenadas(valor_rateio, 0.9)
        px.click(x+200, y)

    def incluir_cte():
        incluir_icon = cte.join("incluir_cte.png")
        x, y = Img.coordenadas(incluir_icon, 0.9)
        px.click(x, y)
