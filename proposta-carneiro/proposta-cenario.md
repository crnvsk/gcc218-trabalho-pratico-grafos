# GCC218 - Algoritmos em Grafos - Trabalho Prático

## Título do Trabalho:
"Monitoramento e Vigilância de trecho na Universidade Federal de Lavras - UFLA"

## Introdução:
O presente trabalho aborda um problema prático de otimização envolvendo grafos, especificamente a necessidade de posicionar câmeras em interseções de ruas para garantir a cobertura máxima de vias adjacentes. O grafo modela, a partir de um recorte de um trecho do campus da UFLA, as interseções como vértices e as ruas como arestas, sendo crucial determinar quais vértices devem ser equipados com câmeras de vigilância para que nenhuma rua do trecho fique sem monitoramento.

## Objetivo:
O objetivo principal é desenvolver uma abordagem eficiente para encontrar a cobertura mínima de vértices que assegure a monitorização de todas as ruas do grafo. Esse problema é formulado como um caso específico do problema de cobertura de vértices em grafos.

## Metodologia:
A metodologia proposta segue uma estratégia baseada em teoria de grafos, utilizando a linguagem de programação Python e programação orientada a objetos. A solução envolve a iteração sobre os vértices em ordem decrescente de grau, excluindo do grafo as arestas cobertas por cada vértice selecionado. O processo continua iterando sobre os vértices restantes até que o grafo esteja vazio.

## Implementação em Python:
O código em Python foi estruturado através da criação de uma classe denominada "Grafo", que representa o grafo de interseções e ruas. Métodos foram desenvolvidos para adicionar arestas, remover arestas incidentes em um vértice e encontrar a cobertura mínima de vértices.

## Entradas do Usuário:
O usuário fornece o número de vértices (interseções) e arestas (ruas) como entrada. Posteriormente, são inseridos os pares de vértices representando a conectividade entre as interseções.

```
G = {V, E}
G = {32, 41}

Número de vértices: 32 
Número de arestas: 41

0 1
0 2
1 3
1 7
2 29
2 28
3 4
3 5
5 6
7 8
8 9
8 10
9 14
10 11
10 12
11 12
12 13
13 14
13 15
14 17
15 16
16 18
17 18
17 31
18 19
19 20
19 30
20 21
20 22
22 23
22 24
23 25
24 25
24 26
26 27
27 28
27 30
28 31
29 26
30 31
31 30
```

## Resultados:
A solução do problema fornece os vértices ideais para posicionar câmeras, maximizando a cobertura de ruas adjacentes e assegurando a vigilância completa do sistema de interseções.

## Conclusão:
O trabalho proposto oferece uma abordagem eficaz e escalável para o problema de cobertura de vértices em grafos, com aplicação prática na otimização da vigilância em interseções e ruas. A implementação em Python e a estrutura orientada a objetos proporcionam uma solução flexível e de fácil compreensão.

