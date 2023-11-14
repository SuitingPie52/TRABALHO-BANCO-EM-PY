class Cliente:

    def __init__(self, cpf, nome):

        self.cpf = cpf
        self.nome = nome

    def gravar_arq(self):

        with open("Clientes.txt", "a") as arquivo:

            arquivo.write(f"CPF: {self.cpf}/ Nome: {self.nome}\n")

    def imprimir(self):

        print(f"CPF: {self.cpf}/ Nome: {self.nome}")
