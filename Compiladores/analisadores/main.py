from lexical import run_lexer
from syntactic import run_parser
from utils import print_result

if __name__ == "__main__":

    # Captura código fonte
    source = ""
    with open("source.txt", "r") as file:
        source = file.read()
    if source == "":
        print("Código fonte vazio!")
        exit()
    else:
        print_result(f"Código fonte a ser analisado:", 3, source)

    # Executa análise léxica
    result_lex = run_lexer(source)
    print_result("Resultados da análise léxica:", 3, result_lex.get("result"), "Nenhum token válido")
    print_result("Erros da análise léxica:", 3, result_lex.get("errors"), "Todos os tokens são válidos")

    # Executa análise sintática
    result_parse = run_parser(source)
    print_result("Resultados da análise sintática:", 3, result_parse.get("result"), "Consulte arquivos de sáida")
    print_result("Erros da análise sintática:", 3, result_parse.get("errors"), "Nenhum erro sintático encontrado")
