from antlr4 import *
import os
from grammarTraductorLexer import grammarTraductorLexer
from grammarTraductorParser import grammarTraductorParser
from grammarTraductorListener import grammarTraductorListener
from TraduceCode import TraduceCode

def main():
    # Solicita al usuario la ruta del archivo
    in_code = input('> ')

    current_dir = os.path.dirname(os.path.abspath(__file__))
    in_code = os.path.join(current_dir, in_code)

    # Intentar abrir y leer el archivo
    try:
        with open(in_code, 'r') as archivo:
            input_stream = InputStream(archivo.read())
    except FileNotFoundError:
        print(f"Error: El archivo '{in_code}' no fue encontrado.")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return


    ## Se crea una archivo para guardar el código traducido:
    file_path = os.path.join(current_dir, 'in_code')

    # Verificar si el archivo ya existe
    if os.path.exists(file_path):
        # Eliminar el archivo si existe
        os.remove(file_path)
        print(f"El archivo {file_path} ya existía y ha sido eliminado.")

    # Crear el archivo de nuevo
    with open(file_path, 'w') as file:
        file.write("// Archivo traducido a Java\n")  # Escribe una cabecera en el archivo
        print(f"El archivo {file_path} ha sido creado.")

    # Crear el lexer y el parser
    lexer = grammarTraductorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = grammarTraductorParser(stream)

    # Analizar el árbol de sintaxis
    tree = parser.program()

    # Iniciar el recorrido del árbol y traducción con el listener, pasando el archivo como parámetro
    with open(file_path, 'a') as file:  # Abrimos el archivo en modo 'a' para agregar contenido
        # Pasamos la referencia del archivo al listener
        walker = ParseTreeWalker()
        walker.walk(TraduceCode(file), tree)  # El listener escribirá en el archivo

if __name__ == '__main__':
    main()
