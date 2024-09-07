from models.pessoa_fisica import PessoaFisica


def criar_cliente(clientes):
    cpf = input("Informe o CPF: ")
    if next((cliente for cliente in clientes if cliente.cpf == cpf), None):
        print("\n### CPF ja cadastrado! ###")
        return 
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaa): ")
    endereco = input("Informe o endereço: ")
    clientes.append(PessoaFisica(nome, data_nascimento, cpf, endereco)) 
    print("\n=== Cliente criado com sucesso! ===")