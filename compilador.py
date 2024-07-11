import sys
from lexico import AnalizadorLexico
from sintactico import AnalizadorSintactico
from generador_asm import CodeGenerator
import os


def main(source_file):
    source_code = open(source_file).read()
    a_lexico = AnalizadorLexico()
    token_list = a_lexico.tokenize(source_code)
    a_sintactico = AnalizadorSintactico()
    ast = a_sintactico.parsear(token_list)
    codegen = CodeGenerator(ast)
    asm_code = codegen.generate()
    with open('output.asm', 'w') as f:
        f.write(asm_code)
    os.system('nasm -f macho64 output.asm -o output.o')

    # Enlazar el código usando clang
    os.system('clang -o output output.o -lSystem -e _start')


    print("Compilación completa. Ejecuta './output' para ver el resultado.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python compilador.py <archivo_fuente>")
        sys.exit(1)

    main(sys.argv[1])
