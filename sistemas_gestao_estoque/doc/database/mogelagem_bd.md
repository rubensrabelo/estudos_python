## Descrição do projeto

Este projeto é um sistema de gerenciamento de estoque que permite o rastreamento de produtos, fornecedores, clientes, categorias, entradas, saídas e o histórico de movimentação. Ele foi projetado para ajudar a manter um controle eficiente do estoque, garantindo que os produtos estejam sempre disponíveis quando necessário.

## Entidades, Atributos e Relacionamentos

### Entidades

1. **Produtos**
2. **Fornecedores**
3. **Clientes**
4. **Categorias**
5. **Entradas**
6. **Saídas**
7. **Histórico de Movimentação**

### Atributos

#### Produto

- ID do Produto
- Nome do Produto
- Marca
- ID Categoria
- Preço Unitário
- Quantidade em estoque

#### Fornecedores

- ID do Fornecedor
- Nome
- Telefone
- Endereço
- Produto Fornecido

#### Cliente

- ID do Cliente
- Nome
- Data de Nascimento
- Sexo

#### Categorias

- ID da Categoria
- Nome
- Descrição

#### Entradas

- ID Entrada
- ID do Produto
- Quantidade de Entrada
- Data e Hora
- ID Fornecedor
- Preço da Compra
- Descrição

#### Saídas

- ID da Saída
- ID do Produto
- Quantidade de Saída
- Data e Hora
- ID do Cliente
- Preço da Venda
- Motivo da Saída
- Descrição

#### Histórico de Movimentação

- Data e hora da movimentação
- Tipo (Entrada ou Saída)
- ID do Tipo (Informação contida no ID da tabela de Entrada ou Saída)

## Relacionamentos das Entidades

1. **Produto**
   - Cada produto pertence a uma categoria (relacionamento muitos para um com Categorias).
   - Cada produto pode ter várias entradas e saídas (relacionamento um para muitos com Entradas e Saídas).

2. **Fornecedor**
   - Cada fornecedor pode fornecer vários produtos (relacionamento um para muitos com Produtos).
   - Cada fornecedor pode estar associado a várias entradas (relacionamento um para muitos com Entradas).

3. **Cliente**
   - Cada cliente pode estar associado a várias saídas (relacionamento um para muitos com Saídas).

4. **Categoria**
   - Cada categoria pode ter vários produtos (relacionamento um para muitos com Produtos).

5. **Entradas**
   - Cada entrada está associada a um produto (relacionamento muitos para um com Produtos).
   - Cada entrada está associada a um fornecedor (relacionamento muitos para um com Fornecedores).

6. **Saídas**
   - Cada saída está associada a um produto (relacionamento muitos para um com Produtos).
   - Cada saída está associada a um cliente (relacionamento muitos para um com Clientes).

7. **Histórico de Movimentação**
   - Cada registro de movimentação está associado a uma entrada ou saída (relacionamento muitos para um com Entradas e Saídas).

## Diagrama ER (Entidade-Relacionamento)
