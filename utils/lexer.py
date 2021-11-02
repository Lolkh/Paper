# Lexer.py

TOKENS = {
    "type":{"token":"type","ID":"TOKEN_TYPE","type":"BUILTIN_FUNCTION"}
}

def find_tokens_if_any(symbols):
    output = []
    for i in symbols:
        for token in TOKENS:
            if TOKENS[token]["token"] in i:
                output.append(TOKENS[i])
    return output

class Lexer:
    def __init__(self):
        self.VERSION = "v0.0.1"

    def lex_line(self,line):
        symbols = []
        for i in line.split(" "):
            symbols.append(i)

        return find_tokens_if_any(symbols)