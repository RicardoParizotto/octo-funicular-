# -----------------------------------------------------------------------------
#
# A simple calculator of composition with variables.  
# This is based from O'Reilly's
# "Lex and Yacc", p. 63.
# this should open the basis code
# scan the command line (sw, command)
# parse commandline
# open files
# compose
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, "../ply-3.11/")

from composition_compiler import process_commandline

if sys.version_info[0] >= 3:
    raw_input = input

cmd = process_commandline()

tokens = (
    'NAME', 'NUMBER',
)

literals = ['+', '>', '(', ')']

# Tokens
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_.]*'

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
precedence = (
    ('left', '+', '>'),
)

# dictionary of names
names = {}

def p_statement_expr(p):
    'statement : expression'
    print(p[1])


def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '>' expression'''
    print(str(p[3]))
    if p[2] == '+':
        p[0] = cmd.parallel_composition(p[1],p[3])
    elif p[2] == '-':
        p[0] = cmd.sequential_composition(p[1],p[3])


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = p[1]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('input > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)