"""
Este módulo organiza arquivos em um diretório selecionado com base nas extensões de arquivo.
Utiliza a biblioteca tkinter.filedialog para permitir ao usuário escolher um diretório e, 
em seguida, organiza os arquivos
nesse diretório em subdiretórios específicos com base nas extensões de arquivo.
Os subdiretórios são nomeados "Torrents," "Zips," "PDFs" e "Exec."
"""

import os
from tkinter.filedialog import askdirectory

# Função para organizar os arquivos em subdiretórios


def organizar_arquivos(caminho):
    """
    Organiza os arquivos em subdiretórios com base em suas extensões.

    Args:
        caminho (str): O caminho do diretório a ser organizado.
    """
    lista_arquivos = os.listdir(caminho)

    locais = {
        "Torrents": [".torrent"],
        "Zips": [".zip", ".rar"],
        "PDFs": [".pdf"],
        "Exec": [".exe"]
    }

    for arquivo in lista_arquivos:
        _, extensao = os.path.splitext(arquivo)
        for pasta, extensoes in locais.items():
            if extensao in extensoes:
                pasta_destino = os.path.join(caminho, pasta)
                if not os.path.exists(pasta_destino):
                    os.mkdir(pasta_destino)
                origem_arquivo = os.path.join(caminho, arquivo)
                destino_arquivo = os.path.join(pasta_destino, arquivo)
                os.rename(origem_arquivo, destino_arquivo)


if __name__ == "__main__":
    caminho = askdirectory(title="Selecione uma pasta")

    if caminho:
        organizar_arquivos(caminho)
