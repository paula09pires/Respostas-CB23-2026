# Questão 1
Classes base:

pessoa

restaurante

iguaria

Subclasse de pessoa:

funcionário

 **Herda 'nome' e 'idade' de pessoa**

Subclasse de funcionário:

garçom

gerente

chefe de cozinha

**Herdam 'salário' e 'carga_horária' de funcionário, além de 'nome' e 'idade' indiretamente**

Subclasse de restaurante:

pizzaria

**Herda 'nome', 'endereço' e 'telefone' de restaurante**

Subclasse de iguaria:

pizza

bolo

**Herdam 'nome' e 'preço' de iguaria**


# Questão 2

Adicionaria um atributo a restaurante que seria o cardápio, que contém os itens do cardápio.
Esses itens do cardápio conteriam a iguaria e o seu preço. 
A iguaria conteria apenas seu nome.

A ordem ficaria:

Restaurante: {nome: str, endereco: str, telefone: str, cardapio: List[ItemCardapio]}

ItemCardapio: {iguaria: Iguaria, preco: float}

Iguaria: {nome: str}

# Questão 3

argumento1: List[ItemCardapio]

**Pois o garçom coleta as comidas, não apenas uma necessariamente**

argumento2: List[Iguaria]

**O chef poderia fazer apenas uma comida por vez, mas, creio que se adeque mais à realidade ele fazer vários pratos.**

argumento3: funcionário 

**não faz sentido ele demitir mais de uma pessoa por vez (então não é lista) e ele não precisa saber das especificidades (garçom, etc), logo, precisa apenas saber da classe funcionário.**

