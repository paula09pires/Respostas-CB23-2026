from P06_3470_pilha_encadeada import PilhaEncadeada

class FilaEncadeada:
    """
    Fila implementada por composição de duas instâncias de
    PilhaEncadeada (entrada e saída).
    Interface pública: enfileirar, desenfileirar, frente,
    esta_vazia, __len__ e __repr__.
    """
    def __init__(self):
        self.entrada = PilhaEncadeada()
        self.saida = PilhaEncadeada()
        self._len = 0


    def enfileirar(self,item):
        """
        Insere item no fim da fila (empilha em entrada).
        Complexidade O(1).
        """
        self.entrada.push(item)
        self._len += 1

    def desenfileirar(self):
        """
        Remove e retorna o item da frente da fila.
        Levanta IndexError se a fila estiver vazia.
        Complexidade O(1) amortizada: transfere entrada para saida
        (O(n)) apenas quando a saida está vazia; cada item é
        transferido no máximo uma vez ao longo de sua vida na
        estrutura, então o custo se dilui entre as chamadas.
        """
        if self._len == 0:
            raise IndexError("desenfileirar com Lista Vazia")

        else:
            if self.saida.esta_vazia():
                while not self.entrada.esta_vazia():
                    valor = self.entrada.pop()
                    self.saida.push(valor)

            valor = self.saida.pop()
            self._len -= 1
            return valor

        
    def frente(self):
        """
        Retorna o item da frente da fila, sem removê-lo.
        Levanta IndexError se a fila estiver vazia.
        Complexidade O(1) amortizada, pelo mesmo motivo de
        desenfileirar().
        """
        if self._len == 0:
            raise IndexError("frente com Lista Vazia")

        else:
            if self.saida.esta_vazia():
                while not self.entrada.esta_vazia():
                    valor = self.entrada.pop()
                    self.saida.push(valor)

            return self.saida.topo()

    def esta_vazia(self):
        """
        Retorna True se a fila não tem elementos, False se tiver.
        Complexidade O(1).
        """
        return self._len == 0

    def __len__(self):
        """
        Retorna a quantidade de elementos na fila.
        Complexidade O(1)
        """
        return self._len 


    def __repr__(self):
        """
        Retorna uma representação textual da fila, do item da frente
        até o item do fim.
        Complexidade O(n): percorre saida uma vez e entrada duas vezes
        (uma para inverter em aux, outra para restaurar entrada).
        """
        parte_saida = str(self.saida)
        aux = PilhaEncadeada()
        
        while not self.entrada.esta_vazia():
            aux.push(self.entrada.pop())

        parte_entrada = str(aux)

        while not aux.esta_vazia():
            self.entrada.push(aux.pop())

        partes = [p for p in (parte_saida, parte_entrada) if p != ""]
        return " -> ".join(partes)


        
        