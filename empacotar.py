"""
FarmTech Solutions - Gera o ZIP final da entrega.
Roda com: python empacotar.py
"""

import os
import zipfile

PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__))
NOME_ZIP = "farmtech-solutions-entrega.zip"

IGNORAR_PASTAS = {".git", "__pycache__"}
IGNORAR_ARQUIVOS = {NOME_ZIP, os.path.basename(__file__)}


def deve_incluir(caminho_relativo):
    partes = caminho_relativo.split(os.sep)
    if any(parte in IGNORAR_PASTAS for parte in partes):
        return False
    if os.path.basename(caminho_relativo) in IGNORAR_ARQUIVOS:
        return False
    return True


def gerar_zip():
    caminho_zip = os.path.join(PASTA_PROJETO, NOME_ZIP)
    with zipfile.ZipFile(caminho_zip, "w", zipfile.ZIP_DEFLATED) as zip_arquivo:
        for raiz, pastas, arquivos in os.walk(PASTA_PROJETO):
            pastas[:] = [p for p in pastas if p not in IGNORAR_PASTAS]
            for nome_arquivo in arquivos:
                caminho_completo = os.path.join(raiz, nome_arquivo)
                caminho_relativo = os.path.relpath(caminho_completo, PASTA_PROJETO)
                if deve_incluir(caminho_relativo):
                    zip_arquivo.write(caminho_completo, caminho_relativo)
                    print(f"Adicionado: {caminho_relativo}")

    print(f"\nZIP gerado em: {caminho_zip}")


if __name__ == "__main__":
    gerar_zip()
