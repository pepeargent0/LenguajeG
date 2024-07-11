import ply.yacc as yacc
from lexico import tokens  # Asegúrate de que la lista de tokens esté definida en lexico.py

class AnalizadorSintactico:
    tokens = tokens  # Importa la lista de tokens desde lexico.py

    def p_statement_print(self, p):
        'statement : PRINT STRING'
        p[0] = ('PRINT', p[2])

    def p_error(self, p):
        print(f'Error de sintaxis: {p.value!r}')

    def __init__(self):
        self.parser = yacc.yacc(module=self)

    @staticmethod
    def parsear(token_list):
        iter_lexer = IterLexer(token_list)
        return AnalizadorSintactico().parser.parse(lexer=iter_lexer)

class IterLexer:
    def __init__(self, token_list):
        self.tokens = iter(token_list)
        self.current_token = None

    def token(self):
        try:
            self.current_token = next(self.tokens)
            return self.current_token
        except StopIteration:
            return None
