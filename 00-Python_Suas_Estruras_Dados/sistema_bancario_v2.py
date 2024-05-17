# Sistema bancário V2


def menu():
    menu = """
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Criar Usuário
    [5] - Listar Contas
    [6] - Criar Conta
    [0] - Sair
    """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    # Recebendo os valores somente por posição, /
    if valor > 0:
        saldo += valor
        extrato += f"+ Deposito: R$ {valor:.2f}\n"            
        print(f"++++ Deposito realizado com sucesso: RS$ {valor:.2f} ++++")
        deposito = 0
    else:
        print("---- Operação falhou! Valor inválido para depósito ----")


def sacar(*, saldo, valor, extrato, limite, numeros_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques >= limite_saques

    if excedeu_saldo:
        print("---- Não foi possível efetuar o saque por falta de saldo ----")

    elif excedeu_limite:
        print(f"---- Você só pode sacar R$ {limite} por vez e no máximo {limite_saques} vezes por dia ----")

    elif excedeu_saques:
        print(f"---- Você ultrapassou o limites de saques por dia: {numero_saques} de {limite_saques} ----")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"- Saque: R$ {valor:.2f}\n"            
        print(f"++++ Saque realizado com sucesso: RS$ {valor:.2f} ++++")

    else:
        print("---- Valor inválido!\nTente novamente! ----")


def extrato(saldo, /, *, extrato):
    if extrato:
        print(f" EXTRATO ".center(60, '+'))
        print()
        print(f"{extrato}")
        print(f"\nSeu saldo é: R$ {saldo:.2f}")
        print(f" FIM ".center(60, '-'))

    else:
        print("----Não foram realizadas movimentações----")


def criar_usuario(usuarios):
    cpf = input("Informe CPF (somente números)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        return f"Já existe um usuário com o CPF: {cpf}"
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("informe a data de anscimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (ogradouro, númeor - bairro - cidade/Sigla Estado): ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf "endereco": endereco})
        print("++++ Usuário criado com sucesso ++++")    


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = cpf = input("Informe CPF do usuário")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n++++ Conta criada com sucesso! ++++")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("---- Usuário não encontrado! Tente novamente! ----")


def listar_contas():
    pass


def listar_usuario():
    pass


def main(): 
    AGENCIA = 27
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()
    
        if opcao == "1":
            valor = float(input("Informe o valor o para depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeros_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            extrato()

        elif opcao == "4":
           criar_usuario()

        elif opcao == "5":
           listar_contas()
        
        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "0":
            print("Obrigado por usar nossos serviços, estamos aqui para melhor atender-lo")
            break

        else:
            print("Opção inválida, tente novamente!")
    

main()