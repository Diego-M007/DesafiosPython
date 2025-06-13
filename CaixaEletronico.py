saldo = int(1000)


def Menu():
    print("Opções")
    print("1- Ver Saldo")
    print("2- Sacar")
    print("3- Depositar")
    print("4- Sair")
    print("____________")


def mostrar_saque(saldo):
    saque = int(input("Digite o valor do saque:  "))
    if saque <= 0:
        print("valor inválido")
    elif saque > saldo:
        print("Saldo insuficiente")
        print("____________")
    else:
        print("____________")
        print("Saque efetuado com sucesso")
        saldo -= saque
        print("____________")
        print("Saldo Restante: ", "R$", saldo)
        print("____________")
    return saldo


def mostrar_deposito(saldo):
    deposito = int(input("Digite o valor do depósito: "))
    saldo += deposito
    print("Depósito efetuado com sucesso")
    print("____________")
    print("Saldo atual:", "R$", saldo)
    return saldo


def mostrar_saldo(saldo):
    print("R$", saldo)
    print("____________")


while True:
    Menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        mostrar_saldo(saldo)
    elif opcao == 2:
        saldo = mostrar_saque(saldo)
    elif opcao == 3:
        saldo = mostrar_deposito(saldo)
    elif opcao == 4:
        print("Obrigado por usar o sistema")
        break
    else:
        print("================")
        print("Digite uma opção válida")
        print("================")
