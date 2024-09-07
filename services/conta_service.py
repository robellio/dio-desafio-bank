from models.conta_corrente import ContaCorrente
from utils.helpers import obter_cliente_por_cpf
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
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF: ")
    cliente = obter_cliente_por_cpf(cpf, clientes)
    if not cliente:
        return
    try:
        limite = float(input("Informe o limite de saque: "))
        limite_saques = int(input("Informe o número máximo de saques por dia: "))
        nova_conta = ContaCorrente(numero_conta, cliente, limite, limite_saques)
        contas.append(nova_conta)
        cliente.adicionar_conta(nova_conta)
        print("\n=== Conta criada com sucesso! ===")
    except ValueError:
        print("\n@@@ Valor inválido! @@@")
