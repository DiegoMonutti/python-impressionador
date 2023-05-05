from contas_banco import *

#Criar Conta:
conta_Diego = ContaCorrente('Diego','111.222.333.44', 1234, 56789)

#Criando Cartão de Crédito:
cartao_Diego = CartaoCredito('Diego', conta_Diego)

#Alterando senha
cartao_Diego.senha = '2345'

#Verificando:
print(conta_Diego.__dict__)
print(cartao_Diego.__dict__)