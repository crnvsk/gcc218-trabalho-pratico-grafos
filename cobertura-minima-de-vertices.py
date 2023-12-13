import sys

class Grafo:
    def __init__(self, V, inicial=0):
        # Inicializa o grafo com um número de vértices V
        self.V = V
        self.inicial = inicial
        # Cria um dicionário de adjacência para representar as arestas do grafo
        self.adj = {v: [] for v in range(inicial, inicial + V)}
        # Cria um dicionário para armazenar o grau de cada vértice
        self.grau = {v: 0 for v in range(inicial, inicial + V)}

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

        # Enquanto ainda houverem arestas no grafo
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
    # Verifica se o nome do arquivo foi fornecido como argumento de linha de comando
    if len(sys.argv) != 2:
        print("insira no terminal: python nome_do_programa.py nome_do_arquivo.txt")
        sys.exit(1)

    nome_arquivo = sys.argv[1]

    # Lê as entradas do arquivo especificado na linha de comando
    with open(nome_arquivo, "r") as file:
        V, E, inicial = map(int, file.readline().strip().split())

        grafo = Grafo(V, inicial)
        for _ in range(E):
            u, v = map(int, file.readline().strip().split())
            if inicial <= u <= inicial + V - 1 and inicial <= v <= inicial + V - 1:
                grafo.adicionar_aresta(u, v)
            else:
                print("Entrada inválida. Certifique-se de que está dentro do intervalo especificado.")

        cobertura = grafo.encontrar_cobertura_minima()
        print("Vertices para cobertura mínima:", cobertura)
