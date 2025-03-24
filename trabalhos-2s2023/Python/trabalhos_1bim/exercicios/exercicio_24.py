class ContaBancaria:
    def __init__(self, titular, saldo = 0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficinte.")

conta1 = ContaBancaria("João", 1000)
print(f"Saldo inicial de {conta1.titular}: {conta1.saldo}")
conta1.depositar(500)
print(f"Novo saldo após depósito: {conta1.saldo}")
conta1.sacar(300)
print(f"Novo saldo após saque: {conta1.saldo}")