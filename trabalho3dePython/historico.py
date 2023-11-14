from datetime import date


class Historico:
    def __init__(self):

        """
        datas_movimento: será um array onde as chaves serão as operações (ex: Depósito: {conta.cpf})
        e a data em que foi executada a ação
        """

        self.datas_movimento = []

    def atualizar(self, movimento):

        self.datas_movimento.append(str(movimento) + "/ Data: " + str(date.today()))

    def gravar_arq(self):

        for i in self.datas_movimento:

            with open("Historico.txt", "w") as arquivo:

                arquivo.write(i + "\n")

    def imprimir(self):

        for i in self.datas_movimento:

            print(i)
