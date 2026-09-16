
from P06_3470_pilha_encadeada import PilhaEncadeada
from P06_3470_fila_encadeada import FilaEncadeada


# TESTE DA PILHA
print('TESTE DA PILHA')
p = PilhaEncadeada()

print("Pilha vazia no início?", p.esta_vazia())
print("Tamanho inicial:", len(p))

p.push("A")
p.push("B")

print("Representação da pilha:", repr(p))
print("Pilha continua vazia?", p.esta_vazia())
print("Tamanho atual:", len(p))
print("Elemento do topo:", p.topo())
print("Elemento removido:", p.pop())
print("Tamanho após o pop:", len(p))

print("\n" + "=" * 30 + "\n")

# TESTE DA FILA
print('TESTE DA FILA')
f = FilaEncadeada()

print("Fila vazia no início?", f.esta_vazia())
print("Tamanho inicial:", len(f))

f.enfileirar(10)
f.enfileirar(20)

print("Representação da fila:", repr(f))
print("Fila continua vazia?", f.esta_vazia())
print("Tamanho atual:", len(f))
print("Elemento da frente:", f.frente())
print("Elemento removido:", f.desenfileirar())
print("Tamanho após desenfileirar:", len(f))