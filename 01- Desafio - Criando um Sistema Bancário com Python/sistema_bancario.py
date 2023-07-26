# Matheus Rodrigues Silva Maia

# DEPÓSITO
# - Valores Positivos
# - Armazenar depósitos no Extrato

# SAQUE
# - 3 Saques diários
# - Limite de R$500,00 por saque
# - Tratar saldo insuficiente
# - Armazenar saques no Extrato

# EXTRATO
# - Exibe todos os depósitos e saques
# - Se extrato estiver em branco, avisar que não foram realizadas movimentações


menu = '''=======MENU=======
[d] -> Depósito
[s] -> Saque
[e] -> Ver Extrato
[q] -> Sair\n'''

LIMITE_SAQUES = 3
LIMITE_VALOR = 500

saldo = 0
saques = 0
extrato = ""
operations = 0

while True:
    
    operation = input(menu)

    # Deposito
    if operation == 'd':
        deposito = float(input("\nInsira o valor a ser depositado: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"# Deposito de R${deposito:.2f}\n  Saldo final: R${saldo:.2f}\n\n"
            print(f"\nDepósito de R${deposito:.2f} realizado com sucesso!\nSeu saldo agora é de R${saldo:.2f}\n\n")
            operations += 1

        elif type(deposito) != type(100.00):
            print("Valor inválido, tente novamente mais tarde")

        else:
            print("Valor inválido, tente novamente mais tarde")

    # Saque
    elif operation == 's':
        saque = float(input("\nInsira o valor que deseja sacar: "))

        if saque < 0: 
            print("Valor inválido, tente novamente mais tarde\n\n")

        elif saque > 500:
            print(f"Saque de {saque:.2f} não permitido\nExcede o limite de R$500.00\n\n")

        elif saques >= 3:
            print("Você alcançou o limite de 3 saques diários!\n\n")

        elif saque > saldo:
            print(f"Você tentou sacar R${saque:.2f}, e se saldo é de R${saldo:.2f}\nSaldo Insuficiente\n\n")

        else:
            saldo -= saque
            saques += 1
            extrato += f"# Saque de R${saque:.2f}\n  Saldo final: R${saldo:.2f}\n\n"
            print(f"\nSaque de R${saque:.2f} realizado com sucesso!\nSeu saldo agora é de R${saldo:.2f}")
            print(f"Você ainda possui {3 - saques} saques disponíveis hoje\n\n")
            operations += 1

    # Visualizar Extrato
    elif operation == 'e':
        
        if operations <= 0:
            print("Ainda não foram realizadas movimentações na conta\n\nd")

        else:           # Saque de R${saque:.2f}
            print(f'''\n======== EXTRATO ========\n{extrato}''')

    # Fim do Programa
    elif operation == 'q':
        break

    else:
        print("\nOperação Inválida!")


print("\nObrigado por utilizar nossos serviços! :)")