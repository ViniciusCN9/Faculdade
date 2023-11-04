def registrar_atividade(nome_usuario, atividade, registro):
    if nome_usuario in registro:
        registro[nome_usuario].append(atividade)
    else:
        registro[nome_usuario] = [atividade]


registro_atividades = {}

registrar_atividade('Joao', 'Login realizado', registro_atividades)
registrar_atividade('Maria', 'Criado novo post', registro_atividades)
registrar_atividade('Joao', 'Feito upload de arquivo', registro_atividades)
registrar_atividade('Pedro', 'Logout realizado', registro_atividades)
registrar_atividade('Maria', 'Comentário adicionado', registro_atividades)

print(registro_atividades)
