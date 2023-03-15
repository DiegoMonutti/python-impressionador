"""Lista de Exercícios pt2

# Exercícios

## 1. Criando um mini sistema de controle de estoque

- Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
- Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve ser avisado (print) para fazer um novo pedido daquele produto.
- Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:

- alimentos -> Estoque mínimo: 50
- bebidas -> Estoque mínimo: 75
- limpeza -> Estoque mínimo: 30

Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e quantidade atual em estoque.

Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"

Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.
Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.

Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.
Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente.
"""

#seu código aqui

# Dicionário com categorias e seus respectivos estoques mínimos:
categorias = {
    "alimentos": 50,
    "bebidas": 75,
    "limpeza": 30
}

# Pede o nome do produto ao usuário e verifica se o input não está vazio:
produto = None
while not produto:
    produto = input('Insira o nome do produto: ')
    if not produto:
        print('Produto inválido. Por favor, digite novamente.')

# Pede a categoria do produto e verifica se é uma categoria válida:
categoria = None
while categoria not in categorias:
    categoria = input('Insira a categoria do produto (alimentos, bebidas ou limpeza): ').lower()
    if categoria not in categorias:
        print('Categoria inválida. Por favor, digite novamente.')

# Pede a quantidade em estoque do produto e verifica se é um valor inteiro:
quantidade = None
while quantidade is None:
    quantidade_str = input('Digite a quantidade atual em estoque: ')
    if quantidade_str.isdigit():
        quantidade = int(quantidade_str)
    else:
        print('Quantidade inválida. Por favor, digite novamente.')

# Obtém o estoque mínimo da categoria do produto:
estoque_minimo = categorias.get(categoria)

#Se a quantidade em estoque for menor que o estoque mínimo, faz a solicitação de uma nova compra
if quantidade < estoque_minimo:
    print(f'Solicitar {produto} à equipe de compras, temos apenas {quantidade} em estoque.')