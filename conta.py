class Conta():
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return  self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    def extrato(self):
        print("O saldo da conta é de: {}".format(self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        print("Valor de {} depositado com sucesso".format(valor))

    def __pode_sacar(self, valor_a_sacar):
        limite_de_saque = self.__saldo + self.__limite
        return valor_a_sacar <= limite_de_saque

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print("Valor de {} sacado com sucesso".format(valor))
        else:
            print("Saldo insuficiente na conta")

    def tranfere(self,valor, destino):
        if self.saca(valor):
            destino.deposita(valor)
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237" }