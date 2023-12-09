# Implementação por força bruta, testando todas as possibilidades, sem a utilização da heurística gulosa para encontrar a cobertura mínima de vértices.
# Problema NP-Completo.
# A solução tem complexidade de O(V!).

class Grafo:
    def __init__(self, V, inicial=0):
        self.V = V
        self.inicial = inicial
        self.adj = {v: [] for v in range(inicial, inicial + V)}
        self.grau = {v: 0 for v in range(inicial, inicial + V)}

    def adicionar_aresta(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.grau[u] += 1
        self.grau[v] += 1

    def remover_arestas(self, vertice):
        for adjacente in self.adj[vertice]:
            self.grau[adjacente] -= 1
            self.adj[adjacente].remove(vertice)
        self.grau[vertice] = 0
        self.adj[vertice] = []

    def encontrar_cobertura_minima_bruta(self):
        menor_cobertura = None

        for r in range(1, self.V + 1):
            for combo in self.gerar_combinacoes(range(self.inicial, self.inicial + self.V), r):
                grafo_temp = self.criar_copia_temporaria()
                cobertura_temp = []

                for vertice in combo:
                    cobertura_temp.append(vertice)
                    grafo_temp.remover_arestas(vertice)

                if self.eh_cobertura(grafo_temp):
                    if menor_cobertura is None or len(cobertura_temp) < len(menor_cobertura):
                        menor_cobertura = cobertura_temp

        return menor_cobertura

    def criar_copia_temporaria(self):
        grafo_temp = Grafo(self.V, self.inicial)
        grafo_temp.adj = {v: list(adj) for v, adj in self.adj.items()}
        grafo_temp.grau = {v: grau for v, grau in self.grau.items()}
        return grafo_temp

    def eh_cobertura(self, grafo):
        return all(not grafo.adj[v] for v in grafo.adj)

    def gerar_combinacoes(self, elementos, r):
        if r == 0:
            yield []
            return

        for i in range(len(elementos)):
            for combo in self.gerar_combinacoes(elementos[i + 1:], r - 1):
                yield [elementos[i]] + combo


if __name__ == "__main__":
    V = int(input("Digite o número de vértices: "))
    E = int(input("Digite o número de arestas: "))
    inicial = int(input("Digite o número do vértice inicial: "))
    
    grafo = Grafo(V, inicial)

    print(f"Digite os pares de arestas (u v) onde {inicial} <= u,v <= {inicial + V - 1}:")
    for _ in range(E):
        u, v = map(int, input().split())
        if inicial <= u <= inicial + V - 1 and inicial <= v <= inicial + V - 1:
            grafo.adicionar_aresta(u, v)
        else:
            print("Entrada inválida. Certifique-se de que está dentro do intervalo especificado.")

    cobertura = grafo.encontrar_cobertura_minima_bruta()
    print("Vertices para cobertura mínima:", cobertura)
