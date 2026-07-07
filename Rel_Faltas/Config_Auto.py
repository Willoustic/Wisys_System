from .Config_Clicks import Clicks_Sistema, MsgToWhatsapp
from Emsys.login_emsys import Emsys

class Enviar_Relatório_de_Faltas():
    def __init__(self, cod_posto, usuario, senha):
        Emsys(posto=cod_posto, name=usuario, password=senha).run()
        clicks = Clicks_Sistema(cod_posto)
        clicks.config_all()
        try:
            MsgToWhatsapp(cod_posto, clicks.nome_arquivo).config()
        except Exception as e:
            print(e)
