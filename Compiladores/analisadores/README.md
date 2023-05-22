# **ANALISADOR LÉXICO E SINTÁTICO**

## **Como executar:**

- Rodar comando de instalação das dependências: **pip install -r requirements.txt**
- Executar arquivo **main.py**

## **Saídas:**

Serão exibidos no console os seguintes elementos:
- Código fonte a ser analisado, lido do arquivo **source.txt**
- Resultados e erros da análise léxica
- Resultados e erros da análise sintática

**__OBS__:** A análise sintática gera os arquivos **parser.out** e **parsetab.out** que podem ser consultados para validação da análise realizada

## **Código fonte:**

A linguagem fícticia criada para esse analisador segue algumas regras gramaticais simples, baseadas na linguagem python e c#
- Variáveis tipadas (INT, DOUBLE, CHAR, STRING, BOOL)
- Palavras reservadas (IF, ELSE, FOR, WHILE ...)
- Comentários (`#`), fim de linha (`;`) e início de sentença (`:`)
- Entre outros recursos