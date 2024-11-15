import networkx as nx
import matplotlib.pyplot as plt

from debug_log import debug

class LabirintoGrafo:
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.grafo = nx.Graph()
        self.positions = {}
        self._criar_nos_e_posicoes()
        self._adicionar_arestas()
        debug("Nós: ", list(self.grafo.nodes))
        debug("Arestas: ", list(self.grafo.edges))

    def get_positions(self):
        """Retorna as posições dos nós."""
        return self.positions

    def get_grafo(self):
        """Retorna o grafo."""
        return nx.to_dict_of_lists(self.grafo)
    
    def get_label(self, col, row):
        return self._coord_to_node(row, col)

    def _coord_to_node(self, row, col):
        """Converte coordenadas em um identificador de nó."""
        return f"{chr(65 + row)}{chr(65 + col)}"

    def _criar_nos_e_posicoes(self):
        """Cria os nós do grafo e define as posições para células com valor 0 (caminhos)."""
        for row in range(len(self.labirinto)):
            for col in range(len(self.labirinto[0])):
                if self.labirinto[row][col] == 0:
                    node = self._coord_to_node(row, col)
                    self.positions[node] = (col, -row)
                    self.grafo.add_node(node)

    def _adicionar_arestas(self):
        """Adiciona arestas para conectar células adjacentes horizontal e verticalmente."""
        for row in range(len(self.labirinto)):
            for col in range(len(self.labirinto[0])):
                if self.labirinto[row][col] == 0:
                    node = self._coord_to_node(row, col)
                    
                    # Conecta ao nó à direita, se existir
                    if col < len(self.labirinto[0]) - 1 and self.labirinto[row][col + 1] == 0:
                        neighbor = self._coord_to_node(row, col + 1)
                        self.grafo.add_edge(node, neighbor)
                    
                    # Conecta ao nó abaixo, se existir
                    if row < len(self.labirinto) - 1 and self.labirinto[row + 1][col] == 0:
                        neighbor = self._coord_to_node(row + 1, col)
                        self.grafo.add_edge(node, neighbor)

    def desenhar_grafo(self):
        """Desenha o grafo do labirinto com as posições definidas."""
        nx.draw(self.grafo, pos=self.positions, with_labels=True, node_size=500, 
                node_color='lightblue', font_weight='bold', font_size=10)
        plt.show()

    
