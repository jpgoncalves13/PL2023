import ply.lex as lex

tokens = (
    "INITCOMMENT",
    "CLOSECOMMENT",
    "COMMENT",
    "INT",
    "ID",
    "PVIR",
    "FUNCTION",
    "APARENTESISC",
    "FPARENTESISC",
    "VAR",
    "EQUAL",
    "NUM",
    "WHILE",
    "OPERATOR", # '*', '-', '>', '<'
    "ACHAVETA",
    "FCHAVETA",
    "PROGRAM",
    "FOR",
    "APARENTESISR",
    "FPARENTESISR",
    "PRINT",
    "IN",
    "VIRGULA",
    "IF",
    "DPONTOS"
)

t_NUM = r'\d+'
t_ID = r'\w+'
t_EQUAL = r'='
t_PVIR = r';'
t_OPERATOR = r'[\-*><]'
t_DPONTOS = r'\.\.'
t_ACHAVETA = r'{'
t_FCHAVETA = r'}'
t_APARENTESISC = r'('
t_FPARENTESISC = r')'
t_APARENTESISR = r'\['
t_FPARENTESISR = r'\]'
t_VIRGULA = r','

def t_INT(t):
    r'\bint\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_PRINT(t):
    r'\bprint\(\w+\)'
    return t

def t_FOR(t):
    r'\bfor\b'
    return t

def t_WHILE(t):
    r'\bwhile\b'
    return t

def t_IN(t):
    r'\bin\b'
    return t

def t_IF(t):
    r'\bif\b'
    return t

def t_FUNCTION(t):
    r'\bfunction\b'
    return t

def t_PROGRAM(t):
    r'\bprogram\b'
    return t

def t_INITCOMMENT(t):
    r'/\*'
    t.lexer.begin('commentml')
    return t

def t_commentml_CLOSECOMMENT(t):
    r'\*/'
    t.lexer.begin('INITIAL')
    return t

def t_commentml_ANY(t):
    r'(.|\n)'
    pass

def t_COMMENT(t):
    r'//'
    t.lexer.begin('commentl')
    return t

def t_commentl_newline(t):
    r'\n'
    t.lexer.begin('INITIAL')

def t_commentl_ANY(t):
    r'.'
    pass

t_ignore = ' \n\t'

t_commentml_ignore = ''

t_commentl_ignore = ''

# Error rule for the initial state
def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

def t_commentml_error(t):
    pass

def t_commentl_error(t):
    pass

# Build the lexer
lexer = lex.lex()

data = """
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/
int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};
// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
"""

lexer.input(data)

for tok in lexer:
    print(tok)

