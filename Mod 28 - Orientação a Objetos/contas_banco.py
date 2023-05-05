from datetime import datetime
import pytz
from random import randint


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
        cartoes: cartões de créditos associados a conta do cliente
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
        self._saldo = 0
        self._limite = None
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        '''
        Exibe o saldo atual da conta do cliente. 
        Não há parâmetros necessários.
        '''
        print(f'Seu saldo atual é de R$ {self._saldo:,.2f}')

    def depositar_dinheiro(self, valor):
        '''
        Adiciona o valor ao saldo da conta do cliente e registra a transação na lista de transações.

        Parâmetros: 
            valor(float): Valor depositado em conta.
        '''
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _definir_limite(self):
        '''
        Define o limite da conta do cliente.

        Atributo: 
            limite(float): Limite disponível em conta.
        '''
        self._limite = -1000
        return self._limite
    
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
        if self._saldo - valor < self._definir_limite():
            print('Você não possui saldo e(ou) limite para sacar esse valor.')
            self.consultar_saldo()
            self.consultar_limite()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
    
    def consultar_transacoes(self):
        '''
        Exibe o histórico de transações da conta do cliente que foi armazenado na lista de transações. 
        Não há parâmetros necessários.
        '''
        print('Histórico de Transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        '''
        Transfere o valor de uma conta, caso a diferença entre o valor inserido e o saldo atual seja menor do que o limite em conta, para uma segunda conta de destino. Após isso, registra a transação na lista de transações para cada conta.

        Parâmetros: 
            valor(float): Valor depositado em conta.
            conta_destino: Objeto conta para o qual será feita a operação.
        '''
        if self._saldo - valor < self._definir_limite():
            print('Você não possui saldo e(ou) limite para realizar essa transferência.')
            self.consultar_saldo()
            self.consultar_limite()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            conta_destino._saldo += valor
            conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:
    '''
    Cria um objeto CartaoCredito para gerenciar os cartões de crédito das contas dos clientes

    Atributos:
        numero (int): Número inteiro gerado aleatoriamente com 16 dígitos
        titular (str): Nome do cliente
        validade(str): Data gerada através do método estático contando 4 anos após a criação do cartão
        cod_seguranca(int): 3 números inteiro gerados aleatoriamente
        limite(float): Limite do cartão
        conta_corrente: conta do cliente associada aos cartões
    '''
    
    @staticmethod
    def _validade():
        ano = datetime.now().year + 4
        mes = datetime.now().month
        return datetime(ano, mes,1).strftime('%m/%y')

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = CartaoCredito._validade()
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = 1000
        self._senha ='1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
    
    @property
    def senha (self):
        return self._senha
    
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('Nova senha inválida')