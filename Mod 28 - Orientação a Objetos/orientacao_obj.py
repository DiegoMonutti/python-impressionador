from datetime import datetime
import pytz


class ContaCorrente:

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
        print(f'Seu saldo atual é de R$ {self.saldo:,.2f}')

    def depositar_dinheiro(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _definir_limite(self):
        self.limite = -1000
        return self.limite
    
    def consultar_limite(self):
        print(f'Seu limite do Cheque Especial é de R$ {-1*(self._definir_limite()):,.2f}')

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._definir_limite():
            print('Você não possui saldo e(ou) limite para sacar esse valor.')
            self.consultar_saldo()
            self.consultar_limite()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
    
    def consultar_transacoes(self):
        print('Histórico de Transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
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