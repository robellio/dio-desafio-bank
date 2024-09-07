from models.transacao import Transacao

class Deposito(Transacao):

    def __init__ (self, valor):
        self._valor = valor

    def __str__(self):
        return f"Depósito de R$ {self.valor:.2f} em {self.data.strftime('%d-%m-%Y %H:%M:%S')}"
        
    @property 
    def valor(self):
        return self._valor 
    
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
    
   