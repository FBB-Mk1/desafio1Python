print("Bem vindo ao pior banco do mundo:")
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

    if opcao == "d":
        valor_deposito = float(input("Quanto você deseja depositar: "))
        if valor_deposito <= 0:
            print("Valor inválido, digite um valor positivo")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito realizado: R$ {valor_deposito:.2f}\n")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            while True:
                valor_saque = float(input("Quanto você deseja sacar: "))
                
                if valor_saque <= 0:
                    print("Valor de saque inválido, digite um valor positivo.")
                elif valor_saque > limite:
                    print("Saque acima do limite. Seu limite atual por saque é de: R$ 500.00")
                elif valor_saque > saldo:
                    print(f"Saldo indisponível, seu saldo é de: R$ {saldo:.2f}")
                else:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                    break
        else:
            print("Limite de saques do dia atingido")


    elif opcao == "e":
       print("========EXTRATO========")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print(f"Saldo: R$ {saldo:.2f}")
       print("=======================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
