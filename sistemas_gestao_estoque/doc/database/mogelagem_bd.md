## Descrição do projeto

Este projeto é um sistema de gerenciamento de estoque que permite o rastreamento de produtos, fornecedores, clientes, categorias, entradas, saídas e o histórico de movimentação. Ele foi projetado para ajudar a manter um controle eficiente do estoque, garantindo que os produtos estejam sempre disponíveis quando necessário.

# Entidades, Atributos e Relacionamentos

## Entidades

1. **Produtos**
2. **Fornecedores**
3. **Clientes**
4. **Categorias**
5. **Entradas**
6. **Saídas**
7. **Histórico de Movimentação**

## Atributos

### Produto

- ID do Produto
- Nome do Produto
- Marca
- ID Categoria
- Preço Unitário
- Quantidade em estoque

### Fornecedores

- ID do Fornecedor
- Nome
- Telefone
- Endereço
- Produto Fornecido

### Cliente

- ID do Cliente
- Nome
- Data de Nascimento
- Sexo

### Categorias

- ID da Categoria
- Nome
- Descrição

### Entradas

- ID Entrada
- ID do Produto
- Quatidade de Entrada
- Data e Hora
- ID Fornecedor
- Preço da Compra
- Descrição

### Saídas

- ID da Saída
- ID do Produto
- Quatidade de Saída
- Data e Hora
- ID do Cliente
- Preço da Venda
- Motívo da Saída
- Descrição

### Histórico de Movimentação

- Data e hora da movimentação
- Tipo (Entrada ou Saída)
- ID do Tipo (Informação contida no ID da tabela de Entrada ou Saída)

## Relacionamentos

1. 