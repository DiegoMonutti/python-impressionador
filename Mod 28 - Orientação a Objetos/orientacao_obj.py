from datetime import datetime
import pytz


class ContaCorrente:
    '''
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        nome (str): Nome do cliente
        cpf (str - inserido com pontos e traço): CPF do cliente
        agencia(int): Agência responsável pela conta do cliente
        num_conta(int): Número da Conta Corrente do cliente
        saldo: Saldo disponível na conta do cliente
        limite: Limite do cheque especial do cliente
        transacoes: histórico de transações da conta do cliente
    '''

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime(r'%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = 0
        self.limite = None
        self.transacoes = []

    def consultar_saldo(self):
        '''
        Exibe o saldo atual da conta do cliente. 
        Não há parâmetros necessários.
        '''
        print(f'Seu saldo atual é de R$ {self.saldo:,.2f}')

    def depositar_dinheiro(self, valor):
        '''
        Adiciona o valor ao saldo da conta do cliente e registra a transação na lista de transações.

        Parâmetros: 
            valor(float): Valor depositado em conta.
        '''
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _definir_limite(self):
        '''
        Define o limite da conta do cliente.

        Atributo: 
            limite(float): Limite disponível em conta.
        '''
        self.limite = -1000
        return self.limite
    
    def consultar_limite(self):
        '''
        Exibe o limite da conta do cliente. 
        Não há parâmetros necessários.
        '''
        print(f'Seu limite do Cheque Especial é de R$ {-1*(self._definir_limite()):,.2f}')

    def sacar_dinheiro(self, valor):
        '''
        Subtrai o valor do saldo da conta do cliente caso a diferença entre o valor inserido e o saldo atual seja menor do que o limite em conta do cliente. Após isso, registra a transação na lista de transações.

        Parâmetros: 
            valor(float): Valor depositado em conta.
        '''
        if self.saldo - valor < self._definir_limite():
            print('Você não possui saldo e(ou) limite para sacar esse valor.')
            self.consultar_saldo()
            self.consultar_limite()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
    
    def consultar_transacoes(self):
        '''
        Exibe o histórico de transações da conta do cliente que foi armazenado na lista de transações. 
        Não há parâmetros necessários.
        '''
        print('Histórico de Transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        '''
        Transfere o valor de uma conta, caso a diferença entre o valor inserido e o saldo atual seja menor do que o limite em conta, para uma segunda conta de destino. Após isso, registra a transação na lista de transações para cada conta.

        Parâmetros: 
            valor(float): Valor depositado em conta.
            conta_destino: Objeto conta para o qual será feita a operação.
        '''
        if self.saldo - valor < self._definir_limite():
            print('Você não possui saldo e(ou) limite para realizar essa transferência.')
            self.consultar_saldo()
            self.consultar_limite()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
            conta_destino.saldo += valor
            conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


#Criar Conta:
conta_Diego = ContaCorrente('Diego','111.222.333.44', 1234, 56789)

#Informar o Saldo:
conta_Diego.consultar_saldo()

#Depositar dinheiro:
conta_Diego.depositar_dinheiro(10000)

#Consultar Transações:
conta_Diego.consultar_transacoes()

#Criar Nova Conta:
conta_Fulano = ContaCorrente('Fulano', '222.333.444-55', 5678, 12345)

#Transferir:
conta_Diego.transferir(1000, conta_Fulano)

conta_Diego.consultar_transacoes()
conta_Fulano.consultar_transacoes()