from .lexer import SixenineLexer
from .parser import SixenineParser
from .interpreter import SixenineInterpreter

class SixenineCompiler:
    def __init__(self):
        self.lexer = SixenineLexer()
        self.parser = SixenineParser()
        self.interpreter = SixenineInterpreter()

    def compile_and_run(self, code):
        try:
            # Tokenize
            tokens = self.lexer.tokenize(code)
            
            # Parse
            ast = self.parser.parse(tokens)
            
            # Interpret
            result = self.interpreter.run(ast)
            
            return result
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

def main():
    compiler = SixenineCompiler()
    
    while True:
        try:
            text = input('sixenine> ')
            if text.strip() == "exit":
                break
            result = compiler.compile_and_run(text)
            if result is not None:
                print("=>", result)
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")

if __name__ == '__main__':
    main() 