from pessoa import pessoa

class funcionario(pessoa):
    def __init__(self, nome, sobrenome, emprego, salario):
        super().__init__(nome, sobrenome)
        self.emprego = emprego
        self.salario = float(salario)

    def exibir(self):
        conteudo = f'{self.nome} {self.sobrenome} é {self.emprego} e ganha R$ %.2f' % (self.salario)
        print(conteudo)
