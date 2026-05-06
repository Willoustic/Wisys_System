import tkinter as tk
from tkinter import filedialog, messagebox
import xml.etree.ElementTree as ET
from datetime import datetime


def get_text(root, path, ns):
    elemento = root.find(path, ns)
    return elemento.text if elemento is not None else ""

class Ler_cte():
    def __init__(self):
        # Abre seletor de arquivo
        caminho = filedialog.askopenfilename(
            title="Selecionar arquivo CT-e",
            filetypes=[("Arquivos XML", "*.xml")]
        )

        try:
            tree = ET.parse(caminho)
            root = tree.getroot()

            # Namespace obrigatório do CT-e
            ns = {"cte": "http://www.portalfiscal.inf.br/cte"}

            numero = get_text(root, ".//cte:ide/cte:nCT", ns)
            emissao = get_text(root, ".//cte:ide/cte:dhEmi", ns)
            emitente = get_text(root, ".//cte:emit/cte:xNome", ns)
            destinatario = get_text(root, ".//cte:dest/cte:xNome", ns)
            valor = get_text(root, ".//cte:vPrest/cte:vTPrest", ns)
            cidade_origem = get_text(root, ".//cte:ide/cte:xMunIni", ns)
            uf_origem = get_text(root, ".//cte:ide/cte:UFIni", ns)
            chave = get_text(root, ".//cte:protCTe/cte:infProt/cte:chCTe", ns)
            serie = get_text(root, ".//cte:ide/cte:serie", ns)
            cidade_destino = get_text(root, ".//cte:ide/cte:xMunFim", ns)
            uf_destino = get_text(root, ".//cte:ide/cte:UFFim", ns)

            if emissao:
                emissao = datetime.fromisoformat(emissao).strftime("%d/%m/%Y")

            self.numero = numero
            self.emissao = emissao
            self.emitente = emitente
            self.destinatario = destinatario
            self.valor = float(valor)
            self.cidade_origem = cidade_origem
            self.uf_origem = uf_origem
            self.chave = chave
            self.serie = serie
            self.cidade_destino = cidade_destino
            self.uf_destino = uf_destino
            self.cidade_destino_total = f"{cidade_destino} - {uf_destino}"
            self.cidade_origem_total = f"{cidade_origem} - {uf_origem}"
            self.condition = True

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler XML como CTe:\n{e}")
            self.condition = False


    def get_all_info(self):
        try:
            info = {
                'Número CT-e': f'{self.numero}',
                'Chave': f'{self.chave}',
                'Serie': f'{self.serie}',
                'Emissão': f'{self.emissao}',
                'Emitente': f'{self.emitente}',
                'Destinatário': f'{self.destinatario}',
                'Valor': f'{float(self.valor):.2f}',
                'Cidade Origem': f'{self.cidade_origem} - {self.uf_origem}',
                'Cidade Destino': f'{self.cidade_destino} - {self.uf_destino}'
                }

            messagebox.showinfo("CT-e carregado", info)
        
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler XML como CTe:\n{e}")

# exemplo de como deve ser       
"""xml = Ler_cte()
xml.get_all_info()
print(xml.numero)"""
