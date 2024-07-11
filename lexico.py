import ply.lex as lex

tokens = (
    'PRINT',
    'STRING',
)

t_PRINT = r'imprimir'
t_STRING = r'"[^"]*"'

t_ignore = ' \t'


def t_error(t):
    print(f'Caracter ilegal: {t.value[0]}')
    t.lexer.skip(1)


lexer = lex.lex()


class AnalizadorLexico:

    @staticmethod
    def tokenize(source_code):
        _tokens = []
        lexer.input(source_code)
        while True:
            tok = lexer.token()
            if not tok:
                break
            _tokens.append(tok)
        return _tokens
