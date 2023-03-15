# -*- coding: utf-8 -*-
"""Exercícios Listas pt1.ipynb

Exercícios

1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
"""
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_ano = vendas_1sem + vendas_2sem

melhor = max(vendas_ano)
indice_melhor = vendas_ano.index(melhor)

print(f'O mês de "{meses[indice_melhor]}" foi o melhor em vendas com o total de R${melhor:,.2f}.')

pior = min(vendas_ano)
indice_pior = vendas_ano.index(pior)

print(f'O mês de "{meses[indice_pior]}" foi o pior em vendas com o total de R${pior:,.2f}.')

#Outra solução:
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_ano = vendas_1sem + vendas_2sem

# encontra o melhor mês e as vendas utilizando a função max com lambda
melhor_mes, melhor_vendas = max(enumerate(vendas_ano), key=lambda x: x[1])
print(f'O mês de "{meses[melhor_mes]}" foi o melhor em vendas com o total de R${melhor_vendas:,.2f}.')

# encontra o pior mês e as vendas utilizando a função min com lambda
pior_mes, pior_vendas = min(enumerate(vendas_ano), key=lambda x: x[1])
print(f'O mês de "{meses[pior_mes]}" foi o pior em vendas com o total de R${pior_vendas:,.2f}.')

"""2. Continuação
Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
"""
faturamento_total = sum(vendas_ano)
print(f'O faturamento total do ano foi de R${faturamento_total:,.2f}.')

"""3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista.
"""
top3_vendas = []
top_3meses = []

for venda in range(3):
    max_venda = max(vendas_ano)
    top3_vendas.append(max_venda)
    max_index = vendas_ano.index(max_venda)
    top_3meses.append(meses[max_index])
    vendas_ano.pop(max_index)
    meses.pop(max_index)

print(f'Os 3 melhores meses de vendas e seus respectivos valores foram: ')
for i in range (3):
    print(f'{top_3meses[i]}: R${(top3_vendas[i]):,.2f}')