class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo da conta é de: {}".format(self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        print("Valor de {} depositado com sucesso".format(valor))

    def saca(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente na conta")
            return False
        else:
            self.__saldo -= valor
            print("Valor de {} sacado com sucesso".format(valor))
            return True

    def tranfere(self,valor, destino):
        if self.saca(valor):
            destino.deposita(valor)

