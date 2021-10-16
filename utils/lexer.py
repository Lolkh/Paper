# Lexer.py

KNOWN_TOKES = [
    # Numbers
    {"token":"1","ID":"NUMBER_1"},
    {"token":"2","ID":"NUMBER_2"},
    {"token":"3","ID":"NUMBER_3"},
    {"token":"4","ID":"NUMBER_4"},
    {"token":"5","ID":"NUMBER_5"},
    {"token":"6","ID":"NUMBER_6"},
    {"token":"7","ID":"NUMBER_7"},
    {"token":"8","ID":"NUMBER_8"},
    {"token":"9","ID":"NUMBER_9"},
    {"token":"0","ID":"NUMBER_0"},
    # Letters: Capital
    {"token":"Q","ID":"LETTER_Q"},
    {"token":"W","ID":"LETTER_W"},
    {"token":"E","ID":"LETTER_E"},
    {"token":"R","ID":"LETTER_R"},
    {"token":"T","ID":"LETTER_T"},
    {"token":"Y","ID":"LETTER_Y"},
    {"token":"U","ID":"LETTER_U"},
    {"token":"I","ID":"LETTER_I"},
    {"token":"O","ID":"LETTER_O"},
    {"token":"P","ID":"LETTER_P"},
    {"token":"A","ID":"LETTER_A"},
    {"token":"S","ID":"LETTER_S"},
    {"token":"D","ID":"LETTER_D"},
    {"token":"F","ID":"LETTER_F"},
    {"token":"G","ID":"LETTER_G"},
    {"token":"H","ID":"LETTER_H"},
    {"token":"J","ID":"LETTER_J"},
    {"token":"K","ID":"LETTER_K"},
    {"token":"L","ID":"LETTER_L"},
    {"token":"Z","ID":"LETTER_Z"},
    {"token":"X","ID":"LETTER_X"},
    {"token":"C","ID":"LETTER_C"},
    {"token":"V","ID":"LETTER_V"},
    {"token":"B","ID":"LETTER_B"},
    {"token":"N","ID":"LETTER_N"},
    {"token":"M","ID":"LETTER_M"},
    # Letters: Lower
    {"token":"q","ID":"LETTER_q"},
    {"token":"w","ID":"LETTER_w"},
    {"token":"e","ID":"LETTER_e"},
    {"token":"r","ID":"LETTER_r"},
    {"token":"t","ID":"LETTER_t"},
    {"token":"y","ID":"LETTER_y"},
    {"token":"u","ID":"LETTER_u"},
    {"token":"i","ID":"LETTER_i"},
    {"token":"o","ID":"LETTER_o"},
    {"token":"p","ID":"LETTER_p"},
    {"token":"a","ID":"LETTER_a"},
    {"token":"s","ID":"LETTER_s"},
    {"token":"d","ID":"LETTER_d"},
    {"token":"f","ID":"LETTER_f"},
    {"token":"g","ID":"LETTER_g"},
    {"token":"h","ID":"LETTER_h"},
    {"token":"j","ID":"LETTER_j"},
    {"token":"k","ID":"LETTER_k"},
    {"token":"l","ID":"LETTER_l"},
    {"token":"z","ID":"LETTER_z"},
    {"token":"x","ID":"LETTER_x"},
    {"token":"c","ID":"LETTER_c"},
    {"token":"v","ID":"LETTER_v"},
    {"token":"b","ID":"LETTER_b"},
    {"token":"n","ID":"LETTER_n"},
    {"token":"m","ID":"LETTER_m"},
    # Symbols
    {"token":"!","ID":"SYMBOL_EXC"},
    {"token":"@","ID":"SYMBOL_AT"},
    {"token":"#","ID":"SYMBOL_HASH"},
    {"token":"$","ID":"SYMBOL_DOLLAR"},
    {"token":"%","ID":"SYMBOL_PERC"},
    {"token":"^","ID":"SYMBOL_EXP"},
    {"token":"*","ID":"SYMBOL_AST"},
    {"token":"(","ID":"SYMBOL_PAREN_OPEN"},
    {"token":")","ID":"SYMBOL_PAREN_CLOSE"},
    {"token":"[","ID":"SYMBOL_SQUARE_OPEN"},
    {"token":"]","ID":"SYMBOL_SQUARE_CLOSE"},
    {"token":"{","ID":"SYMBOL_CURL_OPEN"},
    {"token":"}","ID":"SYMBOL_CURL_CLOSE"},
    {"token":"\"","ID":"SYMBOL_DOUBLE_QUOTE"},
    {"token":"\'","ID":"SYMBOL_SINGLE_QUOTE"},
    {"token":"<","ID":"SYMBOL_ANGLE_OPEN"},
    {"token":">","ID":"SYMBOL_ANGLE_CLOSE"},
    {"token":"\\","ID":"SYMBOL_BACKSLASH"},
    {"token":"/","ID":"SYMBOL_FORWARDSKASH"},
    {"token":"+","ID":"SYMBOL_PLUS"},
    {"token":"-","ID":"SYMBOL_MINUS"},
    {"token":".","ID":"SYMBOL_DOT"},
    {"token":",","ID":"SYMBOL_COMMA"},
    {"token":"?","ID":"SYMBOL_QUESTION"},
    {"token":"|","ID":"SYMBOL_PIPE"},
    {"token":"=","ID":"SYMBOL_EQUALS"},
    {"token":"-","ID":"SYMBOL_MINUS"},
    {"token":"_","ID":"SYMBOL_UNDERSCORE"},
]

def find_symbol(symbol):
    for i in KNOWN_TOKES:
        if i["token"] == symbol:
            return i

# CENTURY!

class Lexer:
    def __init__(self):
        self.VERSION = "v0.0.1"

    def lex_line(self,line):
        for i in line:
            symbol = find_symbol(i)
