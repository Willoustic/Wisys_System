import os
import shutil
from pathlib import Path
from .CTe_Clicks import Clicks
from CTe_Auto.Xml.read_xml import Ler_cte


class Auto_CTe():
    @staticmethod
    def run():
        xml = Ler_cte()
        if xml.condition == True:
            if xml.uf_destino == xml.uf_origem:
                natureza_da_operacao = "DE"
            else:
                natureza_da_operacao = "FE"
        
            # Limpar tela
            Clicks.limpar_tela()

            # Tela conhecimento
            Clicks.digitar_n_conhecimento(n_conhecimento=xml.numero)
            Clicks.digitar_serie(n_serie=xml.serie)
            Clicks.digitar_transportadora()
            Clicks.digitar_datas(data_emi=xml.emissao)
            Clicks.modelo_documento()
            Clicks.modal_transp()
            Clicks.clicar_natureza_operac(tipo=natureza_da_operacao)
            Clicks.tribut_pis()
            Clicks.tribut_cofins()
            Clicks.digitar_chave(xml.chave)
            Clicks.selec_nat_frete()
            Clicks.digitar_cidade_destino(xml.cidade_destino)
            Clicks.digitar_cidade_origem(xml.cidade_origem)


            # Tela valores
            Clicks.clicar_valores()
            Clicks.botar_total_frete(xml.valor)
            Clicks.apagar_valor_pis()
            Clicks.apagar_valor_cofins()

            # Tela pagamento
            Clicks.clicar_pagamento()
            Clicks.selec_tipo_cobranc()
            Clicks.add_vencimento(data_emi=xml.emissao)
            Clicks.get_valor_cobranca()
            Clicks.incluir_vencimento()
            Clicks.incluir_centro_e_rateio()
            Clicks.inserir_rateio()

            # Incluir CTe
            Clicks.incluir_cte()

    @staticmethod
    def run_pasta(pasta, subpasta="Feitos"):
        pasta_path = Path(pasta)
        destino = pasta_path / subpasta
        destino.mkdir(parents=True, exist_ok=True)

        xmls = sorted(pasta_path.glob("*.xml"))

        resumo = {"processados": [], "erros": [], "movidos": []}

        for arquivo in xmls:
            try:
                xml = Ler_cte(caminho=str(arquivo))
                if xml.condition is not True:
                    resumo["erros"].append({"arquivo": arquivo.name, "erro": "XML inválido"})
                    continue

                if xml.uf_destino == xml.uf_origem:
                    natureza_da_operacao = "DE"
                else:
                    natureza_da_operacao = "FE"

                Clicks.limpar_tela()

                Clicks.digitar_n_conhecimento(n_conhecimento=xml.numero)
                Clicks.digitar_serie(n_serie=xml.serie)
                Clicks.digitar_transportadora()
                Clicks.digitar_datas(data_emi=xml.emissao)
                Clicks.modelo_documento()
                Clicks.modal_transp()
                Clicks.clicar_natureza_operac(tipo=natureza_da_operacao)
                Clicks.tribut_pis()
                Clicks.tribut_cofins()
                Clicks.digitar_chave(xml.chave)
                Clicks.selec_nat_frete()
                Clicks.digitar_cidade_destino(xml.cidade_destino)
                Clicks.digitar_cidade_origem(xml.cidade_origem)

                Clicks.clicar_valores()
                Clicks.botar_total_frete(xml.valor)
                Clicks.apagar_valor_pis()
                Clicks.apagar_valor_cofins()

                Clicks.clicar_pagamento()
                Clicks.selec_tipo_cobranc()
                Clicks.add_vencimento(data_emi=xml.emissao)
                Clicks.get_valor_cobranca()
                Clicks.incluir_vencimento()
                Clicks.incluir_centro_e_rateio()
                Clicks.inserir_rateio()

                Clicks.incluir_cte()

                caminho_destino = destino / arquivo.name
                if caminho_destino.exists():
                    base = arquivo.stem
                    ext = arquivo.suffix
                    i = 1
                    while (destino / f"{base}_{i}{ext}").exists():
                        i += 1
                    caminho_destino = destino / f"{base}_{i}{ext}"

                shutil.move(str(arquivo), str(caminho_destino))
                resumo["processados"].append(arquivo.name)
                resumo["movidos"].append(str(caminho_destino))
            except Exception as e:
                resumo["erros"].append({"arquivo": arquivo.name, "erro": str(e)})

        return resumo
