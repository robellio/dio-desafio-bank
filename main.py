from services.cliente_service import criar_cliente
from services.conta_service import criar_conta
from services.transacao_service import realizar_deposito, realizar_saque
from utils.menu import menu
from utils.helpers import obter_cliente_por_cpf, recuperar_conta_cliente, listar_contas
from models.pessoa_fisica import PessoaFisica
from utils.helpers import obter_cliente_por_cpf


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

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = obter_cliente_por_cpf(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            realizar_deposito(clientes)

        elif opcao == 's':
            realizar_saque(clientes)

        elif opcao == 'e':
            exibir_extrato(clientes)    

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'nu':
            criar_cliente(clientes)

        elif opcao == 'q':
            break

if __name__ == "__main__":
    main()
