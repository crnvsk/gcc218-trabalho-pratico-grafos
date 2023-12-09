# Programa gerador de entradas para testes.

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