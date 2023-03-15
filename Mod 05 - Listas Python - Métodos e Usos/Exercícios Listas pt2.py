"""Exercícios Listas pt2.ipynb

1. Mudança de Carga Tributária

- Reformas e mudanças de cargas tributárias são bem comuns no Brasil.

Digamos que você trabalhe em uma empresa de ecommerce

No Brasil, o imposto sobre livros é zerado. De um ano para o outro, o governo criou um novo imposto que incide em 10% sobre o valor dos livros e agora você precisa alterar o registro dos preços dos livros da empresa para garantir que esse imposto vai ser repassado para o preço final do produto.

Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela.

Além disso, calcule qual vai ser o impacto financeiro da criação desse imposto para a empresa (ou seja, quanto que o imposto vai aumentar de custo para a empresa)

Obs: para facilitar, colocamos apenas 1 livro na lista, mas em breve vamos aprender um for que vai adaptar esse cenário para qualquer quantidade de livros na sua lista.

Obs2: Seu código deve funcionar mesmo que não haja livros na lista de produtos da empresa
"""

produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if 'livro' in produtos:
    index_livro = produtos.index('livro')
    custo_livros_antigo = produtos_ecommerce[index_livro][0] * produtos_ecommerce[index_livro][1]
    produtos_ecommerce[index_livro][1] *= 1.1
    custo_livros_novo = custo_livros_antigo * 1.1
    aumento_custo = custo_livros_novo - custo_livros_antigo
    print(f'Pagaremos R${aumento_custo:,.2f} a mais de impostos após o reajuste.')
else:
    print('Não há livros em nosso e-commerce.')

print(produtos)
print(produtos_ecommerce)

#Considerando que poderia ter mais de um livro na lista:
produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'livro', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [10000, 10],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

imposto_livros = 0.1
aumento_custo = []

for i, produto in enumerate(produtos):
    if produto == 'livro':
        custo_antigo = produtos_ecommerce[i][0] * produtos_ecommerce[i][1]
        produtos_ecommerce[i][1] *= (1 + imposto_livros)
        custo_novo = produtos_ecommerce[i][0] * produtos_ecommerce[i][1]
        aumento_custo.append(custo_novo - custo_antigo)

print(f'O imposto sobre livros aumentou em R${sum(aumento_custo):,.2f}.')
        
print(produtos)
print(produtos_ecommerce)