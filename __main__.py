from utils.exec import _execute
from utils.lexer import *

lex = Lexer()
while True:
    inp = input('> ')
    _execute(lex.lex_line(inp),inp)
