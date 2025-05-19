import sys
import os

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.compiler import SixenineCompiler

def run_file(filename):
    try:
        with open(filename, 'r') as f:
            code = f.read()
        
        compiler = SixenineCompiler()
        result = compiler.compile_and_run(code)
        return result
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    run_file(filename)

if __name__ == '__main__':
    main() 