## Questão 2
Escolhi utilizar a **Busca em Largura (BFS)**.

Ela garante que a primeira vez que o rato chegar no queijo o caminho percorrido será o menor possível. 
(Ao contrário da busca em profundidade, que poderia seguir por um caminho longo e menos eficiente antes de encontrar o objetivo.)


O algoritmo visita todas as células a 1 passo da origem, depois a 2 passos e em diante.

O algoritmo é eficiente ao utilizar o 'collections.deque' e 'popleft()', que possui O(1).



