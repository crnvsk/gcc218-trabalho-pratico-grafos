# O problema não tem solução polinomial, por que?

O problema conhecido como o Problema da Cobertura de Vértices, é classificado como NP-completo. A classificação NP-completo implica que, embora seja possível verificar em tempo polinomial se uma solução proposta é correta, não se conhece um algoritmo eficiente (polinomial) para encontrar uma solução ótima para o problema em todos os casos.

A razão pela qual o problema não possui uma solução polinomial reside na natureza combinatória e na complexidade dos casos que precisam ser considerados.

Completude do Grafo: O problema da cobertura de vértices lida com a necessidade de selecionar um subconjunto mínimo de vértices de modo que cada aresta do grafo seja coberta por pelo menos um vértice. A quantidade de subconjuntos de vértices a serem avaliados cresce exponencialmente com o número de vértices, tornando impraticável a busca exaustiva em muitos casos.

NP-Completo: A redução de outros problemas NP-completos ao problema da cobertura de vértices demonstra sua complexidade. Isso significa que, se houvesse um algoritmo polinomial para o problema da cobertura de vértices, seria possível encontrar algoritmos polinomiais para todos os problemas NP-completos, o que é uma conjectura ainda não resolvida na teoria da computação (a questão P vs NP).

Em resumo, a complexidade do problema da cobertura de vértices reside na necessidade de considerar todas as combinações possíveis de vértices para encontrar a solução ótima, levando a uma explosão combinatória que dificulta a obtenção de uma solução eficiente em termos de tempo de execução.

# Tamanho do Grafo e Algoritmo Exponencial de Força Bruta

```
import random

def generate_random_graph(num_vertices, num_edges):
    # Cria um grafo representado por um dicionário
    graph = {vertex: [] for vertex in range(num_vertices)}

    # Adiciona arestas aleatórias
    for _ in range(num_edges):
        source = random.randint(0, num_vertices - 1)
        target = random.randint(0, num_vertices - 1)

        # Evita adicionar arestas para o mesmo vértice
        while source == target or target in graph[source]:
            target = random.randint(0, num_vertices - 1)

        graph[source].append(target)

    return graph

def main():
    # Solicita a entrada do usuário para o número de vértices e arestas
    num_vertices = int(input("Digite o número de vértices: "))
    num_edges = int(input("Digite o número de arestas: "))

    random_graph = generate_random_graph(num_vertices, num_edges)

    # Exibe informações sobre o grafo gerado
    print("Arestas:")

    for vertex, edges in random_graph.items():
        for target in edges:
            print(f"{vertex} {target}")

if __name__ == "__main__":
    main()

```

```
# Implementação por força bruta, testando todas as possibilidades, sem a utilização da heurística gulosa para encontrar a cobertura mínima de vértices.
# Complexidade de 

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

```

# Explicação da Heurística

A heurística gulosa é um método de resolução de problemas que segue uma abordagem gananciosa, ou seja, faz escolhas locais que parecem ser as melhores em cada etapa, na esperança de alcançar uma solução global otimizada. No problema de cobertura de vértices, o objetivo é encontrar o menor conjunto de vértices em um grafo que cubra todas as arestas.

A abordagem gulosa para o problema de cobertura de vértices funciona da seguinte maneira:

Seleção Gananciosa: Em cada etapa, escolhe-se um vértice que cobre o maior número possível de arestas não cobertas. Isso significa escolher o vértice de maior grau, ou seja, o vértice que está conectado ao maior número de outros vértices.

Remoção de Arestas Cobertas: Após a seleção do vértice, todas as arestas cobertas por ele são removidas. Isso reduz o problema original para um subproblema mais simples.

Repetição: Repete-se o processo nas arestas restantes até que todas sejam cobertas.

Critério de Parada: O algoritmo continua até que todas as arestas sejam cobertas ou até que não seja possível selecionar mais vértices.

A heurística gulosa para o problema de cobertura de vértices não garante uma solução ótima, mas muitas vezes produz soluções razoáveis com um esforço computacional relativamente baixo. No entanto, vale ressaltar que, em alguns casos, a solução obtida pode estar longe da solução ótima global.