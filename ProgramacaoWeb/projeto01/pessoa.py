from cgitb import text
from email import contentmanager


class pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar(self, texto):
        conteudo = (f'{self.nome} {self.sobrenome} disse: {texto}')
        return conteudo

    
