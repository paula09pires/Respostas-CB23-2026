import AP_03_ordenacao as ap3
import random
import time
import sys

sys.setrecursionlimit(10**6)

def quick_pior(n):
    return [x for x in range(n)[::-1]]

def medio(n):
    sem_repeticao = {}
    lista = []

    elem = random.randint(1,n)
    if elem not in sem_repeticao:
        lista.append(elem)
        sem_repeticao[elem] = True

    return lista 

def tempo_merge(n,k):
    tempos = []
    for _ in range(k):
        lista = medio(n)
        t0 = time.perf_counter()
        ap3.divide_and_conquer_sort(lista)
        tf = time.perf_counter()
        tempos.append(tf-t0)

    return sum(tempos)/k

def tempo_quick(n,k, pior=None):
    tempos = []
    for _ in range(k):
        lista = quick_pior(n) if pior else medio(n)
        t0 = time.perf_counter()
        ap3.quick_sort(lista)
        tf = time.perf_counter()
        tempos.append(tf-t0)

    return sum(tempos)/k

def tempo_select(n,k):
    tempos = []
    for _ in range(k):
        lista = medio(n)
        t0 = time.perf_counter()
        ap3.selection_sort(lista)
        tf = time.perf_counter()
        tempos.append(tf-t0)

    return sum(tempos)/k


print('-' * 50)
print(f'{'Select Sort':^50}')
print('-' * 50)
print(f'N(200): {tempo_select(200,50)} ms')
print(f'N(600): {tempo_select(600,50)} ms')
print(f'N(2000): {tempo_select(2000,50)} ms')
print(f'N(6000): {tempo_select(6000,50)} ms')
print('-' * 50)
print(f'{'Merge Sort':^50}')
print('-' * 50)
print(f'N(200): {tempo_merge(200,50)} ms')
print(f'N(600): {tempo_merge(600,50)} ms')
print(f'N(2000): {tempo_merge(2000,50)} ms')
print(f'N(6000): {tempo_merge(6000,50)} ms')
print('-' * 50)
print(f'{'Quick Sort Caso Médio':^50}')
print('-' * 50)
print(f'N(200): {tempo_quick(200,50)} ms')
print(f'N(600): {tempo_quick(600,50)} ms')
print(f'N(2000): {tempo_quick(2000,50)} ms')
print(f'N(6000): {tempo_quick(6000,50)} ms')
print('-' * 50)
print(f'{'Quick Sort Pior Caso':^50}')
print('-' * 50)
print(f'N(200): {tempo_quick(200,50,quick_pior)} ms')
print(f'N(600): {tempo_quick(600,50,quick_pior)} ms')
print(f'N(2000): {tempo_quick(2000,50,quick_pior)} ms')
print(f'N(6000): {tempo_quick(6000,50,quick_pior)} ms')
print('-' * 50)