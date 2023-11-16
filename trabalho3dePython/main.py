from trabalho3dePython.cliente import Cliente
from trabalho3dePython.conta import Conta
from trabalho3dePython.historico import Historico


def imprimir_todos_conjunto(conjunto_classes):
    for i in conjunto_classes:
        i.imprimir()


def encontrar_pelo_cpf(cpf, conjunto_classes):

    for i in conjunto_classes:

        if i.cpf == cpf:
            return i

    return None


def menu():

    opcao = 0
    clientes = []
    contas = []
    h = Historico()

    while opcao != -1:
        print("\n|==================================================|\n"
              "|        BEM-VINDO, O QUE VOCÊ DESEJA FAZER?       |\n"
              "|==================================================|\n"
              "| 1 - Adicionar cliente                            |\n"
              "| 2 - Passar informações de um cliente pra .txt    |\n"
              "| 3 - Imprimir informações de todos os clientes    |\n"
              "| 4 - Criar conta para um cliente                  |\n"
              "| 5 - Passar informações de uma conta pra .txt     |\n"
              "| 6 - Imprimir informações de todas as contas      |\n"
              "| 7 - Depositar na conta                           |\n"
              "| 8 - Sacar da conta                               |\n"
              "| 9 - Transferir de uma conta para outra           |\n"
              "| 10 - Passar informações do histórico para .txt   |\n"
              "| 11 - Imprimir histórico                          |\n"
              "|==================================================|\n"
              "| -1 - Encerrar programa                           |\n"
              "|==================================================|\n\n")

        opcao = int(input("Qual comando você deseja executar? "))

        if opcao == 1:

            cpf = input("Qual será o CPF desse cliente? ")
            nome = input("Qual será o nome desse cliente? ")

            clientes.append(Cliente(cpf, nome))
            print("Cliente adicionado!")

        elif opcao == 2:

            cpf = input("Qual será o CPF do cliente que você deseja escrever em .txt? ")

            cliente_desejado = encontrar_pelo_cpf(cpf, clientes)

            if cliente_desejado:
                cliente_desejado.gravar_arq()
                print("Os dados foram escritos!")
            else:
                print("Cliente não encontrado.")

        elif opcao == 3:

            imprimir_todos_conjunto(clientes)

        elif opcao == 4:

            cpf = input("Você deseja abrir uma conta para qual cliente? (Informe o CPF dele) ")
            numero_conta = input("Qual será o número de identificação dessa conta? ")
            saldo = int(input("Qual será o saldo inicial dessa conta? "))

            contas.append(Conta(cpf, numero_conta, saldo))
            print("Conta adicionado!")

        elif opcao == 5:

            cpf = input("Qual é o CPF identificador dessa conta que você deseja escrever em .txt? ")

            conta_desejada = encontrar_pelo_cpf(cpf, contas)

            if conta_desejada:
                conta_desejada.gravar_arq()
                print("Os dados foram escritos!")

            else:
                print("Conta não encontrada.")

        elif opcao == 6:

            imprimir_todos_conjunto(contas)

        elif opcao == 7:

            cpf = input("Qual é o CPF identificador da conta em que você deseja depositar? ")
            valor = int(input("Qual é o valor que você deseja depositar? "))

            conta_desejada = encontrar_pelo_cpf(cpf, contas)

            if conta_desejada:
                conta_desejada.depositar(valor)
                h = h.atualizar(f"Depósito: {str(conta_desejada.cpf)}")
                print("Valor depositado!")

            else:
                print("Conta não encontrada.")

        elif opcao == 8:

            cpf = input("Qual é o CPF identificador da conta em que você quer sacar? ")
            valor = int(input("Qual é o valor que você deseja sacar? "))

            """
            Não funciona com valores muito altos.
            """

            conta_desejada = encontrar_pelo_cpf(cpf, contas)

            if conta_desejada:
                conta_desejada.sacar(valor)
                h = h.atualizar(f"Sacar: {str(conta_desejada.cpf)}")

            else:
                print("Conta não encontrada.")

        elif opcao == 9:

            cpf1 = input("Você deseja transferir de qual conta? (Informe o CPF) ")
            cpf2 = input("Para qual? (Informe o cpf) ")

            conta_que_envia = encontrar_pelo_cpf(cpf1, contas)
            conta_que_recebe = encontrar_pelo_cpf(cpf2, contas)

            valor = int(input("Qual é o valor que você deseja transferir? "))

            if conta_que_envia and conta_que_recebe:
                conta_que_envia.transferir(conta_que_recebe, valor)
                h = h.atualizar(f"Transferência: {str(conta_que_envia.cpf)} -> {str(conta_que_recebe.cpf)}")

            else:
                print("Erro ao passar o CPF das contas.")

        elif opcao == 10:
            h.gravar_arq()
            print("Os dados foram gravados!")

        elif opcao == 11:
            h.imprimir()


menu()
