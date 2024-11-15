import tkinter as tk
import string
from movimentacao_robo import MovimentacaoRobo

class Labirinto:
    def __init__(self, root, labirinto, caminho, inicio, fim):
        self.root = root
        self.root.title("Labirinto")

        self.labirinto = labirinto

        self.largura = len(self.labirinto[0])
        self.altura = len(self.labirinto)
        self.bloco_tamanho = 40

        self.canvas = tk.Canvas(root, width=self.largura * self.bloco_tamanho + 40,
                                height=self.altura * self.bloco_tamanho + 40, bg="white")
        self.canvas.pack()

        self.inicio = inicio
        self.fim = fim
        self.robo = self.inicio

        self._caminho = caminho

        self.desenhar_labirinto()
        self.desenhar_robo()

        self.movimentacao = MovimentacaoRobo(self)
        self.root.bind("<Up>", self.movimentacao.mover_cima)
        self.root.bind("<Down>", self.movimentacao.mover_baixo)
        self.root.bind("<Left>", self.movimentacao.mover_esquerda)
        self.root.bind("<Right>", self.movimentacao.mover_direita)
        self.root.bind("p", self.movimentacao.executar_caminho)

        self.label_comando = tk.Label(root, text="Último comando: Nenhum")
        self.label_comando.pack()

        self.botao_reiniciar = tk.Button(root, text="Reiniciar", command=self.reiniciar_jogo)
        self.botao_reiniciar.pack()

    def desenhar_labirinto(self):
        # Desenha rótulos dos eixos (A, B, C, ...)
        letras = string.ascii_uppercase

        # Rótulos para o eixo x (horizontal)
        for x in range(self.largura):
            self.canvas.create_text(x * self.bloco_tamanho + 60, 20, text=letras[x], font=("Arial", 12, "bold"))

        # Rótulos para o eixo y (vertical)
        for y in range(self.altura):
            self.canvas.create_text(20, y * self.bloco_tamanho + 60, text=letras[y], font=("Arial", 12, "bold"))

        # Desenha o labirinto
        for y, linha in enumerate(self.labirinto):
            for x, bloco in enumerate(linha):
                if bloco == 1:
                    self.canvas.create_rectangle(x * self.bloco_tamanho + 40, y * self.bloco_tamanho + 40,
                                                 (x + 1) * self.bloco_tamanho + 40, (y + 1) * self.bloco_tamanho + 40,
                                                 fill="black")

        # Desenha o quadrado azul para o início
        x, y = self.inicio
        self.canvas.create_rectangle(x * self.bloco_tamanho + 40, y * self.bloco_tamanho + 40,
                                     (x + 1) * self.bloco_tamanho + 40, (y + 1) * self.bloco_tamanho + 40,
                                     fill="blue")

        # Desenha o quadrado vermelho para o fim
        x, y = self.fim
        self.canvas.create_rectangle(x * self.bloco_tamanho + 40, y * self.bloco_tamanho + 40,
                                     (x + 1) * self.bloco_tamanho + 40, (y + 1) * self.bloco_tamanho + 40,
                                     fill="red")

    def desenhar_robo(self):
        """
        Desenha o robô redondo e verde.
        """
        x, y = self.robo
        self.robo_rect = self.canvas.create_oval(x * self.bloco_tamanho + 50, y * self.bloco_tamanho + 50,
                                                    (x + 1) * self.bloco_tamanho + 30, (y + 1) * self.bloco_tamanho + 30,
                                                    fill="green")

    def reiniciar_jogo(self):
        """
        Reinicia o jogo, retornando o robo para a posição inicial e limpando o comando.
        """
        self.robo = self.inicio
        self.canvas.coords(self.robo_rect, self.robo[0] * self.bloco_tamanho + 50, 
                           self.robo[1] * self.bloco_tamanho + 50,
                           (self.robo[0] + 1) * self.bloco_tamanho + 30, 
                           (self.robo[1] + 1) * self.bloco_tamanho + 30)
        self.label_comando.config(text="Último comando: Nenhum")