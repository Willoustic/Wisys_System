import sqlite3 as sql
import os

class Banco():
    def __init__(self):
        os.makedirs(f'{os.path.join('backend')}\\bancos', exist_ok=True)
        self.conexao = sql.connect(os.path.join('backend', 'bancos', 'postos.db'))
        self.cursor = self.conexao.cursor()


    def gerar(self):
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS Postos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    tipo TEXT NOT NULL
)
""")
        self.conexao.commit()


    def add_posto(self, nome: str, tipo):
        self.cursor.execute("""
INSERT INTO Postos (nome, tipo)
VALUES (?, ?)
""", (nome, tipo))
        self.conexao.commit()


    def get_class(self, posto):
        self.cursor.execute("SELECT * FROM Postos")
        dados = self.cursor.fetchall()
        dados_tipos = []

        for i in dados:
            #print({i[1]: i[2]}) 
            dados_tipos.append({i[1]: i[2]})


        for j in dados_tipos:
            try:
                tipo = j[posto]
            except:
                pass
            else:
                break

        return tipo

    
    def get_nomes(self):
        self.cursor.execute("SELECT * FROM Postos")
        dados = self.cursor.fetchall()
        dados_nomes = []

        for i in dados:
            #print(i[1]) 
            dados_nomes.append(i[1])

        return dados_nomes
    
    def get_id(self, posto):
        self.cursor.execute("SELECT * FROM Postos")
        dados = self.cursor.fetchall()
        dados_tipos = []

        for i in dados:
            #print({i[1]: i[2]}) 
            dados_tipos.append({i[1]: i[0]})


        for j in dados_tipos:
            try:
                cod = j[posto]
            except:
                pass
            else:
                break

        return cod


    def del_nomes(self, cod: int):
        self.cursor.execute("DELETE FROM Postos WHERE id = ?", (cod,))
        self.conexao.commit()


    def update_dados(self, cod: int, nome: str, tipo: str):
        self.cursor.execute("""
        UPDATE Postos
        SET id = ?, tipo = ?
        WHERE nome = ?
        """, (cod, tipo, nome))

        self.conexao.commit()

    def end_conection(self):
        self.conexao.close()








        



