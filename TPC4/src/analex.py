import ply.lex as lex

tokens = (
    'COMMAND',
    'WHERE',
    'VARS',
    'VALORES',
    'SEPARADORES',
    'BLOCOS',
    'LIMIT',
    'COMMENT',
    'PREFIX',
    'STRING',
    'RDF_TYPE'
)

t_COMMAND = r'[Ss][Ee][Ll][Ee][Cc][Tt]'
t_WHERE = r'[Ww][Hh][Ee][Rr][Ee]'
t_VARS = r'\?\w*'
t_VALORES = r'-?\d+'
t_SEPARADORES = r"\."
t_BLOCOS = r"[{|}]"
t_LIMIT = r"[Ll][Ii][Mm][Ii][Tt]"
t_COMMENT = r"\#.*"
t_PREFIX = r"\w+:\w+"
t_STRING = r'"([^"]+)"@[a-zA-Z]+'
t_RDF_TYPE = r'\ba\b'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def ana(input):
    out = ""

    lexer = lex.lex()
    lexer.input(input)

    for token in lexer:
        out += (f'{token}\n')

    return out