import	datetime

class Historico:
    def	__init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes	= []
        
    def	imprime(self):
        print(f"data abertura: {self.data_abertura}")
        print("transações: ")
        for	t in self.transacoes:
            print("-", t)

class Cliente:
    def	__init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def	__init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero	= numero
        self.titular = cliente
        self.saldo = saldo
        self.limite	= limite
        self.historico = Historico()

    def	depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"depósito de R${valor}")

    def	sacar(self, valor):
        if (self.saldo < valor):
            return False

        self.saldo -= valor
        self.historico.transacoes.append(f"saque de R${valor}")
        return True

    def	tirarExtrato(self):
        print(f"numero: {self.numero}\nsaldo: {self.saldo}")
        self.historico.transacoes.append(f"tirou extrato - saldo de {self.saldo}")

    def	transferir(self, destino, valor):
        retirou	= self.sacar(valor)
        if not retirou:
            return False

        destino.depositar(valor)
        self.historico.transacoes.append(f"transfêrencia de {valor} para conta {destino.numero}")
        return True

cliente1 = Cliente('João', 'Oliveira', '11111111111-11')
cliente2 = Cliente('José', 'Azevedo', '222222222-22')
conta1 = Conta('123-4',	cliente1, 1000.0)
conta2 = Conta('123-5',	cliente2, 1000.0)
conta1.depositar(100.0)
conta1.sacar(50.0)
conta1.transferir(conta2, 200.0)
conta1.tirarExtrato()
#numero:	123-4	
#saldo:	850.0
conta1.historico.imprime()
#data	abertura:	2018-05-10	19:44:07.406533
#transações:	
#-	depósito	de	100.0
#-	saque	de	50.0
#-	saque	de	200.0
#-	transferencia	de	200.0	para	conta	123-5
#-	tirou	extrato	-	saldo	de	850.0
conta2.historico.imprime()
#data	abertura:	2018-05-10	19:44:07.406553
#transações:	
#-	depósito	de	200.0