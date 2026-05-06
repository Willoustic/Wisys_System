"""PROGRAMA PARA RODAR PROGRAMA NO CHROME"""

from time import sleep
import pyautogui as px
from backend.get_logins import Portal
from Sites.chrome import abrir_chrome
from Sites.url_sites import Site
from Sangrias.autom.auto import caps_lock_ativado

site = Site()
portal = Portal()

def pesquisar_elemento_da_pagina(elemento):
    """PESQUISA SOBRE O ELEMENTO DA TELA (CHROME)"""
    px.hotkey('ctrl', 'f')
    px.write(str(elemento))
    px.press('esc')

def recarregar():
    """APERTA F5 PARA RECARREGAR A TELA"""
    px.press('f5')

class Chrome():
    """TORNA O OBJETO EM UM AUTOMATIZADOR DO CHROME"""
    def __init__(self, cod):
        self.posto = cod
        abrir_chrome("https://mail.google.com/mail/u/0/#inbox")
        sleep(0.2)
        abrir_chrome("https://mail.google.com/mail/u/1/#inbox")
        sleep(0.2)
        abrir_chrome("https://mail.google.com/mail/u/2/#inbox")
        sleep(2)


    def cielo(self):
        """USA O CHROME PARA ENTRAR NA CIELO"""
        login, senha = portal.get_portal("cielo", self.posto)
        abrir_chrome(site.cielo)
        sleep(3)
        pesquisar_elemento_da_pagina('cpf')
        sleep(1)
        px.write(login)
        pesquisar_elemento_da_pagina('entrar')
        px.press('enter')
        for i in range(0, 3):
            px.press('tab')
        px.press('space')
        sleep(10)
        pesquisar_elemento_da_pagina('entrar')
        px.press('enter')


    def wizeo(self):
        """USA O CHROME PARA ENTRAR NA WIZEO"""
        abrir_chrome(site.wizeo)


    def fancard(self):
        """USA O CHROME PARA ENTRAR NA FANCARD"""
        # Sessão de Login
        login, senha = portal.get_portal("fancard", self.posto)
        abrir_chrome(site.fancard)
        sleep(1)
        pesquisar_elemento_da_pagina('sair')
        px.press('enter')
        sleep(1)
        recarregar()
        sleep(1)
        pesquisar_elemento_da_pagina('lojista')
        px.press('enter')
        sleep(1)
        pesquisar_elemento_da_pagina('codigo da loja')
        px.press('tab')
        px.write(login)
        px.press('tab')
        px.write(senha)
        px.press('tab')
        px.press('enter')

        # aba relatórios
        sleep(3)
        pesquisar_elemento_da_pagina('relatorios')

        px.press('enter')
        sleep(2)
        pesquisar_elemento_da_pagina('relatorio de vendas')
        px.press('enter')


    def prime(self):
        """USA O CHROME PARA ENTRAR NA PRIME"""
        login, senha = portal.get_portal("prime", self.posto)
        abrir_chrome(site.prime)
        sleep(3)
        pesquisar_elemento_da_pagina('sair')
        px.press('enter')
        sleep(1)
        pesquisar_elemento_da_pagina('credenciado')
        px.press('tab')
        px.press('enter')
        sleep(1)
        recarregar()
        px.press('enter')
        sleep(1)
        px.press('tab')
        px.press('tab')
        px.hotkey('ctrl', 'a')
        px.press('del')
        px.hotkey('shift', 'tab')
        for i in range(0, 2):
            px.write(login)
            px.press('tab')
        px.write(senha)
        px.press('tab')
        px.press('enter')

        # abrir rel de vendas
        sleep(5)
        recarregar()
        sleep(1)
        pesquisar_elemento_da_pagina('vendas')
        px.press('enter')


    def link(self):
        """USA O CHROME PARA ENTRAR NA LINK"""
        login, senha = portal.get_portal("link", self.posto)
        abrir_chrome(site.link)
        sleep(2)
        pesquisar_elemento_da_pagina('sair')
        px.press('enter')

        sleep(1)
        recarregar()
        sleep(1)
        for i in range(0, 4):
            px.press('tab')

        px.write(login)
        px.press('tab')
        px.write(login)
        px.press('tab')
        px.write(senha)
        px.press('tab')
        px.press('enter')

        sleep(5)
        recarregar()
        sleep(1)
        pesquisar_elemento_da_pagina('vendas')
        px.press('enter')


    def neo(self):
        """USA O CHROME PARA ENTRAR NA NEO"""
        login, senha = portal.get_portal("neo", self.posto)
        abrir_chrome(site.neo)

        sleep(2)
        pesquisar_elemento_da_pagina('sair')
        px.press('enter')

        sleep(1)
        recarregar()
        sleep(1)
        for i in range(0, 1):
            px.press('tab')

        px.write(login)
        px.press('tab')
        px.write(login)
        px.press('tab')
        px.write(senha)
        px.press('tab')
        px.press('enter')

        sleep(5)
        recarregar()
        sleep(2)
        pesquisar_elemento_da_pagina('vendas')
        px.press('enter')


    def agilli(self):
        """USA O CHROME PARA ENTRAR NA AGILLI"""
        login, senha = portal.get_portal("agilli", self.posto)
        abrir_chrome(site.agilli)
        sleep(6)
        px.hotkey('ctrl', 'a')
        px.write(login)
        px.press('tab')
        px.write(senha)
        px.press('tab')
        px.press('enter')
        sleep(5)
        px.hotkey('ctrl', 'l')
        sleep(0.7)
        px.write(site.agilli_vendas)
        sleep(1)
        px.press('enter')


    def ctf(self):
        """USA O CHROME PARA ENTRAR NA CTF"""
        login, senha = portal.get_portal("ctf", self.posto)
        abrir_chrome(site.ctf)
        sleep(1)
        pesquisar_elemento_da_pagina('cliente ctf')
        px.press('enter')

        sleep(3)
        px.press('tab')
        px.write(login)
        px.press('tab')
        px.write(senha)


    def qrlinx(self):
        """USA O CHROME PARA ENTRAR NA QRLINX"""
        login, senha = portal.get_portal('qrlinx', self.posto)
        abrir_chrome(site.qrlinx)
        sleep(1)
        px.hotkey('ctrl', 'a')
        px.write(login)
        px.press('tab')
        px.write(senha)
        px.press('tab')
        px.press('space')


    def ticket(self):
        """USA O CHROME PARA ENTRAR NA TICKET"""
        login, senha = portal.get_portal('ticket', self.posto)
        abrir_chrome(site.ticket)
        sleep(6)
        pesquisar_elemento_da_pagina('email')
        px.press('tab')
        px.write(login)
        px.press('tab')
        px.write(senha)
        pesquisar_elemento_da_pagina('entrar')
        px.press('enter')


    def policard(self):
        """USA O CHROME PARA ENTRAR NA POLICARD"""
        login, senha = portal.get_portal('policard', self.posto)
        abrir_chrome(site.policard)
        sleep(3)
        px.hotkey('ctrl', 'a')
        px.press('del')
        px.write(login)
        px.press('tab')
        px.hotkey('ctrl', 'a')
        px.write(senha)
        px.press('tab')
        
        pesquisar_elemento_da_pagina('entrar')
        px.press('enter')

        sleep(3)


    def vibra(self):
        """USA O CHROME PARA ENTRAR NA VIBRA"""

        login, senha = portal.get_portal('vibra', self.posto)
        abrir_chrome(site.vibra)
        sleep(3)
        px.press('tab')
        px.hotkey('ctrl', 'a')
        px.write(login)
        sleep(0.5)
        px.press('tab')
        sleep(0.5)
        px.write(senha)
        sleep(0.5)
        px.press('tab')
        sleep(0.5)
        px.press('enter')
        sleep(5)
        abrir_chrome(site.vibra_config)
        sleep(5)
        pesquisar_elemento_da_pagina('conferencia')
        sleep(0.5)
        px.press('enter')


    def stone(self):
        """USA O CHROME PARA ENTRAR NA STONE"""
        abrir_chrome(site.stone)


    def frota_flex(self):
        abrir_chrome(site.frota)



class BotMaster():
    """USA O CHROME E O PYAUTOGUI PARA AUTOMATIZAR TAREFAS"""
    def __init__(self, cod):
        if caps_lock_ativado() is True:
            px.press('CAPSLOCK')

        self.cod = cod
        self.bot = Chrome(cod)

    def run(self):
        """ESCOLHE A EXECUÇÃO QUE VAI FAZER"""
        if self.cod == 1:
            self.zn()
        elif self.cod == 2:
            self.zs()
        elif self.cod == 3:
            self.pv()
        else:
            print('Dados inválidos')

    def zn(self):
        """USA O CHROME PARA ACESSAR CARTÕES DA ZN"""
        self.bot.cielo()
        sleep(2)
        self.bot.agilli()
        sleep(2)
        self.bot.wizeo()
        sleep(2)
        self.bot.fancard()
        sleep(2)
        self.bot.prime()
        sleep(2)
        self.bot.link()
        sleep(2)
        self.bot.neo()
        sleep(2)
        self.bot.ctf()
        sleep(2)
        self.bot.ticket()
        sleep(2)
        self.bot.qrlinx()
        sleep(2)
        self.bot.frota_flex()


    def pv(self):
        """USA O CHROME PARA ACESSAR CARTÕES DO PV"""
        self.bot.cielo()
        sleep(2)
        self.bot.agilli()
        sleep(2)
        self.bot.wizeo()
        sleep(2)
        self.bot.fancard()
        sleep(2)
        self.bot.prime()
        sleep(2)
        self.bot.link()
        sleep(2)
        self.bot.neo()
        sleep(2)
        self.bot.ctf()
        sleep(2)
        self.bot.ticket()
        sleep(2)
        self.bot.stone()
        sleep(2)
        self.bot.vibra()
        sleep(2)
        self.bot.frota_flex()


    def zs(self):
        """USA O CHROME PARA ACESSAR CARTÕES DA ZS"""
        self.bot.cielo()
        sleep(2)
        self.bot.agilli()
        sleep(2)
        self.bot.wizeo()
        sleep(2)
        self.bot.fancard()
        sleep(2)
        self.bot.prime()
        sleep(2)
        self.bot.link()
        sleep(2)
        self.bot.neo()
        sleep(2)
        self.bot.ctf()
        sleep(2)
        self.bot.ticket()
        sleep(2)
        self.bot.qrlinx()
        sleep(2)
        self.bot.policard()
        sleep(2)
        self.bot.frota_flex()