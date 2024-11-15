from grafo import LabirintoGrafo

def busca_profundidade(grafo, inicio, objetivo, caminho=None, visitados=None, percurso=None):
    """
    Algoritmo de busca por profundidade, retorna o caminho (sequencia de nós até o objetivo) e
    percurso (sequencia de nós de toda a busca).
    """
    if caminho is None:
        caminho = [inicio]
    if visitados is None:
        visitados = set()
    if percurso is None:
        percurso = []

    visitados.add(inicio)
    percurso.append(inicio)  

    if inicio == objetivo:
        return caminho, percurso

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            resultado, percurso = busca_profundidade(grafo, vizinho, objetivo, caminho + [vizinho], visitados, percurso)
            if resultado:  
                return resultado, percurso
            percurso.append(inicio)
            
    return None, percurso 



if __name__ == "__main__":
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
    
    labirinto_grafo = LabirintoGrafo(labirinto)

    positions = labirinto_grafo.get_positions()
    grafo = labirinto_grafo.get_grafo()

    print("Positions:", positions)
    print('------------------------- \n')
    print("Grafo:", grafo)
    print('------------------------- \n')

    caminho, percurso = busca_profundidade(grafo,"BB", "HB")
    print(caminho)
    print(percurso)