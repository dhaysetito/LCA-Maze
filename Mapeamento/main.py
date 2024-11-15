"""
###############################################################################
# Nome do Programa: Mapeamento Maze
# Descrição: A partir de um labirinto faz o mapeamento para diferentes buscas 
# (por profundidade, largura e A*). 
#
# Autor: Dhayse Tito e Breno
# Data de Criação: 14/11/2024
# Última Modificação: 15/11/2024
#
# Versão: 1.0
#
# Linguagem: Python
# Requisitos: Windows, Python 3 com as bibliotecas `tkinter`, `networkx` e `matplotlib` 
#
#
# Uso:
#   python main.py
#
###############################################################################
"""
from labirinto_app import LabirintoApp


def main():
    """
    Função principal para executar o programa.
    """
    labirinto = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    inicio = (1, 1)
    fim = (1, 7)

    app = LabirintoApp(labirinto, inicio, fim)

    # Escolher o tipo de busca
    busca_tipo = 1 

    caminho, mapeamento = app.executar_busca(busca_tipo)
    app.desenhar_grafo()            # Gera o grafo do labirinto
    app.mostrar_labirinto(caminho)  # Mostra o labirinto com o caminho


if __name__ == "__main__":
    main()
