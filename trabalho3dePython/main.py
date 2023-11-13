from cliente import Cliente

def menu():

    opcao = 0
    clientes = []

    while opcao != -1:
        print("\n|==================================================|\n"
              "|        BEM-VINDO, O QUE VOCÊ DESEJA FAZER?       |\n"
              "|==================================================|\n"
              "| 1 - Adicionar cliente                            |\n"
              "| 2 - Passar informações de um cliente pra .txt    |\n"
              "| 3 - Imprimir informações de um cliente           |\n"
              "| 4 - Criar conta para um cliente                  |\n"
              "| 5 - Passar informações de uma conta pra .txt     |\n"
              "| 6 - Imprimir informações de uma conta            |\n"
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

        elif opcao == 2:

            cpf = input("Qual será o CPF do cliente que você deseja escrever em .txt? ")
            encontrou = False

            for i in clientes:

                if i.cpf == cpf:
                    i.gravar_arq()
                    encontrou = True

            if encontrou:
                print("Os dados foram escritos!")
            else:
                print("Cliente não encontrado.")

        elif opcao == 3:

            pass

        elif opcao == 4:

            pass

        elif opcao == 5:

            pass

        elif opcao == 6:

            pass

