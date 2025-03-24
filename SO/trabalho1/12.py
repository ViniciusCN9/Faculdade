with open("meuarquivo.txt", "r") as original_file:
    conteudo = original_file.read()

    with open("copia_meuarquivo.txt", "w") as copia_file:
        copia_file.write(conteudo)

print("Arquivo copiado com sucesso!")
