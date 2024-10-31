import textwrap

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair

    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depóstio realizado com sucesso!")  
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > limite:
        print("Saque maior que o limite de R$ 500.00")
    elif numero_saques > limite_saques:
        print("Limite de 3 saques diários atingidos!")
    elif saldo < valor:
        print("Saldo insuficiente!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo:\t\tR$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("O usuário já está cadastrado.")
        return
    
    nome = input("Informe nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereço (logradouro, nro = bairro - cidade/sigla estado):")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("Usuário criado com sucesso")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    valor = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input("Digite o valor a ser depósitado:\n"))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 's':
            print("Saque")
            valor = float(input("Digite o valor a ser sacado.\n"))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break
            
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()