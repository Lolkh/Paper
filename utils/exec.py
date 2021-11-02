# exec.py
from utils.lexer import TOKENS

def _execute(lex_data, orig_string):
    for token in lex_data:
        if token['token'] == 'type':
            stuff_to_type = orig_string.split('type ')[1]
            print(stuff_to_type)