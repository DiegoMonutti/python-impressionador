"""Exercícios do Módulo 1 - Operações, Variáveis e Input

Parte 1 - Operações e Variáveis

Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano.
Obs: faça tudo usando variáveis.

Valores do último ano:

    #Quantidade de Vendas de Coca = 150
    #Quantidade de Vendas de Pepsi = 130
    #Preço Unitário da Coca = 1,50
    #Preço Unitário da Pepsi = 1,50
    #Custo da Loja: 2.500,00"""

#Variáveis:

qtd_coca = 150
qtd_pepsi = 130
preco_coca = 1.50
preco_pepsi = 1.50
custo = 2500

#1. Qual foi o faturamento de Pepsi da Loja?

fat_pepsi = qtd_pepsi * preco_pepsi
print (f'O faturamento de pepsi da loja foi de: R${fat_pepsi:.2f}')

#2. Qual foi o faturamento de Coca da Loja?

fat_coca = qtd_coca * preco_coca
print (f'O faturamento de Coca-Cola da loja foi de: R${fat_coca:.2f}')

#3. Qual foi o Lucro da loja?

lucro = fat_pepsi + fat_coca - custo

if lucro == 0:
    print ('A loja não teve lucro nesse mês.')
elif lucro > 0:
    print (f'O lucro da loja nesse período foi de: R${lucro:.2f}')
else:
    print (f'Nesse período a loja teve um prejuízo de: R${(lucro * -1):.2f}')

#4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual

margem = lucro / (fat_coca + fat_pepsi)
print (f'A margem da loja nesse período foi de {margem:.2%}')


"""Parte 2 - Inputs e Strings:

A maioria das empresas trabalham com um Código para cada produto que possuem. 
A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.

Ex: 
    Coca -> Código: BEB1300543
    Pepsi -> Código: BEB1300545
    Vinho Primitivo Lucarelli -> Código: BAC1546001
    Vodka Smirnoff -> Código: BAC17675002

Repare que todas as bebidas não alcoólicas tem o início do Código "BEB" e todas as bebidas alcoólicas tem o início do código "BAC".

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcoólica. 
     O programa deve responder True para bebidas alcoólicas e False para bebidas não alcoólicas. 
     Para inserir um código, use um input."""


bebida = input('Insira o código da bebida que será consultada: ').upper()

print ('BAC' in bebida)