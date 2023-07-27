# Matheus Rodrigues Silva Maia

# DEPÓSITO
# - Positional only
# - (saldo, valor, extrato)
# - Retorna saldo e extrato

# SAQUE
# - Keyword only **kwargs
# - (saldo, valor, extrato, numero_saques, limite_saques)
# - Retorna saldo e extrato

# EXTRATO
# - Positional only (saldo) e keyword only (extrato)

# CRIAR USUÁRIO
# - Armazena usuários em uma lista (Lista de Dicionários)
# - Composto por:
#   - Nome
#   - CPF (Numbers only (Sem pontos e hífen))
#   - Endereço (Logradouro, Numero - Bairro - Cidade/Estado)
#   > Filtro para não haver 2 users com mesmo CPF

# CRIAR CONTA CORRENTE
# - Armazena usuários em uma lista (Lista de Dicionários)
# - Composto por:
#   - Agência
#   - Número de conta (Iterado automaticamente)
#   - Número da Agência (Fixo "0001")
#   > Filtro para poder ter mais de uma conta por usuário, mas nunca mais de 1 usuário dividindo uma mesma conta

# LISTAR CONTAS

import textwrap

def menu():
    menu = '''=======MENU=======
[d]\tDepósito
[s]\tSaque
[nu]\tCriar Usuário
[nc]\tCriar Conta Corrente
[l]\tListar Contas
[e]\tExibir Extrato
[q]\tSair

==> '''

    return input(textwrap.dedent(menu))

def realiza_depositos(saldo, deposito, extrato, operations, /):

    if deposito > 0:
        saldo += deposito
        extrato += f"# Deposito de\tR${deposito:.2f}\nSaldo final:\tR${saldo:.2f}\n\n"
        print(f"\n=== Depósito de R${deposito:.2f} realizado com sucesso! ===\nSeu saldo agora é de R${saldo:.2f}\n\n")
        operations += 1

    elif type(deposito) != type(100.00):
        print("--- Valor inválido, tente novamente mais tarde ---")

    else:
        print("--- Valor inválido, tente novamente mais tarde ---")
    
    return saldo, extrato, operations

def realiza_saques(*, saldo, saque, extrato, limite, limite_saques, numero_saques, operations):

    excedeu_valor_limite = saque > limite
    excedeu_limite = numero_saques >= limite_saques


    if excedeu_valor_limite:
        print(f"--- Saque de {saque:.2f} não permitido ---\nExcede o limite de R$500.00\n\n")

    elif excedeu_limite:
        print("--- Você alcançou o limite de 3 saques diários! ---\n\n")

    elif saque > saldo:
        print(f"--- Você tentou sacar R${saque:.2f}, e seu saldo é de R${saldo:.2f} ---\nSaldo Insuficiente\n\n")

    elif saque > 0:
        saldo -= saque
        numero_saques += 1
        extrato += f"# Saque de R${saque:.2f}\nSaldo final:\tR${saldo:.2f}\n\n"
        print(f"\n=== Saque de R${saque:.2f} realizado com sucesso! ===\nSeu saldo agora é de R${saldo:.2f}")
        print(f"Você ainda possui {limite_saques - numero_saques} saques disponíveis hoje\n\n")
        operations += 1
    
    else:
        print("--- Valor inválido, tente novamente mais tarde ---\n\n")

    return saldo, extrato, operations, numero_saques

def new_user(usuarios):
    cpf = int(input("\nInsira o CPF (Apenas números): "))

    if verify_cpf(usuarios, cpf):
        print("\n--- Usuário já Cadastrado! ---")
        return
    
    else:
        nome = input("Insira seu nome completo: ")
        nascimento = input("Insira sua data de nascimento no modelo (dd-mm-aaaa): ")
        endereco = input("Insira seu endereço no formato (Logradouro, Numero - Bairro - Cidade/Estado): ")

        user = {"CPF": cpf, "nome": nome, "nascimento": nascimento, "endereco": endereco}
        print("=== Usuario Cadastrado com Sucesso! ===\n")
        usuarios.append(user)

def new_account(*, agencia, usuarios, numero_conta):
    cpf = int(input("Insira o CPF do usuario que tera a conta: "))
    user = verify_cpf(usuarios, cpf)

    if user:
        print(f"\n=== Conta Cadastrada com Sucesso! ===\n")
        return {"user": user, "conta": numero_conta, "agencia": agencia}

    print("--- Usuário não encontrado, tente mais tarde com um CPF válido! ---\n")

# Retorna o usuário dono daquele cpf
def verify_cpf(usuarios, cpf):
    cpf_existente = [user for user in usuarios if user["CPF"] == cpf]
    return cpf_existente[0] if cpf_existente else None

def listar_contas(contas):
    print("LISTA DE CONTAS CRIADAS".center(80, "="))
    for conta in contas:
        print("=" * 80)
        print(textwrap.dedent(f"""Nome do Titular:\t{conta["user"]["nome"]}
CPF do Titular:\t{conta["user"]["CPF"]}
Agência:\t\t{conta["agencia"]}
Numero:\t\t{conta["conta"]}\n
"""))

def view_extrato(saldo, /, *, extrato):
        print('''\n======== EXTRATO ========\n''')
        print("Ainda não foram realizadas movimentações na conta\n\nd" if not extrato else extrato)
        print(f"\nSaldo Final:\t\tR$ {saldo:.2f}")
        print("==========================================")

LIMITE_SAQUES = 3
LIMITE_VALOR = 500
AGENCIA = "0001"

saldo = 0
saques = 0
extrato = ""
operations = 0
numero_saques = 0
usuarios = []
contas = []

while True:
    
    operation = menu()

    # Deposito
    if operation == "d":
        deposito = float(input("\nInsira o valor a ser depositado: "))

        saldo, extrato, operations = realiza_depositos(saldo, deposito, extrato, operations)

    # Saque
    elif operation == "s":
        saque = float(input("\nInsira o valor que deseja sacar: "))

        saldo, extrato, operations, numero_saques = realiza_saques(
            saldo = saldo,
            saque = saque,
            extrato = extrato,
            limite = LIMITE_VALOR,
            limite_saques = LIMITE_SAQUES,
            numero_saques = numero_saques,
            operations = operations,
        )

    # Novo Usuário
    elif operation == "nu":
        new_user(usuarios)

    # Nova Conta Corrente
    elif operation == "nc":
        id_conta = len(contas) + 1
        contas.append(new_account(agencia = AGENCIA,
                    usuarios = usuarios,
                    numero_conta = id_conta))

    # Listar contas correntes
    elif operation == "l":
        listar_contas(contas)

    # Visualizar Extrato
    elif operation == 'e':
       view_extrato(saldo, extrato = extrato) 
    
    # Fim do Programa
    elif operation == 'q':
        break

    else:
        print("\nOperação Inválida!")


print("\nObrigado por utilizar nossos serviços! :)")