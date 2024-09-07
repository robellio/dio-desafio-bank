def obter_cliente_por_cpf(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def recuperar_conta_cliente(cliente):
    
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return None
    return cliente.contas[0]

def listar_contas(contas):
    
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada! @@@")
        return

    for conta in contas:
        print("=" * 100)
        print(str(conta))  
        print("=" * 100)
