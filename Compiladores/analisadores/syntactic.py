from ply import yacc
from ply.yacc import LRParser
from lexical import *

parse_errors = []

def p_statements_multiple(p):
    '''
    statements : statements statement
    '''

def p_statements_single(p):
    '''
    statements : statement
    '''

def p_statement_comment(p):
    '''
    statement : OP_MARK_COMMENT
    '''

def p_statement_assignment(p):
    '''
    statement : VARIABLE OP_ATRI_EQUAL INT EOB
            | VARIABLE OP_ATRI_EQUAL TRUE EOB
            | VARIABLE OP_ATRI_EQUAL FALSE EOB
            | VARIABLE OP_ATRI_EQUAL expression EOB
    '''

def p_statement_conditional(p):
    '''
    statement : IF OP_EXPR_OPEN_PARENTHESIS conditional OP_EXPR_CLOSE_PARENTHESIS OP_EXEC_COLON statements
            | IF OP_EXPR_OPEN_PARENTHESIS conditional OP_EXPR_CLOSE_PARENTHESIS OP_EXEC_COLON statements ELSE OP_EXEC_COLON statements
    '''

def p_expression_operation(p):
    '''
    expression : VARIABLE OP_MATE_PLUS VARIABLE
            | VARIABLE OP_MATE_MINUS VARIABLE
            | VARIABLE OP_MATE_TIMES VARIABLE
            | VARIABLE OP_MATE_DIVISION VARIABLE
            | VARIABLE OP_MATE_MODULE VARIABLE
    '''

def p_conditional(p):
    '''
    conditional : VARIABLE OP_RELA_COMPARE INT
    '''

def p_expression_group(p):
    '''
    expression : OP_EXPR_OPEN_PARENTHESIS expression OP_EXPR_CLOSE_PARENTHESIS
    '''

def p_expression_number(p):
    '''
    expression : INT
            | DOUBLE
    '''

def p_expression_bool(p):
    '''
    expression : TRUE
            | FALSE
    '''

def p_error(p):
    parse_errors.append(p)

def run_parser(source):
    parser = yacc.yacc()
    result = parser.parse(source)

    print(result)

    return parse_errors
