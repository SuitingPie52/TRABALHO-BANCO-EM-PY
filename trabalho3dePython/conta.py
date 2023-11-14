class Conta:

    def __init__(self, cpf, numero, saldo):

        """
        cpf: será uma foreign key (FK) de cliente
        deposito: a quantidade total que já foi depositada nessa conta
        saque: a quantidade total que já foi sacada nessa conta
        """

        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
        self.deposito = 0
        self.saque = 0

    def gravar_arq(self):
        with open("Contas.txt", "a") as arquivo:
            arquivo.write(f"CPF: {self.cpf}/ Número: {self.numero}/ Saldo: {self.saldo}/ Depositado: {self.deposito}/ "
                          f"Sacado: {self.saque}\n\n")

    def depositar(self, valor):

        self.deposito += valor
        self.saldo += valor

    def sacar(self, valor):

        if valor > self.saldo:

            print("Não há saldo suficiente para saque.\n")

        else:
            self.saque += valor
            self.saldo -= valor

    def transferir(self, outra_conta, valor):

        """
        outra conta: valor da conta onde sera depositado a variável valor
        esse valor será descontado do saldo da conta self
        caso o valor sacado for maior que o saldo, não será possível executar a operação
        """

        if valor > self.saldo:

            print("Não há saldo suficiente para a transferência.\n")

        else:

            self.saque += valor
            self.saldo -= valor
            outra_conta.saldo += valor
            outra_conta.deposito += valor

    def imprimir(self):

        print(f"CPF: {self.cpf}/ Número: {self.numero}/ Saldo: {self.saldo}/ Depositado: {self.deposito}/ "
              f"Sacado: {self.saque}\n")