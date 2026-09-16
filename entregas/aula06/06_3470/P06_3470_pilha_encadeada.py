class _No:
    """
    Nó auxiliar da lista encadeada: guarda um valor (`valor`) e a
    referência para o próximo nó (`next`).
    """

    def __init__(self,valor):
        self.valor = valor
        self.next = None



class PilhaEncadeada:
    """
    Pilha implementada com armazenamento interno em lista
    simplesmente encadeada
    
    Mantém apenas uma referência ao nó do topo (`head`) e um
    contador de elementos (`_len`). Interface pública: push, pop,
    topo, esta_vazia, __len__ e __repr__.
    """
    def __init__(self):
        self.head = None
        self._len = 0 


    def push(self,item):
        """
        Define o push(item) colocando o item como novo topo da pilha e virando uma head que aponta para a head anterior, 
        complexidade O(1)
        """

        novo = _No(item)

        novo.next = self.head
        self.head = novo

        self._len += 1



    def pop(self):
        """
        Define o pop() que retira o último item da pilha e coloca a nova cabeça como a próxima, 
        complexidade O(1)
        """

        if self.head is None:
            raise IndexError("Pop em Lista vazia")

        else:
            retirado = self.head
            self.head = self.head.next
            self._len -= 1
            return retirado.valor
  
    def topo(self):
        """
        Define o topo() que retorna o valor da head, 
        complexidade O(1)
        """ 

        if self.head is None:
            raise IndexError("Topo em Lista vazia")
        else:
            return self.head.valor     

    
    def esta_vazia(self):
        """
        Retorna se a lista está vazia, 
        complexidade O(1)
        """

        return self.head is None

    def __len__(self):
        """
        Retorna o tamanho da pilha, 
        complexidade O(1)
        """

        return self._len


    def __repr__(self):
        """
        Retorna todos os valores da pilha em ordem, 
        complexidade O(n)
        """

        i = 0
        string = ""
        atual = self.head
        while i != self._len:
            atual_string = str(atual.valor)
            string += atual_string + " -> "
            atual = atual.next
            i += 1
        return string[:-4]

