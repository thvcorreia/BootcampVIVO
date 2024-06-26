# Sistema bancário V2
import textwrap

def menu():
    menu = """
    ********* Menu **********
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Criar Usuário
    [5] - Listar Contas
    [6] - Criar Conta
    [7] - Realtório Usuários
    [0] - Sair

    -> """
    return input(menu)


def depositar(saldo, valor, extrato, /):
    # Recebendo os valores somente por posição, /
    if valor > 0:
        saldo += valor
        extrato += f"+ Deposito: R$ {valor:.2f}\n"            
        print(f"++++ Deposito realizado com sucesso: RS$ {valor:.2f} ++++")
    else:
        print("---- Operação falhou! Valor inválido para depósito ----")
    # Retornando os valores    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numeros_saques, limite_saques):
    # Pré-verificações
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeros_saques >= limite_saques
    # Validando as pré-verificações
    if excedeu_saldo:
        print("---- Não foi possível efetuar o saque por falta de saldo ----")

    elif excedeu_limite:
        print(f"---- Você só pode sacar R$ {limite} por vez e no máximo {limite_saques} vezes por dia ----")

    elif excedeu_saques:
        print(f"---- Você ultrapassou o limites de saques por dia: {numeros_saques} de {limite_saques} ----")

    elif valor > 0:
        saldo -= valor
        numeros_saques += 1
        extrato += f"- Saque: R$ {valor:.2f}\n"            
        print(f"++++ Saque realizado com sucesso: RS$ {valor:.2f} ++++")

    else:
        print("---- Valor inválido!\nTente novamente! ----")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    if extrato:
        print(saldo)
        print(extrato)
        print(f" EXTRATO ".center(60, "+"))
        print()
        print(f"{extrato}")
        print(f"\nSeu saldo é: R$ {saldo:.2f}")
        print(f" FIM ".center(60, "-"))
    else:
        print("----Não foram realizadas movimentações----")
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe CPF (somente números)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"Já existe um usuário com o CPF: {cpf}")
        return
    else:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("informe a data de anscimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (ogradouro, númeor - bairro - cidade/Sigla Estado): ")
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("++++ Usuário criado com sucesso! ++++")    


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


def listar_contas(contas):
    for conta in contas:
        linha = f"""\Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']}"""
        print("+" * 100)
        print(textwrap.dedent(linha))


def listar_usuario(usuarios):
    for usuario in usuarios:
        linha = f"""\nUsuário: \t{usuario['nome']}
        CPF:\t\t{usuario['cpf']}
        Endereço:\t{usuario['endereco']}"""
        print("+" * 100)
        print(textwrap.dedent(linha))
        print("+" * 100)


def main(): 
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0
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
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
           criar_usuario(usuarios)

        elif opcao == "5":
           listar_contas(contas)
        
        elif opcao == "6":            
            numero_conta += 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "7":
            listar_usuario(usuarios)

        elif opcao == "0":
            print("Obrigado por usar nossos serviços, estamos aqui para melhor atender-lo")
            break

        else:
            print("Opção inválida, tente novamente!")
    

main()