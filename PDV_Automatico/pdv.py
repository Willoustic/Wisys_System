import pyautogui as px
import pyperclip as pc
from Emsys.login_emsys import Emsys
from time import sleep
import os
from .processos import imagens_pdv, Img, imagens_Emsys
import pandas as pd
from .Excel import Excel
from .extra import Extra_excel
from datetime import datetime



def verificar():

    photo = os.path.join('Images', 'PDV_Automatico', 'fechado.png')

    try: 
        validar = px.locateOnScreen(photo, confidence=0.9)
    except:
        validação = False
    else:
        validação = True

    return validação


class Processos():
    def caminho_do_arquivo(posto_id, mes):
        if posto_id == 1:
            caminho_arq = os.path.join('Arquivos', 'Relatorios', f'MES {mes} {datetime.today().year}', 'NOVO H')
        elif posto_id == 2:
            caminho_arq = os.path.join('Arquivos', 'Relatorios', f'MES {mes} {datetime.today().year}', 'TRANSPORTES')
        elif posto_id == 3:
            caminho_arq = os.path.join('Arquivos', 'Relatorios', f'MES {mes} {datetime.today().year}', 'VITORIA')

        os.makedirs(caminho_arq, exist_ok=True)
        return f'{os.path.abspath('')}\\{caminho_arq}\\'


    def nome_do_posto(cod_posto):
        if cod_posto == 1:
            posto_nome = 'POSTO ZN'
        elif cod_posto == 2:
            posto_nome = 'POSTO ZS'
        elif cod_posto == 3:
            posto_nome = 'P. VITORIA'
        return posto_nome


class Caixa():
    
    def select_data(data):
        pst = imagens_pdv('data')
        select = pst.join('select.png')
        pesquisar = pst.join('pesquisar.png')
        on_pesquisar = pst.join('on_pesquisar.png')

        # clicar na data
        Img.click(select, precisão=0.9)
        # digitar a data
        px.write(data)
        # pesquisar o caixa
        Img.click(imagem=pesquisar, precisão=0.99)

        Caixa.clicar_resumo()


    def voltar():    
    # voltar todos os caixas
        pasta = imagens_pdv('voltar')
        imagem = pasta.join('voltar_button.png')
        Img.click(imagem, 0.99)
        
        Caixa.clicar_resumo()


    def verifica_pendencia():
        pst = imagens_pdv('pendencia')
        pendencia = pst.join('pendencia.png')

        bool_teste = Img.verifica_na_tela(pendencia, precisão=0.99)

        return bool_teste
    

    def inserir_rateio():
        pst = imagens_pdv('rateio')
        operador = pst.join('operador.png')
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
        on_proximo = pst.join('on_proximo.png')

        cont = 1
        while True:
            if cont > 1:
                Caixa.clicar_resumo()
            cont += 1
            if Img.verifica_na_tela(ultimo_Caixa, 0.98) == True:
                break
            
            if Caixa.verifica_pendencia() == False:
                operador_x, operador_y = Img.coordenadas(operador, precisão=0.9)
                px.doubleClick(operador_x+90, operador_y)
                operador_cod = pc.copy('')
                px.hotkey('ctrl', 'c')

                operador_cod = pc.paste()
                
                if len(operador_cod) == 0:
                    operador_cod = '22'

                print(operador_cod)

                Img.click(responsaveis, precisão=0.99)
                Img.verificar_até_achar(valor_rateio, precisão=0.9)

                if Img.verifica_na_tela(valor_rateio, precisão=0.9) == True:
                    rateio_x, rateio_y = Img.coordenadas(valor_rateio, 0.9)
                    valor = pc.copy('')
                    px.doubleClick(rateio_x+130, rateio_y)
                    px.hotkey('ctrl', 'c')
                    valor = pc.paste()
                    print(valor)

                    if str(valor) != '0':
                        Img.click(incluir_rateio, precisão=0.9)
                        Img.verificar_até_achar(incluir_app, precisão=0.9)
                        ratear_x, ratear_y = Img.coordenadas(valor_a_ratear, precisão=0.9)
                        px.click(ratear_x+100, ratear_y)
                        px.write(valor)
                        px.press('enter')
                        sleep(1)
                        if operador_cod == '':
                            operador_cod == '22'
                        px.write(operador_cod)
                        sleep(1)
                        px.press('enter')
                        Img.click(incluir_icon, precisão=0.9)
                        Img.click(incluir_app, precisão=0.9)
                        sleep(0.5)
                        px.hotkey('alt', 'f4')
                        sleep(0.5)
                        Img.verificar_até_sair(incluir_app, precisão=0.9)

                Img.click(salvar, precisão=0.9)
                Img.verificar_até_achar(salvo, precisão=0.9)
                px.press('enter')

            Img.click(proximo, precisão=0.9)
            #Img.verificar_até_sair(on_proximo, precisão=0.9)


    def excluir_sangria():
        pst = imagens_pdv('excluir')
        confirm = pst.join('confirm.png')
        proximo = pst.join('proximo.png')
        excluir = pst.join('excluir.png')
        recebimento = pst.join('recebimento.png')
        salvo = pst.join('salvo.png')
        ultimo_Caixa = pst.join('ultimo_Caixa.png')
        yes_button = pst.join('yes_button.png')
        especies = pst.join('especies.png')
        salvar = pst.join('salvar.png')
        on_proximo = pst.join('on_proximo.png')
        y_excluir = pst.join('y_excluir.png')
        especie_caixa = pst.join('especie_caixa.png')

        cont = 1
        while True:
            if cont > 1:
                Caixa.clicar_resumo()
            cont += 1
            if Img.verifica_na_tela(ultimo_Caixa, 0.98) == True:
                break
            
            if Caixa.verifica_pendencia() == False:
                if Img.verifica_na_tela(especies, precisão=0.9) == True:
                    Img.click(especies, 0.98)
                else:
                    Img.DoubleClick(recebimento, 0.9)
                    Caixa.clicar_resumo()
                    Img.verificar_até_achar(especies, 0.98)
                    Img.click(especies, 0.98)

                Img.verificar_até_achar(especie_caixa, precisão=0.9)

                if Img.verifica_na_tela(y_excluir, precisão=0.99) == False:
                    Img.click(excluir, 0.99)
                    Img.verificar_até_achar(confirm, 0.9)
                    Img.click(yes_button, 0.9)

                Caixa.clicar_resumo()

                Img.click(salvar, 0.9)
                Img.verificar_até_achar(salvo, 0.9)
                px.press('enter')

            Img.click(proximo, 0.9)
            #Img.verificar_até_sair(on_proximo, 0.9)


    def clicar_resumo():
        pst = imagens_pdv('resumo')
        not_resumo = pst.join('not_resumo.png') 
        if_resumo = pst.join('if_resumo.png') 

        Img.click(not_resumo, precisão=0.9)
        Img.verificar_até_achar(if_resumo, 0.9)

    
    def confirmar():
        #while True:
        pasta = imagens_pdv('confirmar')
        ultimo_caixa = pasta.join('ultimo_caixa.png')
        confirm_button = pasta.join('confirm_button.png')
        fechado = pasta.join('fechado.png')
        yes_no = pasta.join('yes_no.png')
        aguarde = pasta.join('aguarde.png')
        proximo = pasta.join('proximo.png')
        status_aberto = pasta.join('status_aberto.png')
        limpar = pasta.join('limpar.png')
        on_limpar = pasta.join('on_limpar.png')
        aba_fech_1 = pasta.join('aba_fech_1.png')
        cont = 1
        while True:
            if cont > 1:
                Caixa.clicar_resumo()
            cont += 1
             
            if Img.verifica_na_tela(ultimo_caixa, precisão=0.98) == True:
                break

            if Caixa.verifica_pendencia() == False:
            
                if Img.verifica_na_tela(confirm_button, precisão=0.99) == True:
                    Img.click(confirm_button, precisão=0.95)    
                    Img.verificar_até_achar(yes_no, precisão=0.95)    
                    Img.click(yes_no, precisão=0.95)    
                    px.write('y')    
                    Img.verificar_até_achar(fechado, precisão=0.95)    
                    Img.click(fechado, precisão=0.95)    
                    px.press('enter')    
                    Img.verificar_até_sair(aguarde, precisão=0.95)    

            if Img.verifica_na_tela(ultimo_caixa, precisão=0.98) == False:
                Img.click(proximo, precisão=0.98)

        Img.click(limpar, precisão=0.9)
        Img.click(aba_fech_1, precisão=0.9)
        Img.verificar_até_sair(on_limpar, precisão=0.9)
        px.hotkey('alt', 'f4')


    def demonstrativo_csv(posto, data):
        try:
            posto = int(posto)
        except:
            print('Número de posto inválido')
        else:
            from .Excel import Excel
            data_ = data
            
            if len(data_) > 4:
                ano = data_[-4:]
                mes = data_[2:4]
                dia = data_[:2]
            else:
                mes = data_[2:4]
                dia = data_[:2]

            posto_nome = Processos.nome_do_posto(cod_posto=posto)
            caminho_arq = Processos.caminho_do_arquivo(posto_id=posto, mes=mes)
            # abrir relatorio de demonstrativo em csv

            imagens = imagens_pdv('d_csv')

            rel = imagens.join('ABA_REL.png')
            custom = imagens.join('CUSTOM.png')
            aba_dem = imagens.join('DEMONSTRATIVO.png')
            seta_csv = imagens.join('seta_csv.png')
            csv_select = imagens.join('csv_select.png')
            gerar_relatorio = imagens.join('gerar_relatorio.png')
            realizando_consulta = imagens.join('realizando_consulta.png')
            data_select = imagens.join('data_select.png')
            ok_button = imagens.join('ok_button.png')
            venda_cartao = imagens.join('venda_cartao.png')
            sair = imagens.join('sair.png')
            gerar_arquivo = imagens.join('gerar_arquivo.png')
            salvar = imagens.join('salvar.png')
            salvo = imagens.join('salvo.png')
            template = imagens.join('template.png')

            
            Img.click(rel, precisão=0.9)
            Img.click(custom, precisão=0.9)
            Img.click(aba_dem, precisão=0.9)
            Img.click(seta_csv, precisão=0.9)
            Img.click(csv_select, precisão=0.9)
            Img.click(gerar_relatorio, precisão=0.9)

            Img.verificar_até_achar(data_select, precisão=0.9)
            
            # digitar posto
            px.write(str(posto))
            px.press('tab')

            # digitar data
            px.write(str(data))

            Img.click(ok_button, precisão=0.9)
            Img.verificar_até_achar(realizando_consulta, 0.9)
            x_cons, y_cons = Img.coordenadas(realizando_consulta, 0.9)
            px.moveTo(x_cons, y_cons)
            Img.verificar_até_sair(realizando_consulta, 0.9)
            sleep(1)

            while Img.verifica_na_tela(venda_cartao, 0.9) == False:
                # era px.hotkey('alt', 'tab') mas não deu certo
                px.click()
            Img.click(venda_cartao, precisão=0.9)
            Img.click(sair, precisão=0.9)
            px.press('space')
            Img.verificar_até_achar(gerar_arquivo, precisão=0.9)

            caminho_total = f'{caminho_arq}{posto_nome} {data_} rel'
            
            px.write(f'{caminho_total}')
            print(f'{caminho_total}')
            
            Img.click(salvar, precisão=0.9)
            Img.verificar_até_achar(salvo, precisão=0.9)
            px.press('enter')
            Img.click(template, precisão=0.9)
            px.hotkey('alt', 'f4')
            Excel.run(arquivo_inicial=f'{caminho_total}.csv')
            Extra_excel(arquivo=f'{caminho_total}.xlsx')
            
            

    def fechamento_por_vendedor(posto, data):
        try:
            posto = int(posto)
        except:
            print('Numero de posto inválido')
        else:
            data_ = data
            mes = data_[2:4]
            posto_nome = Processos.nome_do_posto(cod_posto=posto)
            caminho_arq = Processos.caminho_do_arquivo(posto_id=posto, mes=mes)
        
            imagens = imagens_pdv('fech_csv')


            rel = imagens.join('ABA_REL.png')
            custom = imagens.join('CUSTOM.png')
            fech_aba = imagens.join('fech_aba.png')
            seta_csv = imagens.join('seta_csv.png')
            csv_select = imagens.join('csv_select.png')
            gerar_relatorio = imagens.join('gerar_relatorio.png')
            data_select = imagens.join('data_select.png')
            ok_button = imagens.join('ok_button.png')
            venda_cartao = imagens.join('venda_cartao.png')
            sair = imagens.join('sair.png')
            gerar_arquivo = imagens.join('gerar_arquivo.png')
            salvar = imagens.join('salvar.png')
            salvo = imagens.join('salvo.png')
            template = imagens.join('template.png')


            Img.click(rel, precisão=0.9)
            Img.click(custom, precisão=0.9)
            Img.click(fech_aba, precisão=0.9)
            Img.click(seta_csv, precisão=0.9)
            Img.click(csv_select, precisão=0.9)
            Img.click(gerar_relatorio, precisão=0.9)

            Img.verificar_até_achar(data_select, precisão=0.9)
            
            # digitar data
            px.write(str(data))

            Img.click(ok_button, precisão=0.9)
            Img.click(venda_cartao, precisão=0.9)
            Img.click(sair, precisão=0.9)
            px.press('space')
            Img.verificar_até_achar(gerar_arquivo, precisão=0.9)

            caminho_total = f'{caminho_arq}'
            
            px.write(f'{caminho_total}{posto_nome} {data_} vendas')
            print(f'{caminho_total}{posto_nome} {data_} vendas')
            
            
            Img.click(salvar, precisão=0.9)
            Img.verificar_até_achar(salvo, precisão=0.9)
            px.press('enter')
            Img.click(template, precisão=0.9)
            px.hotkey('alt', 'f4')


    def conferencia(data):
        pst = imagens_pdv('conferencia')
        conf_aba = pst.join('conf_aba.png')
        conf_app = pst.join('conf_app.png')
        pdv_aba = pst.join('pdv_aba.png')
        pesquisar = pst.join('pesquisar.png')
        warning_aba = pst.join('warning.png')
        acertar_dif = pst.join('acertar_dif.png')
        conferido = pst.join('conferido.png')
        estornar = pst.join('estornar.png')
        data_abastecimento = pst.join('data_abastecimento.png')

        Img.click(pdv_aba, precisão=0.9)
        Img.click(conf_aba, precisão=0.9)
        Img.verificar_até_achar(conf_app, precisão=0.9)

        # clicar na data
        data_x, data_y = Img.coordenadas(data_abastecimento, precisão=0.9)
        px.click(data_x+20, data_y-3)

        # digitar data
        px.write(data)

        Img.click(pesquisar, precisão=0.99)
        Img.click(warning_aba, precisão=0.9)
        px.write('y')
        Img.verificar_até_achar(acertar_dif, precisão=0.98)
        Img.click(acertar_dif, precisão=0.99)

        sleep(5)

        if Img.verifica_na_tela(warning_aba, precisão=0.9):
            px.write('y')

        Img.click(conferido, precisão=0.99)
        px.press('enter')
        
        Img.verificar_até_achar(estornar, precisão=0.99)


    def relatorio_formas_pgto(posto, data):
        pst = imagens_pdv('formas_pgto')
        apenas = pst.join('caixas_confirmed.png')
        gerar = pst.join('gerar_relatorio.png')
        imprimir = pst.join('imprimir.png')
        print_aba = pst.join('print_aba.png')
        aba_forma = pst.join('aba_forma.png')
        rel_aberto = pst.join('rel_aberto.png')
        ok_button = pst.join('ok_button.png')
        pre_aberto = pst.join('pre_aberto.png')
        # abrir rel. vendas por forma de pgto.
        px.hotkey('altleft')
        px.write('Y2')
        sleep(0.2)
        px.write('Y04')
        sleep(0.2)
        px.write('Y16')
        sleep(0.2)
        px.write('Y17')
        Img.verificar_até_achar(aba_forma, 0.9)
        # selecionar a data
        px.write(data)
        sleep(0.2)
        px.write(data)
        sleep(0.2)
        # desabilitar a caixinha 'apenas caixas confirmados'
        x, y = Img.coordenadas(apenas, 0.9)
        sleep(0.5)
        # gerar relatorio
        Img.click(gerar, 0.9)
        Img.verificar_até_achar(rel_aberto, 0.9)
        # clicar para imprimir
        Img.click(imprimir, 0.9)
        sleep(1)
        # clicar ok
        Img.verificar_até_achar(print_aba, 0.9)
        Img.click(ok_button, 0.9)
        Img.verificar_até_sair(print_aba, 0.9)
        Img.verificar_até_achar(rel_aberto, 0.9)
        Img.click(rel_aberto, 0.9)
        sleep(2)
        # fechar o rel.
        px.hotkey('alt', 'f4')
        sleep(0.9)
        Img.verificar_até_sair(rel_aberto, 0.9)
        Img.verificar_até_achar(aba_forma, 0.9)
        Img.click(aba_forma, 0.9)
        # fechar o selecionador de data de vendas por forma de pgto.
        px.hotkey('alt', 'f4')
        Img.verificar_até_sair(aba_forma, 0.9)        
        sleep(0.2)


    def rel_boletim_caixa(posto, data):
        try:
            posto = int(posto)
        except:
            print('Numero de posto inválido')
        else:
            data_ = data
            mes = data_[2:4]
            posto_nome = Processos.nome_do_posto(cod_posto=posto)
            caminho_arq = Processos.caminho_do_arquivo(posto_id=posto, mes=mes)

        imgs = imagens_pdv('boletim')

        caixa_select = imgs.join('caixa_select.png')
        csv_aba = imgs.join('csv_aba.png')
        financeiro_aba = imgs.join('financeiro_aba.png')
        gera_arq_csv = imgs.join('gera_arq_csv.png')
        gera_rel = imgs.join('gera_rel.png')
        gerado_ok = imgs.join('gerado_ok.png')
        rel_aba = imgs.join('rel_aba.png')
        rel_bol_aba = imgs.join('rel_bol_aba.png')
        rel_bol_cx = imgs.join('rel_bol_cx.png')
        salvar = imgs.join('salvar.png')
        setinha = imgs.join('setinha.png')

        Img.click(financeiro_aba, 0.9)
        Img.click(caixa_select, 0.9)
        Img.click(rel_aba, 0.9)
        Img.click(rel_bol_cx, 0.9)

        Img.verificar_até_achar(rel_bol_aba, 0.9)
        px.write(str(data_))
        px.write(str(data_))

        Img.click(setinha, 0.9)
        Img.click(csv_aba, 0.9)
        Img.click(gera_rel, 0.9)

        Img.verificar_até_achar(gera_arq_csv, 0.9)

        caminho_total = f'{caminho_arq}'
        
        px.write(f'{caminho_total}{posto_nome} {data_} sangrias')
        print(f'{caminho_total}{posto_nome} {data_} sangrias')

        Img.click(salvar, 0.9)
        Img.verificar_até_achar(gerado_ok, 0.9)
        Img.click(gerado_ok, 0.9)
        px.press('enter')

        Img.verificar_até_achar(rel_bol_aba, 0.9)
        Img.click(rel_bol_aba, 0.9)
        px.hotkey('alt', 'f4')

        arquivo_csv = f'{caminho_total}{posto_nome} {data_} sangrias.csv'
        arquivo = Excel.csv_to_excel(arquivo_csv)
        print(arquivo)
        if os.path.exists(arquivo):
            df_depositos = pd.DataFrame({'Valor': [], 'Operador': []})
            df_brasifort = pd.DataFrame({'Usuário Nome': [], 'Usuário Sobrenome': [], 'Total Valor Automático': []})
            df_brinks = pd.DataFrame({'Depositante': [], 'Valor do Depósito': []})
            df_especie = pd.DataFrame({'Valor': [], 'Operador': []})

            with pd.ExcelWriter(arquivo, mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
                df_depositos.to_excel(writer, sheet_name='DEPOSITOS', index=False)
                df_brasifort.to_excel(writer, sheet_name='BRASIFORT', index=False)
                df_brinks.to_excel(writer, sheet_name='BRINKS', index=False)
                df_especie.to_excel(writer, sheet_name='ESPECIE', index=False)

            os.remove(arquivo_csv)


class Caixas():
    from datetime import datetime
    def __init__(self, dia, mes, posto, ano=datetime.today().year):
        while True:
            try:
                self.dia = str(dia)
                self.mes = str(mes)
                self.ano = str(ano)
                self.posto = str(posto)
            except Exception:
                print(Exception)
            else:
                if len(self.dia) == 2:
                    if len(self.mes) == 2:
                        self.data = f'{self.dia}{self.mes}{self.ano}'
                        break
                break

        
    def Iniciar(self):
        Caixa.demonstrativo_csv(posto=self.posto, data=self.data)
        Caixa.fechamento_por_vendedor(posto=self.posto, data=self.data)
        Emsys.abrir_pdv()
        Caixa.select_data(data=self.data)
        Caixa.excluir_sangria()
        Caixa.voltar()

        Caixa.inserir_rateio()
        
        pasta = imagens_pdv('confirmar')
        limpar = pasta.join('limpar.png')
        on_limpar = pasta.join('on_limpar.png')
        aba_fech_1 = pasta.join('aba_fech_1.png')

        Img.click(limpar, precisão=0.9)
        Img.click(aba_fech_1, precisão=0.9)
        Img.verificar_até_sair(on_limpar, precisão=0.9)
        px.hotkey('alt', 'f4')

        if self.posto != '2':
            Caixa.rel_boletim_caixa(posto=self.posto, data=self.data)

    def Finalizar(self):
        Emsys.abrir_pdv()
        Caixa.select_data(data=self.data)
        Caixa.confirmar()
        Caixa.relatorio_formas_pgto(posto=self.posto, data=self.data)
        Caixa.conferencia(data=self.data)
