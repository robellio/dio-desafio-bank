from models.cliente import Cliente

class PessoaFisica(Cliente):
    
    def __init__ (self, nome, data_nascimento, cpf, endereco):
        super().__init__ (endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento 
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome}"