menu = """

[e]Entrada
[r]Retirar
[h]Historico
[s]sair
=> """

saldo = 0
limite = 500
historico = ""
numero_retiradas = 0
LIMITE_RETIRADAS = 3

while True:
    opcao = input(menu) 
    if opcao == "e":
        valor = float(input("Qual será o valor do depósito?: "))

        if valor > 0:
            saldo += valor
            historico += f"deposito: R$ {valor:.2f}\n"
    
        else:
            print("a operação falhou! o valor e invalido.")

    elif opcao == "r":
        valor = float(input("Qual será o valor do saque?: "))
        excedeu_saldo = valor > saldo   
        excedeu_limite = valor > limite
        excedeu_retiradas = numero_retiradas >= LIMITE_RETIRADAS
        
        if excedeu_saldo:
            print("Falha! Você não tem saldo suficiente.") 
        elif excedeu_limite:
            print("Falha! O valor da retirada exede o limite.")
        elif excedeu_retiradas:   
            print("Falha! Numero de retirada diaria foi exedido.")  

        elif valor > 0:
            saldo -= valor
            historico += f"Retirada: R$ {valor:.2f}\n"
            numero_retiradas += 1

        else:
            print("Falha! Valor inválido")

    elif opcao == "h":
            print("\n==========Historico==========")
            print("Nenhuma movimentação realizada") if not historico else historico
            print(f"\nHistorico: R$ {saldo:.2f}")
            print("==============================")

    elif opcao == "s":
                break
    else:
                print("Opção invalida, selecione novamente a opção desejada.")