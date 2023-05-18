from lexical import run_lexer
from syntactic import run_parser

if __name__ == "__main__":

    # Captura código fonte
    source = ""
    with open("source.txt", "r") as file:
        source = file.read()
    if source == "":
        print("Código fonte vazio!")
        exit()
    else:
        print(f"Código fonte a ser analisado:\n{source}\n")

    # Executa análise léxica
    result_lex = run_lexer(source)
    print(result_lex)

    # Executa análise sintática
    result_parse = run_parser(source)
    print(result_parse)

