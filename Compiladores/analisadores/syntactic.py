from ply import yacc
from lexical import *

parse_errors = []

def p_statements(p):
    '''
    statements : statements statement
            | statement
    '''

def p_statement(p):
    '''
    statement : comment
            | declaration
            | assignment
            | decision
            | expression
            | operation
            | conditional
            | value
    '''

def p_decision(p):
    '''
    decision : IF OP_EXPR_OPEN_PARENTHESIS conditional OP_EXPR_CLOSE_PARENTHESIS OP_EXEC_COLON statement
            | IF OP_EXPR_OPEN_PARENTHESIS conditional OP_EXPR_CLOSE_PARENTHESIS OP_EXEC_COLON statement ELSE OP_EXEC_COLON statement
    '''

def p_expression(p):
    '''
    expression : OP_EXPR_OPEN_PARENTHESIS conditional OP_EXPR_CLOSE_PARENTHESIS
            | OP_EXPR_OPEN_PARENTHESIS operation OP_EXPR_CLOSE_PARENTHESIS
            | OP_EXPR_OPEN_PARENTHESIS value OP_EXPR_CLOSE_PARENTHESIS
    '''

def p_assignment(p):
    '''
    assignment : INT VARIABLE OP_ATRI_EQUAL NUMERIC EOB
            | DOUBLE VARIABLE OP_ATRI_EQUAL NUMERIC EOB
            | BOOL VARIABLE OP_ATRI_EQUAL BOOLEAN EOB
            | CHAR VARIABLE OP_ATRI_EQUAL CHAR EOB
            | STRING VARIABLE OP_ATRI_EQUAL LITERAL EOB

            | INT VARIABLE OP_ATRI_EQUAL VARIABLE EOB
            | DOUBLE VARIABLE OP_ATRI_EQUAL VARIABLE EOB
            | BOOL VARIABLE OP_ATRI_EQUAL VARIABLE EOB
            | CHAR VARIABLE OP_ATRI_EQUAL VARIABLE EOB
            | STRING VARIABLE OP_ATRI_EQUAL VARIABLE EOB

            | INT VARIABLE OP_ATRI_EQUAL operation EOB
            | DOUBLE VARIABLE OP_ATRI_EQUAL operation EOB

            | VARIABLE OP_ATRI_EQUAL NUMERIC EOB
            | VARIABLE OP_ATRI_EQUAL BOOLEAN EOB
            | VARIABLE OP_ATRI_EQUAL CHARACTER EOB
            | VARIABLE OP_ATRI_EQUAL LITERAL EOB
            | VARIABLE OP_ATRI_EQUAL VARIABLE EOB
    '''

def p_comment(p):
    '''
    comment : OP_MARK_COMMENT
    '''

def p_declaration(p):
    '''
    declaration : INT VARIABLE EOB
            | DOUBLE VARIABLE EOB
            | BOOL VARIABLE EOB
            | CHAR VARIABLE EOB
            | STRING VARIABLE EOB
    '''

def p_operation(p):
    '''
    operation : VARIABLE OP_MATE_PLUS VARIABLE
            | VARIABLE OP_MATE_MINUS VARIABLE
            | VARIABLE OP_MATE_TIMES VARIABLE
            | VARIABLE OP_MATE_DIVISION VARIABLE
            | VARIABLE OP_MATE_MODULE VARIABLE
    '''

def p_conditional(p):
    '''
    conditional : VARIABLE OP_RELA_LESS NUMERIC
            | VARIABLE OP_RELA_LESS BOOLEAN
            | VARIABLE OP_RELA_LESS LITERAL
            | VARIABLE OP_RELA_LESS CHARACTER
            | VARIABLE OP_RELA_LESS VARIABLE

            | VARIABLE OP_RELA_BIGGER NUMERIC
            | VARIABLE OP_RELA_BIGGER BOOLEAN
            | VARIABLE OP_RELA_BIGGER LITERAL
            | VARIABLE OP_RELA_BIGGER CHARACTER
            | VARIABLE OP_RELA_BIGGER VARIABLE

            | VARIABLE OP_RELA_LESS_EQUAL NUMERIC
            | VARIABLE OP_RELA_LESS_EQUAL BOOLEAN
            | VARIABLE OP_RELA_LESS_EQUAL LITERAL
            | VARIABLE OP_RELA_LESS_EQUAL CHARACTER
            | VARIABLE OP_RELA_LESS_EQUAL VARIABLE

            | VARIABLE OP_RELA_BIGGER_EQUAL NUMERIC
            | VARIABLE OP_RELA_BIGGER_EQUAL BOOLEAN
            | VARIABLE OP_RELA_BIGGER_EQUAL LITERAL
            | VARIABLE OP_RELA_BIGGER_EQUAL CHARACTER
            | VARIABLE OP_RELA_BIGGER_EQUAL VARIABLE

            | VARIABLE OP_RELA_COMPARE NUMERIC
            | VARIABLE OP_RELA_COMPARE BOOLEAN
            | VARIABLE OP_RELA_COMPARE LITERAL
            | VARIABLE OP_RELA_COMPARE CHARACTER
            | VARIABLE OP_RELA_COMPARE VARIABLE

            | VARIABLE OP_RELA_DIFFERENTIATE NUMERIC
            | VARIABLE OP_RELA_DIFFERENTIATE BOOLEAN
            | VARIABLE OP_RELA_DIFFERENTIATE LITERAL
            | VARIABLE OP_RELA_DIFFERENTIATE CHARACTER
            | VARIABLE OP_RELA_DIFFERENTIATE VARIABLE
    '''

def p_value(p):
    '''
    value : CHARACTER
            | LITERAL
            | NUMERIC
            | BOOLEAN
    '''


def p_error(p):
    parse_errors.append(p)

def run_parser(source) -> dict:
    parser = yacc.yacc()
    parsed = parser.parse(source)
    return {
        "result": parsed,
        "errors": parse_errors
    }
