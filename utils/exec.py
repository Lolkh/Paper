# exec.py
from utils.lexer import TOKENS

class PaperError:
    def __init__(self, message, errtype):
        self.message = message
        self.errtype = errtype
        print(self.errtype+': '+self.message)

def make_string(data):
    string = ''
    try:
        return data.split(r'"')[1]
    except IndexError:
        try:
            return data.split(r"'")[1]
        except IndexError:
            PaperError('String error', 'PaperError')

def _execute(lex_data, orig_string):
    for token in lex_data:
        if token['token'] == 'type':
            try:
                stuff_to_type = make_string(orig_string.split(token['token'])[1])
                if stuff_to_type == '' or stuff_to_type == None:
                    pass
                else:
                    print(stuff_to_type)
            except IndexError:
                PaperError('No string to type', 'PaperError')
        elif token['token'] == 'quit':
            print('Exitting paper ...')
            exit()
