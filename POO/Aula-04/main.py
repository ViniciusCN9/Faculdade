from conexao import Conexao

def main():
    conexao = Conexao('localhost', 'root', 'root', 'teste')
    conexao.executar("CREATE TABLE Pessoas (Id int NOT NULL AUTO_INCREMENT, Sobrenome varchar(255), Nome varchar(255), Endereco varchar(255), Cidade varchar(255), PRIMARY KEY (Id));")

    conexao.inserir("INSERT INTO Pessoas (Sobrenome, Nome, Endereco, Cidade) VALUES (%s, %s, %s, %s)", ('Amaral', 'Tarcila', 'R.Fulano', 'São Paulo'))
    conexao.inserir("INSERT INTO Pessoas (Sobrenome, Nome, Endereco, Cidade) VALUES (%s, %s, %s, %s)", ('José', 'Gabriel', 'R.Ciclano', 'Vítoria'))
    conexao.inserir("INSERT INTO Pessoas (Sobrenome, Nome, Endereco, Cidade) VALUES (%s, %s, %s, %s)", ('Bonner', 'Willian', 'R.Beltrano', 'Rio de Janeiro'))
    conexao.inserir("INSERT INTO Pessoas (Sobrenome, Nome, Endereco, Cidade) VALUES (%s, %s, %s, %s)", ('Padilha', 'Bruno', 'R.Deltrano', 'Belo Horizonte'))

    consulta = conexao.consultar("SELECT * FROM Pessoas;")
    for dado in consulta:
        print(dado)

    conexao.executar("DROP TABLE Pessoas;")
    conexao.fechar()

main()