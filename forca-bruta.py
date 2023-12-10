# Implementação feita por: Augusto Mariano, João Pedro Alves Carneiro, Lucas Silva Meira, Otavio Rodrigues De Faria
# Implementação por força bruta, testando todas as possibilidades, sem a utilização da heurística gulosa para encontrar a cobertura mínima de vértices.
# Problema NP-Completo.
# A solução tem complexidade de O(V!).

class Grafo:
    def __init__(self, V, inicial=0):
        # Inicializa o grafo com um número de vértices (V) e um vértice inicial opcional.
        self.V = V
        self.inicial = inicial
        # Dicionário para armazenar listas de adjacência para cada vértice.
        self.adj = {v: [] for v in range(inicial, inicial + V)}
        # Dicionário para armazenar os graus de cada vértice.
        self.grau = {v: 0 for v in range(inicial, inicial + V)}

    def adicionar_aresta(self, u, v):
        # Adiciona uma aresta entre os vértices u e v, atualizando as listas de adjacência e os graus.
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.grau[u] += 1
        self.grau[v] += 1

    def remover_arestas(self, vertice):
        # Remove todas as arestas conectadas a um vértice, atualizando as listas de adjacência e os graus.
        for adjacente in self.adj[vertice]:
            self.grau[adjacente] -= 1
            self.adj[adjacente].remove(vertice)
        self.grau[vertice] = 0
        self.adj[vertice] = []

    def encontrar_cobertura_minima_bruta(self):
        # Encontra a cobertura mínima por força bruta, testando todas as combinações possíveis.
        menor_cobertura = None

        # Itera sobre todos os possíveis tamanhos de cobertura.
        for r in range(1, self.V + 1):
            # Gera todas as combinações de vértices possíveis para a cobertura de tamanho r.
            for combo in self.gerar_combinacoes(range(self.inicial, self.inicial + self.V), r):
                # Cria uma cópia temporária do grafo e uma lista temporária para a cobertura.
                grafo_temp = self.criar_copia_temporaria()
                cobertura_temp = []

                # Remove as arestas dos vértices na cobertura temporária.
                for vertice in combo:
                    cobertura_temp.append(vertice)
                    grafo_temp.remover_arestas(vertice)

                # Verifica se a cobertura temporária é válida.
                if self.eh_cobertura(grafo_temp):
                    # Atualiza a menor cobertura se a atual for menor.
                    if menor_cobertura is None or len(cobertura_temp) < len(menor_cobertura):
                        menor_cobertura = cobertura_temp

        return menor_cobertura

    def criar_copia_temporaria(self):
        # Cria uma cópia temporária do grafo para realizar experimentos sem modificar o grafo original.
        grafo_temp = Grafo(self.V, self.inicial)
        grafo_temp.adj = {v: list(adj) for v, adj in self.adj.items()}
        grafo_temp.grau = {v: grau for v, grau in self.grau.items()}
        return grafo_temp

    def eh_cobertura(self, grafo):
        # Verifica se a cobertura é válida, ou seja, se todos os vértices estão cobertos.
        return all(not grafo.adj[v] for v in grafo.adj)

    def gerar_combinacoes(self, elementos, r):
        # Gera todas as combinações possíveis de tamanho r a partir de uma lista de elementos.
        if r == 0:
            yield []
            return

        for i in range(len(elementos)):
            for combo in self.gerar_combinacoes(elementos[i + 1:], r - 1):
                yield [elementos[i]] + combo


if __name__ == "__main__":
    # Solicita entrada do usuário para o número de vértices, arestas e vértice inicial.
    V = int(input("Digite o número de vértices: "))
    E = int(input("Digite o número de arestas: "))
    inicial = int(input("Digite o número do vértice inicial: "))
    
    # Cria um objeto Grafo e solicita ao usuário que insira os pares de arestas.
    grafo = Grafo(V, inicial)
    print(f"Digite os pares de arestas (u v) onde {inicial} <= u,v <= {inicial + V - 1}:")
    for _ in range(E):
        u, v = map(int, input().split())
        if inicial <= u <= inicial + V - 1 and inicial <= v <= inicial + V - 1:
            grafo.adicionar_aresta(u, v)
        else:
            print("Entrada inválida. Certifique-se de que está dentro do intervalo especificado.")

    # Encontra e exibe a cobertura mínima de vértices.
    cobertura = grafo.encontrar_cobertura_minima_bruta()
    print("Vertices para cobertura mínima:", cobertura)

