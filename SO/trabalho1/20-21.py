import struct
from faker import Faker


TAMANHO_REGISTRO = 78
FORMATO = "16s30s2s30s"


def adicionar_registro(arquivo, id, nome, idade, cidade):
    try:
        # Verificar se os dados têm o tamanho esperado
        if len(str(id)) <= 16 and len(nome) <= 30 and len(str(idade)) <= 2 and len(cidade) <= 30:
            arquivo.seek(0, 2)
            registro = struct.pack(FORMATO, str(id).ljust(16).encode(), nome.ljust(
                30).encode(), str(idade).zfill(2).encode(), cidade.ljust(30).encode())
            arquivo.write(registro)
            print("Registro adicionado com sucesso.")
        else:
            print("Os dados não correspondem ao formato esperado.")
    except Exception as e:
        print("Erro ao adicionar o registro:", e)


def listar_registros(arquivo):
    try:
        arquivo.seek(0)
        while True:
            registro = arquivo.read(TAMANHO_REGISTRO)
            if not registro:
                break
            id, nome, idade, cidade = struct.unpack(FORMATO, registro)
            print(f"ID: {id.decode().strip()}, Nome: {nome.decode().strip()}, Idade: {idade.decode().strip()}, Cidade: {cidade.decode().strip()}")
    except Exception as e:
        print("Erro ao listar os registros:", e)


def buscar_registro(arquivo, id):
    try:
        arquivo.seek(0)
        while True:
            registro = arquivo.read(TAMANHO_REGISTRO)
            if not registro:
                break
            current_id = struct.unpack(FORMATO, registro)[0].decode().strip()
            if current_id == str(id):
                registro_id, nome, idade, cidade = struct.unpack(
                    FORMATO, registro)
                print(
                    f"ID: {registro_id.decode().strip()}, Nome: {nome.decode().strip()}, Idade: {idade.decode().strip()}, Cidade: {cidade.decode().strip()}")
                return
        print("Registro não encontrado.")
    except Exception as e:
        print("Erro ao buscar o registro:", e)


def buscar_registro_binaria(arquivo, id):
    try:
        arquivo.seek(0, 2)
        tamanho_arquivo = arquivo.tell()
        total_registros = tamanho_arquivo // TAMANHO_REGISTRO

        registros = []

        arquivo.seek(0)
        for _ in range(total_registros):
            registro = arquivo.read(TAMANHO_REGISTRO)
            id_registro = int(struct.unpack(
                FORMATO, registro)[0].decode().strip())
            registros.append((id_registro, registro))

        registros.sort(key=lambda x: x[0])  # Ordenar os registros por ID

        # Busca binária
        left, right = 0, len(registros) - 1
        while left <= right:
            mid = (left + right) // 2
            current_id, current_registro = registros[mid]
            if current_id == int(id):
                registro_id, nome, idade, cidade = struct.unpack(
                    FORMATO, current_registro)
                print(
                    f"ID: {registro_id.decode().strip()}, Nome: {nome.decode().strip()}, Idade: {idade.decode().strip()}, Cidade: {cidade.decode().strip()}")
                return
            elif current_id < int(id):
                left = mid + 1
            else:
                right = mid - 1

        print("Registro não encontrado.")
    except Exception as e:
        print("Erro na busca binária:", e)


def excluir_registro(arquivo, id):
    try:
        registros = []
        arquivo.seek(0)
        while True:
            registro = arquivo.read(TAMANHO_REGISTRO)
            if not registro:
                break
            registro_id = struct.unpack(FORMATO, registro)[0].decode().strip()
            if registro_id != str(id):
                registros.append(registro)
        arquivo.seek(0)
        arquivo.truncate(0)
        for registro in registros:
            arquivo.write(registro)
        print("Registro excluído com sucesso.")
    except Exception as e:
        print("Erro ao excluir o registro:", e)


def popular_dados(arquivo):
    fake = Faker()
    for _ in range(1000):
        id = fake.unique.random_int(min=1, max=10000)
        nome = fake.name()
        idade = fake.random_int(min=18, max=99)
        cidade = fake.city()
        adicionar_registro(arquivo, id, nome, idade, cidade)
    print("Dados fictícios gerados com sucesso.")


def menu():
    opcao = 0
    with open("dados_formato.bin", "a+b") as arquivo:
        while opcao != 7:
            print("\nMenu:")
            print("1. Adicionar Registro")
            print("2. Listar Registros")
            print("3. Buscar Registro por ID")
            print("4. Buscar Registro por ID (Binária)")
            print("5. Excluir Registro por ID")
            print("6. Popular Dados")
            print("7. Sair")
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                id = input("Digite o ID: ")
                nome = input("Digite o Nome: ")
                idade = input("Digite a Idade: ")
                cidade = input("Digite a Cidade: ")
                adicionar_registro(arquivo, id, nome, idade, cidade)
            elif opcao == 2:
                listar_registros(arquivo)
            elif opcao == 3:
                id = input("Digite o ID para busca: ")
                buscar_registro(arquivo, id)
            elif opcao == 4:
                id = input("Digite o ID para busca: ")
                buscar_registro_binaria(arquivo, id)
            elif opcao == 5:
                id = input("Digite o ID para exclusão: ")
                excluir_registro(arquivo, id)
            elif opcao == 6:
                popular_dados(arquivo)
            elif opcao == 7:
                print("Encerrando o programa.")
            else:
                print("Opção inválida. Tente novamente.")


menu()
