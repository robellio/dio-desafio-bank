import textwrap

def menu():
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo cliente
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto))
