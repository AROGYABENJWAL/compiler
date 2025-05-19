from sly import Lexer

class SixenineLexer(Lexer):
    # Set of token names
    tokens = {
        ID, NUMBER, STRING,
        PLUS, MINUS, TIMES, DIVIDE,
        ASSIGN, LPAREN, RPAREN,
        LBRACE, RBRACE,
        IF, ELSE, WHILE, FUNC,
        RETURN, PRINT,
        EQ, LT, GT,
        COMMA, SEMICOLON
    }

    # String containing ignored characters
    ignore = ' \t'
    ignore_newline = r'\n+'
    ignore_comment = r'#.*'

    # Regular expression rules for tokens
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['func'] = FUNC
    ID['return'] = RETURN
    ID['print'] = PRINT

    NUMBER = r'\d+'
    STRING = r'\".*?\"'
    
    # Special symbols
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACE = r'\{'
    RBRACE = r'\}'
    EQ = r'=='
    LT = r'<'
    GT = r'>'
    COMMA = r','
    SEMICOLON = r';'

    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    def STRING(self, t):
        t.value = t.value[1:-1]  # Remove the quotes
        return t

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print(f"Illegal character '{t.value[0]}' at line {self.lineno}")
        self.index += 1 