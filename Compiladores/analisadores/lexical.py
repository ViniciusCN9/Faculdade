from ply import lex

lex_errors = []

reserved = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
    "int": "INT",
    "double": "DOUBLE",
    "string": "STRING",
    "char": "CHAR",
    "bool": "BOOL"
}

tokens = [
    "OP_MATE_PLUS",
    "OP_MATE_MINUS",
    "OP_MATE_TIMES",
    "OP_MATE_DIVISION",
    "OP_MATE_MODULE",
    
    "OP_EXEC_COLON",
    "OP_EXEC_COMMA",
    "OP_EXEC_DOT",
    
    "OP_MARK_SQUOTES",
    "OP_MARK_DQUOTES",
    "OP_MARK_COMMENT",
    
    "OP_ATRI_DENIAL",
    "OP_ATRI_EQUAL",
    "OP_ATRI_PLUS_EQUAL",
    "OP_ATRI_MINUS_EQUAL",
    "OP_ATRI_TIMES_EQUAL",
    "OP_ATRI_DIVISION_EQUAL",
    
    "OP_RELA_LESS",
    "OP_RELA_BIGGER",
    "OP_RELA_LESS_EQUAL",
    "OP_RELA_BIGGER_EQUAL",
    "OP_RELA_COMPARE",
    "OP_RELA_DIFFERENTIATE",
    
    "OP_LOGI_AND",
    "OP_LOGI_OR",
    
    "OP_EXPR_OPEN_PARENTHESIS",
    "OP_EXPR_CLOSE_PARENTHESIS",
    "OP_EXPR_OPEN_BRACKETS",
    "OP_EXPR_CLOSE_BRACKETS",
    "OP_EXPR_OPEN_CURLY_BRACKETS",
    "OP_EXPR_CLOSE_CURLY_BRACKETS",
    
    "EOB",
    "CHARACTER",
    "LITERAL",
    "NUMERIC",
    "BOOLEAN",
    "VARIABLE"
] + list(reserved.values())

t_OP_MATE_PLUS = r'\+'
t_OP_MATE_MINUS = r'-'
t_OP_MATE_TIMES = r'\*'
t_OP_MATE_DIVISION = r'/'
t_OP_MATE_MODULE = r'\%'

t_OP_EXEC_COLON = r'\:'
t_OP_EXEC_COMMA = r'\,'
t_OP_EXEC_DOT = r'\.'

t_OP_MARK_SQUOTES = r'\''
t_OP_MARK_DQUOTES = r'\"'
t_OP_MARK_COMMENT = r'\#.*'

t_OP_ATRI_DENIAL = r'\~'
t_OP_ATRI_EQUAL = r'\='
t_OP_ATRI_PLUS_EQUAL = r'\+\='
t_OP_ATRI_MINUS_EQUAL = r'\-\='
t_OP_ATRI_TIMES_EQUAL = r'\*\='
t_OP_ATRI_DIVISION_EQUAL = r'\/\='

t_OP_RELA_LESS = r'\<'
t_OP_RELA_BIGGER = r'\>'
t_OP_RELA_LESS_EQUAL = r'\<\='
t_OP_RELA_BIGGER_EQUAL = r'\>\='
t_OP_RELA_COMPARE = r'\=\='
t_OP_RELA_DIFFERENTIATE = r'\!\='

t_OP_LOGI_AND = r'\&\&'
t_OP_LOGI_OR = r'\|\|'

t_OP_EXPR_OPEN_PARENTHESIS = r'\('
t_OP_EXPR_CLOSE_PARENTHESIS = r'\)'
t_OP_EXPR_OPEN_BRACKETS = r'\['
t_OP_EXPR_CLOSE_BRACKETS = r'\]'
t_OP_EXPR_OPEN_CURLY_BRACKETS = r'\{'
t_OP_EXPR_CLOSE_CURLY_BRACKETS = r'\}'

t_ignore = " \t"

def t_CHARACTER(t):
    r'("[a-z_A-Z_0-9]")'
    return t

def t_LITERAL(t):
    r'("[^"]*")'
    return t

def t_NUMERIC(t):
    r'\d+'
    return t
    
def t_BOOLEAN(t):
    r'(true|false)'
    return t

def t_VARIABLE(t): # Se não for reservada é variável
    r'([a-z_A-Z][a-z_A-Z]*)'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_EOB(t):
    r'\;'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    lex_errors.append(t)
    t.lexer.skip(1)

def run_lexer(source):
    lexer = lex.lex()
    lexer.input(source)

    for tok in lexer:
        print(tok)
    
    return lex_errors