menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n================ DEPOSITO ================")
            print(f"Valor depositado: {valor:.2f}")
            print("\n==========================================")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao.lower() == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

      
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n==================SAQUE==================")
            print(f"Saque Realizado no Valor de : {valor:.2f}")
            print("\n==========================================")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao.lower() == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao.lower() == "q":
        print("\n================================")
        print("\nSistema Encerrado com Sucesso")
        print("\n================================")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")