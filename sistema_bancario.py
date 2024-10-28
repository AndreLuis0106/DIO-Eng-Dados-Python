menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor = 0

while True:
    opcao = input(menu)
    
    if opcao == 'd':
        print("Depósito")
        valor = int(input("Digite o valor a ser depósitado.\n"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Saldo atual: {saldo:.2f}\n")
    
    elif opcao == 's':
        print("Saque")
        valor = int(input("Digite o valor a ser sacado.\n"))
        if valor > limite:
            print("Saque maior que R$ 500.00")
        elif numero_saques == LIMITE_SAQUES:
            print("Limite de 3 saques diários atingidos!")
        elif saldo < valor:
            print("Saldo insuficiente!")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saldo atual: {saldo:.2f}\n")
            numero_saques += 1
        
    elif opcao == 'e':
        print("Extrato")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        
    elif opcao == 'q':
        break
        
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")