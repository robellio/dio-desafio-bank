from models.transacao import Transacao
 
class Saque(Transacao):

    def __init__ (self, valor):
        self._valor = valor 

    def __str__(self):
        return f"Saque de R$ {self.valor:.2f} em {self.data.strftime('%d-%m-%Y %H:%M:%S')}"

    @property
    def valor(self):
        return self._valor 
    
    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
