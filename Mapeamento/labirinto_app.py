import tkinter as tk
from debug_log import debug

from grafo import LabirintoGrafo
from buscas import busca_profundidade
from labirinto_figure import Labirinto

class LabirintoApp:
    """
    Classe principal para encapsular a lógica do labirinto e suas operações.
    """
    def __init__(self, labirinto, inicio, fim):
        self.labirinto = labirinto
        self.inicio = inicio
        self.fim = fim

    def desenhar_grafo(self):
        """
        Gera a representação do grafo do labirinto.
        """
        grafo_labirinto = LabirintoGrafo(self.labirinto)
        grafo_labirinto.desenhar_grafo()

    def mostrar_labirinto(self, caminho):
        """
        Gera a interface gráfica para exibir o labirinto e o caminho encontrado.
        """
        root = tk.Tk()
        app = Labirinto(root, self.labirinto, caminho, self.inicio, self.fim)
        root.mainloop()

    def executar_busca(self, busca_tipo):
        """
        Executa uma busca no grafo do labirinto.
        Retorna o caminho e o mapeamento.
        Arg:
            busca_tipo (int): 1 - Busca por profundidade, 2 - Busca por largura, 3 - Busca A*
        """
        grafo_labirinto = LabirintoGrafo(self.labirinto)
        positions = grafo_labirinto.get_positions()
        grafo = grafo_labirinto.get_grafo()

        _inicio = grafo_labirinto.get_label(self.inicio[0], self.inicio[1])
        _fim = grafo_labirinto.get_label(self.fim[0], self.fim[1])

        debug("Positions:", positions)
        debug('-------------------------')
        debug("Grafo:", grafo)
        debug('-------------------------')

        if busca_tipo == 1:  # Busca por profundidade
            caminho, percurso = busca_profundidade(grafo, _inicio, _fim)
        else:
            caminho, percurso = None, None

        debug("Caminho:", caminho)
        debug("Percurso:", percurso)

        return caminho, percurso
