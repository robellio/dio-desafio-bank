from datetime import datetime

class Transacao:
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def __str__(self):
        return f"{self.tipo} de R$ {self.valor:.2f} em {self.data.strftime('%d-%m-%Y %H:%M:%S')}"
