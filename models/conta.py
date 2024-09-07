from models.historico import Historico


class Conta:

    def __init__ (self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod 
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo 

    @property 
    def numero(self):
        return self._numero 

    @property
    def agencia(self):
        return self._agencia

    @property 
    def cliente(self):
        return self._cliente 

    @property 
    def historico(self):
        return self._historico    
    
    def sacar(self, valor):
        if not self.verificar_limite_saque(valor):
            return False
        
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        elif valor > self.saldo:
            print("\n### Operação falhou! Saldo insuficiente. ###")
            return False
        self._saldo -= valor 
        print("\n=== Saque realizado com sucesso! ===")
        return True
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor 
        print("\n=== Depósito realizado com sucesso! ===")
        return True
    
    def exibir_extrato(self):
        
        print("\n=== Extrato da Conta ===")
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.numero}")
        print(f"Titular: {self.cliente}")
        print(f"Saldo atual: {self.saldo}")
        print("\n=== Histórico de Transações ===")
        for transacao in self._historico.transacoes:
            print(f"- {transacao}")
        print("===========================")
    
    def __str__(self):
        return f"Agência: {self.agencia}\nConta: {self.numero}\nTitular: {self.cliente}"