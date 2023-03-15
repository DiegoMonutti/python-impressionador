"""Lista de Exercícios if"""

"""1. Cálculo de Bônus

- Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:

A meta é 1000 vendas.
Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.
Caso contrário o valor de bônus do funcionário é 0.
Print o bônus dos 3 funcionários
"""

meta = 1000

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

#Crie seu código aqui:

vendas = [vendas_funcionario1, vendas_funcionario2, vendas_funcionario3]

bonus = [venda * 0.1 if venda >= meta else 0 for venda in vendas]

for i in range(len(bonus)):
    print(f"O funcionário {i+1} ganhou R${bonus[i]:.2f} de bônus.")

"""Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 270 de bônus"""


"""2. Cálculo de bônus com uma nova regra

- Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:

A meta é 1000 vendas
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:

- Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
- Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
- Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.

Use as mesmas variáveis de vendas_funcionários
"""

meta = 1000

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

#Crie seu código aqui:

vendas = [vendas_funcionario1, vendas_funcionario2, vendas_funcionario3]

bonus = [venda * 0.15 if venda >= 2*meta else (venda * 0.10 if venda >= meta else 0) for venda in vendas]

for i in range(len(bonus)):
    print(f"O funcionário {i+1} ganhou R${bonus[i]:.2f} de bônus.")


#Outra opção:

meta = 1000

vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

vendas = [vendas_funcionario1, vendas_funcionario2, vendas_funcionario3]

bonus = []

for venda in vendas:
    if venda >= 2 * meta:
        bonus.append(venda * 0.15)
    elif venda >= meta:
        bonus.append(venda * 0.10)
    else:
        bonus.append(0)

for i, b in enumerate(bonus):
    print(f"O funcionário {i+1} ganhou R${b:.2f} de bônus.")

    
"""Resposta:
O funcionário 1 ganhou 100 de bônus
O funcionário 2 ganhou 0 de bônus
O funcionário 3 ganhou 405 de bônus
"""