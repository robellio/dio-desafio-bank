from models.conta import Conta

class ContaCorrente(Conta):

    def __init__ (self, numero, cliente, limite=1200, limite_saques=3):
        super().__init__(numero, cliente) 
        self()._limite = limite 
        self._limite_saques = limite_saques 

    def verificar_limite_saque(self, valor):
        numero_saques = len([t for t in self._historico.transacoes if t["tipo"] == "Saque"])    
        if numero_saques >= self._limite_saques:
            print("\n### Operação falhou! Limite de saques excedido. ###")
            return False 
        if valor > self._limite:
            print("\n### Operação falhou! Valor excede o limite de saque. ###")
            return False 
        return True 


    def sacar(self, valor):
        if self.verificar_limite_saque(valor):
            return super().sacar(valor)
        return False
    