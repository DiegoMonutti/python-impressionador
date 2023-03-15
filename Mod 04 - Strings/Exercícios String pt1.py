
"""Exercícios String pt1.ipynb"""


"""1. Cadastro de CPF

Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input box apenas com números.

Ex: 'Insira seu CPF (digite apenas números)'

Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"
"""

while True:
    cpf = input('Insira seu CPF (Digite apenas números): ')
    if cpf.isnumeric() and len(cpf) == 11:
        print(f'CPF validado com sucesso: {cpf}.')
        break
    else:
        print('Por favor digite seu CPF novamente. Digite apenas números.')

"""## 2. Melhorando nosso Cadastro de CPF

Agora, além das validações anteriores, vamos criar um input que permita que o usuário insira pontos, traços e inclusive espaços vazios.

Nosso programa deve "tratar" o que o usuário inserir para padronizar o CPF dele em apenas números.

A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços do CPF que o cliente inserir e, uma vez retirados pontos, traços e espaços, devem sobrar apenas números no CPF. Qualquer outro caractere deve ser considerado inválido.

No final, nosso programa deve exibir uma mensagem para o usuário, caso ele tenha inserido o CPF inválido ou então apenas deve printar o CPF correto já só com número.
"""

def formatar_cpf(cpf):
    cpf_sem_separadores = cpf.replace(".", "").replace("-", "").replace(" ", "")
    return cpf_sem_separadores

while True:
    cpf = input('Insira seu CPF (Digite apenas números): ')
    cpf = formatar_cpf(cpf)
    if cpf.isnumeric() and len(cpf) == 11:
        print(f'CPF validado com sucesso: {cpf}.')
        break
    else:
        print('CPF inválido. Por favor digite seu CPF novamente.')

#Outra solução:
import re

def formatar_cpf(cpf):
    cpf = re.sub(r"\D", "", cpf) # Remove caracteres que não são dígitos
    return cpf

while True:
    cpf = input('Insira seu CPF (Digite apenas números): ')
    cpf = formatar_cpf(cpf)
    if cpf.isdigit() and len(cpf) == 11:
        print(f'CPF validado com sucesso: {cpf}.')
        break
    else:
        print('CPF inválido. Por favor digite seu CPF novamente.')

"""## 3. Cadastro de e-mails

- A Hashtag sempre se comunica com seus clientes por e-mail. Para isso, a gente tem em cada página um cadastro de nome e e-mail. Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu é um e-mail válido, verificando se ele tem '@' e se depois do '@' tem algum ponto, afinal:

- liragmail.com NÃO é um e-mail válido
- lira@gmail NÃO é um e-mail válido
- lira@gmail.com é um e-mail válido

Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique:
1. Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente
2. Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido

Obs: Pode te ajudar lembrar do método .find da aula de Métodos de String. Você pode testar o que ele dá como resposta caso ele não encontre um item dentro da string
"""

def verificar_email(email):
    if '@' in email:
        posicao = email.find('@')
        if '.com' in email[posicao:]:
            return True
    else:
        return False
    
def formatar_email(email):
    email_formatado = email.replace(" ", "")
    return email_formatado

def formatar_nome(nome):
    nome_formatado = nome.replace("  ", " ").title()
    return nome_formatado

def verificar_nome(nome):
    nome_verificado = nome.replace(" ", "")
    if nome_verificado.isalpha():
        return True
    else:
        return False

while True:
    nome = input('Insira o seu nome: ')
    nome = formatar_nome(nome)
    validar_nome = verificar_nome(nome)
    if validar_nome:
        print(f'Nome cadastrados com sucesso: {nome}.')
        break
    else:
        print('Nome inválido. Por favor digite seu nome novamente.')
        continue

while True:
    email = input('Insira o seu e-mail: ')
    email = formatar_email(email)
    validar_email = verificar_email(email)
    if validar_email:
        print(f'E-mail cadastrado com sucesso: {email}')
        break
    else:
        print('E-mail inválido. Por favor digite seu e-mail novamente.')
        continue

#Fazendo a validação do email com expressões regulares:
import re

def verificar_email(email):
    padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]{2,}\.[A-Za-z]{2,}\b'
    return re.match(padrao, email)

def formatar_email(email):
    email_formatado = email.replace(" ", "")
    return email_formatado

def formatar_nome(nome):
    nome_formatado = nome.replace("  ", " ").title()
    return nome_formatado

def verificar_nome(nome):
    nome_verificado = nome.replace(" ", "")
    if nome_verificado.isalpha():
        return True
    else:
        return False

while True:
    nome = input('Insira o seu nome: ')
    nome = formatar_nome(nome)
    validar_nome = verificar_nome(nome)
    if validar_nome:
        print(f'Nome cadastrados com sucesso: {nome}.')
        break
    else:
        print('Nome inválido. Por favor digite seu nome novamente.')
        continue

while True:
    email = input('Insira o seu e-mail: ')
    email = formatar_email(email)
    validar_email = verificar_email(email)
    if validar_email:
        print(f'E-mail cadastrado com sucesso: {email}')
        break
    else:
        print('E-mail inválido. Por favor digite seu e-mail novamente.')
        continue
