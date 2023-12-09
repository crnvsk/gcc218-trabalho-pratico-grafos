Possuo um grafo que representa interseções(vértices) e ruas(arestas), nesse grafo preciso saber em quais vértices devo posicionar câmeras **para que elas cubram a maior quantidade possível de ruas por câmera**(ruas adjacentes à esse vértice), **de forma que cubra todas as ruas do grafo**.
Como voce resolveria esse problema usando **Python** e **orientação a objetos**?
As entradas devem ser **fornecidas pelo usuario** da seguinte forma:

```
4 4
1 2
2 3
2 4
3 4
```

Na primeira linha recebemos V=4 e E=4, onde V é o número de vértices e E o número de arestas, e nas N subsequentes linhas recebemos as arestas(par de vértices).
Este é um problema de cobertura de vértices.

A solução do problema de cobertura deve ser resolvido da seguinte forma: Iteramos por todos os vértices seguindo a ordem decrescente de graus, com o fim de "excluir do grafo" todas as arestas que esse vértice cobre. Dessa forma, iteramos sobre todos os vértices, mas só os restantes (de acordo com os vértices eliminadas) e iteramos as arestas que ainda não foram elminadas, até o grafo estar vazio.