import mysql.connector

class Conexao():
    def __init__(self, host, user, password, database):
        self.conexao = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conexao.cursor()

    def inserir(self, sql):
        self.cursor.execute(sql)
        self.conexao.commit()

    def consultar(self, sql):
        self.cursor.execute(sql)
        retorno = self.cursor.fetchall()
        return retorno

    def fechar(self):
        self.conexao.close()





