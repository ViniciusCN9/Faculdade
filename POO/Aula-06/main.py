import csv
import conexao as cn
import util

conexao = cn.Conexao('localhost', 'root', 'root', 'empresa')

with open('clientes.csv') as arquivo:
    dados = csv.reader(arquivo, delimiter=';')

    contador = 0
    for linha in dados:
        conexao.inserir(f"INSERT INTO clientes VALUES ('{linha[0]}','{linha[1]}', '{linha[2]}', '{linha[3]}', '{util.ajusteData(linha[4])}')")
        contador += 1
        
    print({f'{contador} linhas processadas.'})

conexao.fechar()

