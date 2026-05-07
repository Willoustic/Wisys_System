import pyautogui as px
from time import sleep
import os
from PDV_Automatico.processos import imagens_Emsys, Img


class Emsys:

    def __init__(self, posto, name, password):
        self.posto = posto
        self.usuario = name
        self.senha = password
        os.system('cls')

    def clicar_gerencial():
        gerencial = imagens_Emsys().join('gerencial.png')

        while True:
            if Img.verifica_na_tela(gerencial, 0.9) == True:
                Img.click(gerencial, 0.9)
            else:
                break


    def verificar_fech():
        try:
            verificar_fech_aberto = os.path.join('Images', 'Emsys', 'aba_fech_1.png')
            pdv_aberto = px.locateOnScreen(verificar_fech_aberto, confidence=0.95)
        except:
            try:
                verificar_fech_aberto_1 = os.path.join('Images', 'Emsys', 'aba_fech.png')
                pdv_aberto_1 = px.locateOnScreen(verificar_fech_aberto_1, confidence=0.90)
            except:
                return False
            else:
                if pdv_aberto_1:
                    try:
                        limpar = os.path.join('Images', 'PDV_Automatico', 'limpar.png')
                        limpar_mouse = px.locateOnScreen(limpar, confidence=0.90)
                        pdv_aberto = px.locateOnScreen(verificar_fech_aberto, confidence=0.95)
                    except:
                        pass
                    else:
                        center_clean = px.center(limpar_mouse)
                        px.moveTo(center_clean.x, center_clean.y)
                        px.click()
                        sleep(1)
                        if Img.verifica_na_tela(imagens_Emsys().join('pergunta.png'), precisão=0.9):
                            px.write('n')
                        sleep(1)

                        center_point = px.center(pdv_aberto)
                        px.moveTo(center_point.x, center_point.y)
                        px.click()
                        px.hotkey('alt', 'f4')
                        Img.verificar_até_sair(verificar_fech_aberto, precisão=0.9)
                        print('Fechamento aberto, porém foi fechado')
                        return True
        else:
            if pdv_aberto:
                try:
                    limpar = os.path.join('Images', 'PDV_Automatico', 'limpar.png')
                    limpar_mouse = px.locateOnScreen(limpar, confidence=0.90)
                except:
                    pass
                else:
                    center_clean = px.center(limpar_mouse)
                    px.moveTo(center_clean.x, center_clean.y)
                    px.click()
                    sleep(1)
                    if Img.verifica_na_tela(imagens_Emsys().join('pergunta.png'), precisão=0.9):
                        px.write('n')
                    sleep(1)

                center_point = px.center(pdv_aberto)
                px.moveTo(center_point.x, center_point.y)
                px.click()
                px.hotkey('alt', 'f4')
                Img.verificar_até_sair(verificar_fech_aberto, precisão=0.9)
                print('Fechamento aberto, porém foi fechado')
                return True


    def abrir():
        # abrir emsys
        png = os.path.join('Images', 'Emsys', 'Emsys_App.png')
        try:
            emsys = px.locateOnScreen(png, confidence=0.9)
        except:
            print("Não achou")
        else:
            print(emsys)
            center = px.center(emsys)
            print(center)
            px.click(center.x, center.y)
            sleep(1)
            px.click((center.x-30), (center.y-40))
            sleep(1)
            


    def verificar_se_esta_aberto(self):
        pst = imagens_Emsys()
        emsys_icon = pst.join('Emsys_App.png')
        emsys_aberto = pst.join('Emsys_aberto.png')
        emsys_login = pst.join('Emsys_Login.png')
        bd_foto = pst.join('banco_de_dados.png')
        
        condição = Emsys.verificar_fech()

        if condição == False:
            
            if Img.verifica_na_tela(emsys_aberto, 0.9) == True:
                app = False

            sleep(0.5)

            if Img.verifica_na_tela(emsys_aberto, 0.9) == False:
                """while Img.verifica_na_tela(emsys_login, 0.99) == False:
                    Img.click(emsys_icon, 0.9)
                    sleep(10)"""
                print(1)
                Img.verificar_até_achar(emsys_login, 0.99)
                print(2)
                print('pesquisando db')
                Img.verificar_até_achar(bd_foto, precisão=0.99)
                self.login()
                app = True
        else:
            app = False

        return app
        

    def login(self): 
        usuario_login = imagens_Emsys().join('usuario_login.png')
        x, y = Img.coordenadas(usuario_login, 0.9)
        px.doubleClick(x, y+20)
        px.press('del')
        px.write(self.usuario)
        sleep(0.5)
        px.press('tab')
        sleep(0.5)
        px.write(self.senha)
        sleep(0.5)
        px.press('enter')
        sleep(3)
        print('Escolhendo o posto')
        Emsys.escolher_posto(self.posto)


    def login_aberto(self):
        """Caso der problema ao entrar sem fazer login, fazer o login novamente"""
        def login_logout():
            px.press('alt')
            sleep(0.5)
            px.write('Y1')
            sleep(0.5)
            px.write('Y01')
            sleep(5)

        login_logout()

        login_image = os.path.join('Images', 'Emsys', 'Emsys_Login.png')
        while True:
            try:
                do_login = px.locateOnScreen(login_image, confidence=0.5)
            except:
                pass
            else:
                sleep(1)
                px.press('tab')
                Emsys.login(usuario=self.usuario, senha=self.senha, posto=self.posto)
                break
            sleep(1)


    def verificar_login(self):
        imagem = os.path.join('Images', 'Emsys', 'usuario_deslogado.png')
        try:
            usuario_deslogged = px.locateOnScreen(imagem, confidence=0.5)
        except Exception as e:
            print('Usuário logado')
            login = True        
        else:
            print('Usuário deslogado')
            login = False

        if login:
            if str(self.posto) == '1':
                verify_posto = os.path.join('Images', 'Emsys', 'Posto_1.png')
                try:
                    pdv_aberto = px.locateOnScreen(verify_posto, confidence=0.95)
                except:
                    px.press('alt')
                    sleep(0.2)
                    px.write('Y1')
                    sleep(0.2)
                    px.write('Y03')
                    sleep(0.2)
                    Emsys.escolher_posto(self.posto)
            
            elif str(self.posto) == '2':
                verify_posto = os.path.join('Images', 'Emsys', 'Posto_2.png')
                try:
                    verificar_posto = px.locateOnScreen(verify_posto, confidence=0.95)
                except:
                    px.press('alt')
                    sleep(0.2)
                    px.write('Y1')
                    sleep(0.2)
                    px.write('Y03')
                    sleep(0.2)
                    Emsys.escolher_posto(self.posto)

            if str(self.posto) == '3':
                verify_posto = os.path.join('Images', 'Emsys', 'Posto_3.png')
                try:
                    verificar_posto = px.locateOnScreen(verify_posto, confidence=0.95)
                except:
                    px.press('alt')
                    sleep(0.2)
                    px.write('Y1')
                    sleep(0.2)
                    px.write('Y03')
                    sleep(0.2)
                    Emsys.escolher_posto(self.posto)

        return login
        

    def verificando_abertura(self):
        condition = self.verificar_se_esta_aberto()
        if condition == False:
            condition2 = self.verificar_login()
            if condition2 == False:
                self.login_aberto()
        sleep(0.5)
        

    def escolher_posto(posto):
        #print('escolhendo o posto')
        posto_img = os.path.join('Images', 'Emsys', 'SELECT_POSTO.png')
          
        Img.verificar_até_achar(posto_img, 0.9)
        
        sleep(1)
        px.write(str(posto))
        sleep(1)
        px.press('enter')
        emsys_finally = os.path.join('Images', 'Emsys', 'Emsys_aberto.png')
        emsys_loading = os.path.join('Images', 'Emsys', 'Carregando_Emsys.png')
        
        Img.verificar_até_achar(emsys_loading, precisão=0.9)
        Img.verificar_até_sair(emsys_loading, 0.9)

        Img.verificar_até_achar(imagem=imagens_Emsys().join('gerencial.png'), precisão=0.9)
        Img.click(imagem=imagens_Emsys().join('gerencial.png'), precisão=0.9)
        Img.verificar_até_sair(imagem=imagens_Emsys().join('gerencial.png'), precisão=0.9)
        
        

    def abrir_pdv():
        pst = imagens_Emsys()
        pdv_aba = pst.join('pdv_aba.png')
        fech_aba = pst.join('fech_aba.png')
        fechamento = pst.join('aba_fech_1.png')
        
        Img.click(pdv_aba, 0.9)
        Img.click(fech_aba, 0.99)
        Img.verificar_até_achar(fechamento, 0.8)


    def run(self):
        Emsys.abrir()
        sleep(0)
        self.verificando_abertura()
        print('Emsys logado e posto selecionado e carregado!')
        Emsys.clicar_gerencial()
 

