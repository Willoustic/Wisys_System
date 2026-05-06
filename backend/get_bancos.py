import sqlite3 as sql
import os
import hashlib

class Mnemonicos():
    def __init__(self):
        os.makedirs(os.path.join('backend', 'bancos'), exist_ok=True)
        self.conexao = sql.connect(os.path.join('backend', 'bancos', 'bancos.db'))
        self.cursor = self.conexao.cursor()

    def gerar(self, cod_posto):
        self.cursor.execute(f"""
CREATE TABLE IF NOT EXISTS Posto_{cod_posto} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT UNIQUE NOT NULL,
)
""")
        self.conexao.commit()
        self.end_conection()
        

    def add_single(self, nome: str, senha: str, tipo: str, cod_posto):
        self.cursor.execute(f"""INSERT INTO Posto_{cod_posto} (NOME) VALUES (?)""", (nome, ))
        self.conexao.commit()
        self.end_conection()

    def del_nomes(self, cod: int, cod_posto):
        self.cursor.execute(f"DELETE FROM Posto_{cod_posto} WHERE id = ?", (cod,))
        self.conexao.commit()
        self.end_conection()

    def update(self, id_atual: int, nome: str, cod_posto):
        self.cursor.execute(f"""
        UPDATE Posto_{cod_posto}
        SET NOME = ?=
        WHERE id = ?
        """, (nome, id_atual))

        self.conexao.commit()
        self.end_conection()


    def get_all_dados(self, cod_posto):
        self.cursor.execute(f"SELECT * FROM Posto_{cod_posto}")
        dados = self.cursor.fetchall()
        dados_nomes = []

        for i in dados:
            #print(i) 
            dados_nomes.append(i)

        self.end_conection()
        return dados_nomes
    
    def get_nomes(self, cod_posto):
        self.cursor.execute(f"SELECT * FROM Posto_{cod_posto}")
        dados = self.cursor.fetchall()
        dados_nomes = []

        for i in dados:
            #print(i[1]) 
            dados_nomes.append(i[1])

        self.end_conection()
        return dados_nomes
    
    def get_id(self, banco, cod_posto):
        self.cursor.execute(f"SELECT * FROM Posto_{cod_posto}")
        dados = self.cursor.fetchall()
        dados_tipos = []

        for i in dados:
            #print({i[1]: i[2]}) 
            dados_tipos.append({i[1]: i[0]})

        for j in dados_tipos:
            try:
                cod = j[banco]
            except:
                pass
            else:
                self.end_conection()
                break

        return cod
    

    def end_conection(self):
        self.conexao.close()

