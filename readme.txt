# GCC218 - Algoritmos em Grafos - Trabalho Prático

## Discentes:

- João Pedro Alves Carneiro Valadão
- Augusto Inácio Silva Mariano
- Otávio Rodrigues de Faria
- Lucas Silva Meira

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
O usuário fornece as seguintes informações como entrada no arquivo input.txt:

- O número de vértices (interseções).
- O número de arestas (ruas).
- A numeração do vértice inicial.
- Os pares de vértices representando a conectividade entre as interseções.

Exemplo de arquivo input.txt:

G = {V, E}
G = {4, 4}

```
4 4 1
1 2
2 3
2 4
3 4
```

## Resultados:
A solução do problema fornece os vértices ideais para posicionar câmeras, maximizando a cobertura de ruas adjacentes e assegurando a vigilância completa do sistema de interseções.

## Conclusão:
O trabalho proposto oferece uma abordagem eficaz e escalável para o problema de cobertura de vértices em grafos, com aplicação prática na otimização da vigilância em interseções e ruas. A implementação em Python e a estrutura orientada a objetos proporcionam uma solução flexível e de fácil compreensão.

