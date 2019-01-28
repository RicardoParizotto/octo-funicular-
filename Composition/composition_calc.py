# -----------------------------------------------------------------------------
#
# A simple calculator of composition with variables.  
# This is based from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, "../ply-3.11/")

from p4module import load_p4module

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME', 'NUMBER',
)

literals = ['+', '>', '(', ')']

# Tokens

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '>' expression'''

    if p[2] == '+':
        p[0] = parallel_composition(p[1],p[3])
    elif p[2] == '-':
        p[0] = sequential_composition(p[1],p[3])