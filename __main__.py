from utils.lexer import *

lex = Lexer()
while True:
    print(lex.lex_line(input('> ')))
