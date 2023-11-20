from cliente import Cliente
from conta import Conta
from historico import Historico


def imprimir_todos_conjunto(conjunto_classes):
    for i in conjunto_classes:
        i.imprimir()


def encontrar_pelo_cpf(cpf, conjunto_classes):

    for i in conjunto_classes:

        if i.cpf == cpf:
            return i

    return None


def menu():
    """
    abrindo o arquivo com w apenas para limpar os dados anteriors, já que eles são gravados com a
    """

    with open("Contas.txt", "w") as arquivo:
        arquivo.write("")

    with open("Clientes.txt", "w") as arquivo:
        arquivo.write("")

    opcao = 0
    clientes = []
    contas = []
    h = Historico()

    while opcao != -1:
        print("\n|==================================================|\n"
              "|        BEM-VINDO, O QUE VOCÊ DESEJA FAZER?       |\n"
              "|==================================================|\n"
              "| 1 - Adicionar cliente e conta                    |\n"
              "| 2 - Imprimir informações de todos os clientes    |\n"
              "| 3 - Imprimir informações de todas as contas      |\n"
              "| 4 - Depositar na conta                           |\n"
              "| 5 - Sacar da conta                               |\n"
              "| 6 - Transferir de uma conta para outra           |\n"
              "| 7 - Imprimir histórico                           |\n"
              "|==================================================|\n"
              "| -1 - Encerrar programa                           |\n"
              "|==================================================|\n\n")

        opcao = int(input("Qual comando você deseja executar? "))

        if opcao == 1:

            cpf = input("Qual será o CPF desse cliente? ")
            nome = input("Qual será o nome desse cliente? ")
            numero_conta = input("Qual será o número de identificação da conta? ")
            saldo = int(input("Qual será o saldo inicial da conta? "))

            clientes.append(Cliente(cpf, nome))
            contas.append(Conta(cpf, numero_conta, saldo))
            print("Cliente e conta adicionados!")

            h = h.atualizar(f"Abertura: {str(cpf)}")

        elif opcao == 2:

            imprimir_todos_conjunto(clientes)

        elif opcao == 3:

            imprimir_todos_conjunto(contas)

        elif opcao == 4:

            cpf = input("Qual é o CPF identificador da conta em que você deseja depositar? ")
            valor = int(input("Qual é o valor que você deseja depositar? "))

            conta_desejada = encontrar_pelo_cpf(cpf, contas)

            if conta_desejada:
                conta_desejada.depositar(valor)
                h = h.atualizar(f"Depósito: {str(conta_desejada.cpf)}")
                print("Valor depositado!")

            else:
                print("Conta não encontrada.")

        elif opcao == 5:

            cpf = input("Qual é o CPF identificador da conta em que você quer sacar? ")
            conta_desejada = encontrar_pelo_cpf(cpf, contas)

            if conta_desejada:

                valor = int(input("Qual é o valor que você deseja sacar? "))

                if valor > conta_desejada.saldo:
                    """
                    como o valor é maior que o saldo, a função informará que não há saldo 
                    e o histórico não será atualizado 
                    """
                    conta_desejada.sacar(valor)

                else:
                    conta_desejada.sacar(valor)
                    h = h.atualizar(f"Sacar: {str(conta_desejada.cpf)}")

            else:
                print("Conta não encontrada.")

        elif opcao == 6:

            cpf1 = input("Você deseja transferir de qual conta? (Informe o CPF) ")
            cpf2 = input("Para qual? (Informe o cpf) ")

            conta_que_envia = encontrar_pelo_cpf(cpf1, contas)
            conta_que_recebe = encontrar_pelo_cpf(cpf2, contas)

            """
            Se ambas as contas existirem existirem, irá ser verificado se há saldo disponível para a transferência.
            
            Caso o saldo seja suficiente, será transferido e adicionado ao histórico.
            
            Caso o saldo seja insuficiente, 
            a função irá ser executada (dirá que saldo é insuficiente) e o histórico não será alterado.
            
            Se alguma delas não existir, informará um erro no CPF
            """

            if conta_que_envia and conta_que_recebe:

                valor = int(input("Qual é o valor que você deseja transferir? "))

                if valor > conta_que_envia.saldo:

                    conta_que_envia.transferir(conta_que_recebe, valor)
                    """
                    como nesse caso o saldo é insuficiente, a função apenas irá printar que o saldo não é suficiente
                    """

                else:
                    conta_que_envia.transferir(conta_que_recebe, valor)
                    h = h.atualizar(f"Transferência: {str(conta_que_envia.cpf)} -> {str(conta_que_recebe.cpf)}")

            else:
                print("Erro ao passar o CPF das contas.")

        elif opcao == 7:

            h.imprimir()

    for i in clientes:

        i.gravar_arq()

    for i in contas:

        i.gravar_arq()

    h.gravar_arq()


menu()
