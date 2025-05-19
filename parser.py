from sly import Parser
from .lexer import SixenineLexer

class SixenineParser(Parser):
    tokens = SixenineLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE),
    )

    def __init__(self):
        self.env = {}

    @_('statements')
    def program(self, p):
        return ('program', p.statements)

    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('statements statement')
    def statements(self, p):
        return p.statements + [p.statement]

    @_('func_def')
    def statement(self, p):
        return p.func_def

    @_('FUNC ID LPAREN parameters RPAREN LBRACE statements RBRACE')
    def func_def(self, p):
        return ('func_def', p.ID, p.parameters, p.statements)

    @_('ID COMMA parameters')
    def parameters(self, p):
        return [p.ID] + p.parameters

    @_('ID')
    def parameters(self, p):
        return [p.ID]

    @_('')
    def parameters(self, p):
        return []

    @_('WHILE LPAREN condition RPAREN LBRACE statements RBRACE')
    def statement(self, p):
        return ('while', p.condition, p.statements)

    @_('IF LPAREN condition RPAREN LBRACE statements RBRACE')
    def statement(self, p):
        return ('if', p.condition, p.statements)

    @_('IF LPAREN condition RPAREN LBRACE statements RBRACE ELSE LBRACE statements RBRACE')
    def statement(self, p):
        return ('if_else', p.condition, p.statements0, p.statements1)

    @_('expr EQ expr',
       'expr LT expr',
       'expr GT expr')
    def condition(self, p):
        return (p[1], p.expr0, p.expr1)

    @_('ID ASSIGN expr SEMICOLON')
    def statement(self, p):
        return ('assign', p.ID, p.expr)

    @_('PRINT LPAREN expr RPAREN SEMICOLON')
    def statement(self, p):
        return ('print', p.expr)

    @_('RETURN expr SEMICOLON')
    def statement(self, p):
        return ('return', p.expr)

    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr')
    def expr(self, p):
        return (p[1], p.expr0, p.expr1)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('NUMBER')
    def expr(self, p):
        return ('number', p.NUMBER)

    @_('STRING')
    def expr(self, p):
        return ('string', p.STRING)

    @_('ID')
    def expr(self, p):
        return ('var', p.ID)

    @_('ID LPAREN arguments RPAREN')
    def expr(self, p):
        return ('call', p.ID, p.arguments)

    @_('expr COMMA arguments')
    def arguments(self, p):
        return [p.expr] + p.arguments

    @_('expr')
    def arguments(self, p):
        return [p.expr]

    @_('')
    def arguments(self, p):
        return []

    def error(self, token):
        if token:
            lineno = getattr(token, 'lineno', 0)
            if token.type == '$end':
                print(f'sly: Syntax error at EOF')
            else:
                print(f'sly: Syntax error at line {lineno}, token={token.type}')
        else:
            print('sly: Parse error in input. EOF') 