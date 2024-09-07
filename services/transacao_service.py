from models.deposito import Deposito
from models.pessoa_fisica import PessoaFisica
from models.saque import Saque
from utils.helpers import obter_cliente_por_cpf, recuperar_conta_cliente


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
def realizar_deposito(clientes):
    cpf = input("Informe o CPF: ")
    cliente = obter_cliente_por_cpf(cpf, clientes)
    if not cliente:
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    try:
        valor = float(input("Informe o valor do depósito: "))
        transacao = Deposito(valor)
        cliente.realizar_transacao(conta, transacao)
    except ValueError:
        print("\n@@@ Valor inválido! @@@")

def realizar_saque(clientes):
    cpf = input("Informe o CPF: ")
    cliente = obter_cliente_por_cpf(cpf, clientes)
    if not cliente:
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    try:
        valor = float(input("Informe o valor do saque: "))
        transacao = Saque(valor)
        cliente.realizar_transacao(conta, transacao)
    except ValueError:
        print("\n@@@ Valor inválido! @@@")
