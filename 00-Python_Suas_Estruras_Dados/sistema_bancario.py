# Sistema bancário V1

menu = """
[1] - Deposito
[2] - Saque
[3] - Extrato
[4] - Sair
"""

saldo = 0
MAXIMO_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
i = 0

while True:
    opcao = input(menu)
    
    if opcao == "1":
        deposito = float(input("Informe o valor o para depósito: "))

        if deposito > 0:
            saldo += deposito
            i += 1
            extrato += f"{i} - Deposito: R$ {deposito:.2f}\n"            
            print(f" Deposito realizado com sucesso: RS$ {deposito:.2f}")
            deposito = 0

        else:
            print("Operação falhou! Valor inválido para depósito")

    elif opcao == "2":
        saque = float(input("Informe o valor a sacar: "))

        if saque > saldo or saldo <= 0:
            print("Não foi possível efetuar o saque por falta de saldo")

        elif saque > 500:
            print(f"Você só pode sacar R$ {MAXIMO_SAQUE} por vez e no máximo {LIMITE_SAQUES} vezes por dia")

        elif numero_saques >= LIMITE_SAQUES:
            print(f"Você ultrapassou o limites de saques por dia: {numero_saques} de {LIMITE_SAQUES}")

        else:
            saldo -= saque
            i += 1
            numero_saques += 1
            extrato += f"{i} - Saque: R$ {saque:.2f}\n"            
            print(f"Saque realizado com sucesso: RS$ {saque:.2f}")

    elif opcao == "3":

        if extrato:
            print(f" EXTRATO ".center(60, '-'))
            print()
            print(f"{extrato}")
            print(f"\nSeu saldo é: R$ {saldo:.2f}")
            print(f" FIM ".center(60, '-'))

        else:
            print("Não foram realizadas movimentações")

    elif opcao == "4":

        print("Obrigado por usar nossos serviços, estamos aqui para melhor atender-lo")
        break

    else:
        print("Opção inválida, tente novamente!")

