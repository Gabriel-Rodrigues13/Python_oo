class Conta:
    def __init__(self,numero, titular, saldo, limite  ):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo da conta é de: {}".format(self.saldo))
    def deposita(self, valor):
        self.saldo += valor
        print("Valor de {} depositado com sucesso".format(valor))
    def saca(self, valor):
        if (valor > self.saldo):
            print("Saldo insuficiente na conta")
        else:
            self.saldo -= valor
            print("Valor de {} sacado com sucesso".format(valor))