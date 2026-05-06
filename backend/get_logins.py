import sqlite3
import os

class Portal():
    def __init__(self):
        self.conexao = sqlite3.connect(os.path.join('backend', 'bancos', 'portais.db'))
        self.cursor = self.conexao.cursor()

    def get_portal(self, portal, posto):
        self.cursor.execute(f"SELECT * FROM Posto_{posto} WHERE Portal = '{str(portal).upper()}'")
        dados = self.cursor.fetchall()
        dados = dados[0]
        portal = dados[1]
        login = dados[2]
        senha = dados[3]

        return login, senha
    