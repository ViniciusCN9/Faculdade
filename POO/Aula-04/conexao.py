import mysql.connector

class Conexao():
    def __init__(self, host, user, password, database):
        self.conexao = mysql.connector.connect(host=host, user=user, password=password, database=database)
        self.cursor = self.conexao.cursor()
        
    def executar(self, sql):
        self.cursor.execute(sql)

    def inserir(self, sql, valores):
        self.cursor.execute(sql, valores)
        self.conexao.commit()

    def consultar(self, sql):
        self.cursor.execute(sql)
        retorno = self.cursor.fetchall()
        return retorno

    def fechar(self):
        self.conexao.close()





