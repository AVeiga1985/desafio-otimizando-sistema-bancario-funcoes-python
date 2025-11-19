menu_admin = """

[c] Criar Usuário
[cc] Criar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[l] Listar Conta
[q] Sair

=> """

menu_usuario = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n----> Depósito realizado com sucesso! <----")
    else:
        print("\n!!!!!-> Operação falhou! O valor informado é inválido. <-!!!!!")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\n!!!!!-> Operação falhou! Você não tem saldo suficiente. <-!!!!!")

    elif excedeu_limite:
        print("\n!!!!!-> Operação falhou! O valor do saque excede o limite. <-!!!!!")

    elif excedeu_saques:
        print("\n!!!!!-> Operação falhou! Número máximo de saques excedido. <-!!!!!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n----> Saque realizado com sucesso!  <----")
    else:
        print("\n!!!!!->Operação falhou! O valor informado é inválido. <-!!!!!")

    return saldo, extrato


def exibir_extrato (saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return extrato


def criar_usuario (usuarios):
    cpf = input("Digite o CPF do usuário (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n!!!!!-> Usuário cadastrado! <-!!!!!")
        return
    
    nome = input("Digite o seu nome completo: ")
    data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
    endereco = input("Digite o endereço do usuário (rua, n° - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("----> Usuário criado com sucesso! <----")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário (apenas números):")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n----> Conta criada com sucesso! <----")

        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n!!!!!-> Usuário não encontrado. Não foi possível criar a conta corrente!  <-!!!!!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(f"{linha}")


login = input("\nEntre com o CPF cadastrado ou digite (z) para encerrar o sistema: ")

while login != "z":

    if login == "12345678909":
        print("\n", "#" * 10, " MARKETI9 BANK ", "#" * 10, "\n")
        print("\nSeja Muito Bem-Vindo Ao Nosso Sistema\n")
        print("\nVocê é administrador!")

        while True:

            opcao = input(menu_admin)

            if opcao == "c":
                criar_usuario(usuarios)

            elif opcao == "cc":
                numero_conta = len(contas) + 1
                conta = criar_conta(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)

            elif opcao == "d":
                valor = float(input("Digite o valor do depósito: "))
                saldo, extrato = depositar(saldo, valor, extrato)

            elif opcao == "s":
                valor = float(input("Digite o valor do saque: "))

                saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)
            
            elif opcao == "e":

                exibir_extrato(saldo, extrato=extrato)

            elif opcao == "l":
                listar_contas(contas)
            
            elif opcao == "q":
                break

            else:
                print("\n!!!!!-> Operação inválida, por favor selecione novamente a operação desejada. <-!!!!!")

    else:
        print("\n", "#" * 10, " MARKETI9 BANK ", "#" * 10, "\n")
        print("\nSeja Muito Bem-Vindo Ao Nosso Sistema\n")
        print("\nVocê é usuário!")

        usuario = filtrar_usuario(login, usuarios)

        if usuario:

            while True:

                opcao = input(menu_usuario)

                if opcao == "c":
                    criar_usuario(usuarios)

                elif opcao == "cc":
                    numero_conta = len(contas) + 1
                    conta = criar_conta(AGENCIA, numero_conta, usuarios)

                    if conta:
                        contas.append(conta)

                elif opcao == "d":
                    valor = float(input("Digite o valor do depósito: "))
                    saldo, extrato = depositar(saldo, valor, extrato)

                elif opcao == "s":
                    valor = float(input("Digite o valor do saque: "))

                    saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)
                
                elif opcao == "e":

                    exibir_extrato(saldo, extrato=extrato)

                elif opcao == "l":
                    listar_contas(contas)
                
                elif opcao == "q":
                    break

                else:
                    print("\n!!!!!-> Operação inválida, por favor selecione novamente a operação desejada. <-!!!!!")
            
            
        else:
            print("\n!!!!!-> Usuário não encontrado. Fale com o gerente para realizar o seu cadastro! <-!!!!!")


    login = input("Entre com o CPF cadastrado ou digite (z) para encerrar o sistema: ")