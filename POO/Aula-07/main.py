from datetime import datetime
from conexao import Conexao
import requests

CONEXAO = Conexao('localhost', 'root', 'root', 'financeiro')
DIAS = 20
MOEDA_ORIGEM = 'USD'
MOEDA_DESTINO = 'BRL'
API_URL = f'https://economia.awesomeapi.com.br/json/daily/{MOEDA_ORIGEM}-{MOEDA_DESTINO}/{DIAS}'

def main():
    cotacoes = requests.get(API_URL).json()

    #Inserir dados
    for i in cotacoes:
        CONEXAO.inserir(f"INSERT INTO cotacao VALUES ('{MOEDA_ORIGEM}', '{MOEDA_DESTINO}', {i['timestamp']}, {i['bid']})")

    #Consultar dados
    dados = CONEXAO.consultar("SELECT * FROM cotacao")
    for i in dados:
        data = datetime.fromtimestamp(int(i[2]))
        print(f"Data: {data.day}/{data.month}/{data.year} às {data.hour}:{data.minute} | {i[0]} => {i[1]} | Valor: R${i[3]}")
        
    CONEXAO.fechar()
    
main()