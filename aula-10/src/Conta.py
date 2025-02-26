"""
Definindo a classe Conta
"""


class Conta:
    __saldo: int = 0

    def depositar(self, valor: float):
        if valor > 0:
            self.__saldo += valor

    def get_saldo(self):
        return self.__saldo


"""
Utilizando a classe Conta
"""
conta = Conta()
print(conta)
print(conta.get_saldo())
conta.depositar(5000)
conta.depositar(2500)
print(conta.get_saldo())
# print(conta.saldo)
