from ply import lex

from lexer_config import *

if __name__ == "__main__":
    try:
        # Realiza a leitura do código fonte
        source = ""
        with open("source.txt", "r") as file:
            source = file.read()
        if source == "":
            print("Código fonte vazio!")
            exit()
        else:
            print(f"Código fonte a ser analisado:\n{source}\n")

        # Executa o analisador léxico
        lexer = lex.lex()
        lexer.input(source)
        while True:
            token = lexer.token()
            if not token:
                break
            print(token)

    except Exception as error:
        print(f"Ocorreu o seguinte erro durante a execução: {str(error)}")
        