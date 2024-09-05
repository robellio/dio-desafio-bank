class Conta:

    def __init__ (self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo     
    
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
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