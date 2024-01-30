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
        print('Depósito selecionado')
        while True:
            
            valor_deposito = input('Digite o valor que deseja depositar: R$')
            valor_deposito = float(valor_deposito)
                
            if valor_deposito > 0:
                saldo += valor_deposito
                print(f'O saldo atual é: R${saldo}')
                extrato += f'R${valor_deposito:.2f} - Depósito \n'
                break
                
            else:
                print('Digite um valor válido para o depósito')
        
    elif opcao == "s":
        print('Saque selecionado')
        
        while True:
            valor_saque = input('Digite o valor que deseja sacar: R$')
            valor_saque = float(valor_saque)
                
            if valor_saque > saldo:
                print('Não existe saldo suficiente para a operação.')
                break
                    
            elif numero_saques >= LIMITE_SAQUES: 
                print('Operação falhou! Limite de saques diários atingidos')
                break
                    
            elif valor_saque > limite:
                print(f'Operação falhou! O valor do saque ultrapassa o limite permitido de R${limite}')
                    
            elif valor_saque > 0:
                saldo -= valor_saque
                numero_saques += 1
                print(f'Foi realizado o saque de R${valor_saque} \nSaldo atual R${saldo}')
                extrato += f'R${valor_saque:.2f} - Saque \n'
                break
                
            else:
                print('Digite um valor válido para o saque')
                
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não houveram movimentações na conta." if not extrato else extrato)
        print(f'\nSaldo atual R${saldo:.2f}')
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")