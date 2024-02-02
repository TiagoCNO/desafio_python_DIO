import textwrap


def menu():
    
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def deposito(saldo, valor, extrato, /):
            print('Depósito selecionado')
                    
            if valor > 0:
                saldo += valor
                print(f'O saldo atual é: R${saldo}')
                extrato += f'R${valor:.2f} - Depósito \n'
            
            else:
                print('Digite um valor válido para o depósito')

            return saldo, extrato
        

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
            
            print('Saque selecionado')
                
            if valor > saldo:
                print('Não existe saldo suficiente para a operação.')
                    
            elif numero_saques >= limite_saques: 
                print('Operação falhou! Limite de saques diários atingidos')
                    
            elif valor > limite:
                print(f'Operação falhou! O valor do saque ultrapassa o limite permitido de R${limite}')
                    
            elif valor > 0:
                saldo -= valor
                numero_saques += 1
                print(f'Foi realizado o saque de R${valor} \nSaldo atual R${saldo}')
                extrato += f'R${valor:.2f} - Saque \n'
                
            else:
                print('Digite um valor válido para o saque')
            
            return saldo, extrato, numero_saques
        

def imprimir_extrato(saldo, /, *, extrato):
            print("\n================ EXTRATO ================")
            print("Não houveram movimentações na conta." if not extrato else extrato)
            print(f'\nSaldo atual R${saldo:.2f}')
            print("==========================================")
            

def criar_usuario(usuarios):
    cpf = input('Informe somente os números do CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n**** CPF já cadastrado no sistema! ****')
        return
    
    nome = input('Informe seu nome completo: ')
    data_de_nascimento = input('Informe sua data de nascimento (DD/MM/AAAA): ')
    endereco = input('Informe seu endereço (lagradouro, num - bairro - cidade/sigla Estado): ')
    
    usuarios.append({'nome': nome, 
                     'data_de_nascimento': data_de_nascimento, 
                     'cpf': cpf,
                     'endereco': endereco})
    
    print('\n==== Usuário criado! ====')
    

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe somente os números do CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n==== Conta criada! ====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n**** Usuário não encontrado, conta não pode ser criada! ****")
    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input('Digite o valor que deseja depositar: R$'))
            
            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input('Digite o valor que deseja sacar: R$'))
            
            saldo, extrato, numero_saques = saque(saldo = saldo, 
                                                  valor = valor, 
                                                  extrato = extrato, 
                                                  limite = limite, 
                                                  numero_saques = numero_saques, 
                                                  limite_saques = LIMITE_SAQUES)

        elif opcao == "e":
            imprimir_extrato(saldo, extrato = extrato)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
            
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()