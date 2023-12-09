class Grafo:
    def __init__(self, V):
        # Inicializa o grafo com o número de vértices V
        self.V = V
        # Cria um dicionário de adjacência para representar as arestas do grafo
        self.adj = {v: [] for v in range(V)}
        # Cria um dicionário para armazenar o grau de cada vértice
        self.grau = {v: 0 for v in range(V)}

    def adicionar_aresta(self, u, v):
        # Adiciona uma aresta entre os vértices u e v
        self.adj[u].append(v)
        self.adj[v].append(u)
        # Atualiza os graus dos vértices
        self.grau[u] += 1
        self.grau[v] += 1

    def remover_arestas(self, vertice):
        # Remove as arestas incidentes no vértice e atualiza os graus
        for adjacente in self.adj[vertice]:
            self.grau[adjacente] -= 1
            self.adj[adjacente].remove(vertice)
        self.grau[vertice] = 0
        self.adj[vertice] = []

    def encontrar_cobertura_minima(self):
        # Ordena os vértices pelo grau em ordem decrescente
        vertices_ordenados = sorted(self.grau, key=lambda x: self.grau[x], reverse=True)
        cobertura = []

        # Enquanto ainda houver arestas no grafo
        while any(self.adj.values()):
            # Escolhe o vértice de maior grau
            vertice = vertices_ordenados[0]
            cobertura.append(vertice)
            # Remove as arestas incidentes no vértice escolhido
            self.remover_arestas(vertice)
            # Reordena os vértices pelo grau
            vertices_ordenados = sorted(self.grau, key=lambda x: self.grau[x], reverse=True)

        return cobertura


if __name__ == "__main__":
    # Solicita ao usuário o número de vértices e arestas
    V = int(input("Digite o número de vértices: "))
    E = int(input("Digite o número de arestas: "))
    
    # Criação do objeto Grafo
    grafo = Grafo(V)

    # Adição das arestas ao grafo
    print("Digite os pares de arestas (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        grafo.adicionar_aresta(u, v)

    # Encontrar a cobertura mínima e imprimir os vértices resultantes
    cobertura = grafo.encontrar_cobertura_minima()
    print("Vertices para cobertura mínima:", cobertura)
