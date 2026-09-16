Quando a pilha de saída está vazia, desenfileirar transfere todos os k elementos da pilha de entrada para a pilha de saída, 
o que custa O(k) — no pior caso, O(n)

Cada elemento passa pela estrutura no máximo três vezes: entrada, um push, é transferido uma única vez (um pop, um push) e sai com um pop final. Depois de transferido, ele fica na pilha de saída até ser removido.

O total de operações é no máximo 3n, que dividido por n fica com O(1), na média, por operação.