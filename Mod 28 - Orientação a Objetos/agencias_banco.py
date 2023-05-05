from random import randint

class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
    
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa atual R${self.caixa:,.2f}')
        else:
            print(f'O valor do caixa está ok. Caixa atual R${self.caixa:,.2f}')
    
    def emprestar_dinheiro(self, valor, cpf, juros):
        if caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo impossível de ser realizado. Valor não disponível em caixa.')
    
    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

#Agência Virtual:
class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        super().__init__(telefone, cnpj, 1000)
        self.site = site
        self.caixa = 1000000

#Agência Comum:
class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 1000000

#Agência Premium:
class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj, numero):
        super().__init__(telefone, cnpj, numero=randint(1001,9999))
        self.caixa = 10000000