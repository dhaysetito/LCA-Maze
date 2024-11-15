class MovimentacaoRobo:
    """
    Move o robô pelo labirinto, pelas setas ou por um caminho informado.
    """
    
    def __init__(self, labirinto):
        self.labirinto = labirinto

    def mover_robo(self, dx, dy, comando):
        x, y = self.labirinto.robo
        novo_x, novo_y = x + dx, y + dy

        if (0 <= novo_x < len(self.labirinto.labirinto[0]) and 0 <= novo_y < len(self.labirinto.labirinto)):
            self.labirinto.robo = (novo_x, novo_y)
            self.labirinto.canvas.coords(
                self.labirinto.robo_rect, 
                novo_x * self.labirinto.bloco_tamanho + 50, 
                novo_y * self.labirinto.bloco_tamanho + 50,
                (novo_x + 1) * self.labirinto.bloco_tamanho + 30, 
                (novo_y + 1) * self.labirinto.bloco_tamanho + 30
            )

            self.labirinto.label_comando.config(text=f"Último comando: {comando}")
            if self.labirinto.robo == self.labirinto.fim:
                print("O robô chegou ao fim do labirinto.")

    def mover_cima(self, event):
        self.mover_robo(0, -1, "Cima")

    def mover_baixo(self, event):
        self.mover_robo(0, 1, "Baixo")

    def mover_esquerda(self, event):
        self.mover_robo(-1, 0, "Esquerda")

    def mover_direita(self, event):
        self.mover_robo(1, 0, "Direita")

    def executar_caminho(self, event):
        for i in range(len(self.labirinto._caminho) - 1): 
            if self.labirinto._caminho[i][1] < self.labirinto._caminho[i + 1][1]: # para direita
                self.mover_robo(1, 0, "Direita")

            elif self.labirinto._caminho[i][1] > self.labirinto._caminho[i + 1][1]: # para esquerda
                self.mover_robo(-1, 0, "Esquerda")

            elif self.labirinto._caminho[i][0] < self.labirinto._caminho[i + 1][0]: # para baixo
                self.mover_robo(0, 1, "Baixo")
            
            else:
                self.mover_robo(0, -1, "Cima")
            
            self.labirinto.root.update()
            self.labirinto.root.after(200)