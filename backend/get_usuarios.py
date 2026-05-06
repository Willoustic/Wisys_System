import sqlite3 as sql
import os
import hashlib

class Usuarios():
    def __init__(self):
        os.makedirs(os.path.join('backend', 'bancos'), exist_ok=True)
        self.conexao = sql.connect(os.path.join('backend', 'bancos', 'usuarios.db'))
        self.cursor = self.conexao.cursor()

    def gerar(self):
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT UNIQUE NOT NULL,
    SENHA_HASH TEXT NOT NULL,
    TIPO TEXT NOT NULL
)
""")
        self.conexao.commit()
        self.end_conection()
    

    def senha_codificada(self, senha: str):
        return hashlib.sha256(senha.encode()).hexdigest()
        

    def add_single(self, nome: str, senha: str, tipo: str):
        self.cursor.execute("""INSERT INTO Usuarios (NOME, SENHA_HASH, TIPO) VALUES (?, ?, ?)""", (nome.capitalize(), self.senha_codificada(senha), tipo))
        self.conexao.commit()
        self.end_conection()

    def del_nomes(self, cod: int):
        self.cursor.execute("DELETE FROM Usuarios WHERE id = ?", (cod,))
        self.conexao.commit()
        self.end_conection()

    def update(self, id_atual: int, nome: str, tipo: str):
        self.cursor.execute("""
        UPDATE Usuarios
        SET NOME = ?, TIPO = ?
        WHERE id = ?
        """, (nome, tipo, id_atual))

        self.conexao.commit()
        self.end_conection()


    def get_all_dados(self):
        self.cursor.execute("SELECT * FROM Usuarios")
        dados = self.cursor.fetchall()
        dados_nomes = []

        for i in dados:
            #print(i) 
            dados_nomes.append(i)

        self.end_conection()
        return dados_nomes
    
    def get_nomes(self):
        self.cursor.execute("SELECT * FROM Usuarios")
        dados = self.cursor.fetchall()
        dados_nomes = []

        for i in dados:
            #print(i[1]) 
            dados_nomes.append(i[1])

        self.end_conection()
        return dados_nomes
    
    def get_id(self, usuario):
        self.cursor.execute("SELECT * FROM Usuarios")
        dados = self.cursor.fetchall()
        dados_tipos = []

        for i in dados:
            #print({i[1]: i[2]}) 
            dados_tipos.append({i[1]: i[0]})

        for j in dados_tipos:
            try:
                cod = j[str(usuario).capitalize()]
            except:
                pass
            else:
                self.end_conection()
                break

        return cod
    

    def get_tipo(self, usuario):
        self.cursor.execute("SELECT * FROM Usuarios")
        dados = self.cursor.fetchall()
        dados_tipos = []

        for i in dados:
            #print({i[1]: i[2]}) 
            dados_tipos.append({i[1]: i[3]})

        for j in dados_tipos:
            try:
                tipo = j[usuario]
            except:
                pass
            else:
                break

        self.end_conection()
        return tipo
    

    def autenticar(self, nome: str, senha: str):
        self.cursor.execute("Select SENHA_HASH FROM Usuarios WHERE NOME = ?", (nome.capitalize(), ))

        dado = self.cursor.fetchone()
        if not dado:
            return False
        return dado[0] == self.senha_codificada(senha)
    

    def update_senha(self, id_cod: int, senha: str):
        self.cursor.execute("""
        UPDATE Usuarios
        SET SENHA_HASH = ?
        WHERE id = ?
        """, (self.senha_codificada(senha), id_cod))

        self.conexao.commit()
        self.end_conection()

    
    def end_conection(self):
        self.conexao.close()

