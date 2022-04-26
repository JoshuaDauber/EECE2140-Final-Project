from Lexer import *
from Parser import *
from AbstractSyntaxTree import *

def keyword(kw):
    return Reserved(kw, RESERVED)

id = Tag(ID)
num = Tag(int) ^ (lambda i: int(i))

def aexpValue():
    return (num ^ (lambda i: IntAexp(i))) | (id ^ (lambda v: VarAexp(v)))

def ProcessGroup(parsed):
    ((_, p), _) = parsed
    return p

def aexpGroup():
    return keyword('(') + Lazy(aexp) + keyword(')') ^ ProcessGroup

def aexpTerm():
    return aexpValue() | aexpGroup()

def processBinop(op):
    return lambda l, r: BinopAexp(op, l, r)

def anyOpInList(ops):
    opParsers = [keyword(op) for op in ops]
    parser = reduce(lambda l, r: l | r, opParsers)
    return parser

aexpPrecedence = [
    ['*', '/'],
    ['+', '-'],
]

def precedence(valueParser, precedenceLevels, combine):
    def opParser(precedenceLevel):
        return anyOpInList(precedenceLevel) ^ combine
    parser = valueParser * opParser(precedenceLevels[0])
    for precedenceLevel in precedenceLevels[1:]:
        parser = parser * opParser(precedenceLevel)
    return parser

def aexp():
    return precedence(aexpTerm, aexpPrecedence, processBinop)

def processRelop(parsed):
    ((left, op), right) = parsed
    return RelopBexp(op, left, right)

def bexpRelop():
    relops = ['<', '<=', '>', '>=', '==', '!=']
    return aexp() + anyOpInList(relops) + aexp() ^ processRelop

def bexpNot():
    return keyword('not') + Lazy(bexpTerm) ^ (lambda b: NotBexp(b[1]))

def bexpGroup():
    return keyword('(') + Lazy(bexp) + keyword(')') ^ ProcessGroup

def bexpTerm():
    return bexpNot() | bexpRelop() | bexpGroup()

bexpPrecedence = [ ['and'], ['or'] ]

def processLogic(op):
    if op == 'and':
        return lambda l, r: AndBexp(l, r)
    elif op == 'or':
        return lambda l, r: OrBexp(l, r)
    else:
        raise Exception('Unknown logic operator: ' + op)

def bexp():
    return precedence(bexpTerm, bexpPrecedence, processLogic)

def assignStmnt():
    def process(parsed):
        ((name, _), exp) = parsed
        return AssignStmnt(name, exp)
    return id + keyword('=') + aexp ^ process

def stmtList():
    sep = keyword(';') ^ (lambda x : lambda l, r: compoundStmnt([l, r]))
    return Exp(stmnt(), sep)

def ifStmnt():
    def process(parsed):
        (((((_, cond), _), trStmnt), flsPrsd), _) = parsed
        if flsPrsd:
            (_, flsStmnt) = flsPrsd
        else:
            flsStmnt = None
        return ifStmnt(cond, trStmnt, flsStmnt)
    return keyword('if') + bexp + keyword('then') + Lazy(stmtList) + Opt(keyword('else') + Lazy(stmtList)) + keyword('end') ^ process

def whileStmnt():
    def process(parsed):
        ((((_, cond), _), body), _) = parsed
        return WhileStmnt(cond, body)
    return keyword('while') + bexp + keyword('do') + Lazy(stmtList) + keyword('end') ^ process

def stmnt():
    return assignStmnt() | ifStmnt() | whileStmnt()

def parser():
    return Phrase(stmtList())

def parse(toks):
    ast = parser()(toks,0)
    return ast

with open('testInput.py') as f:
    characters = f.read()

tokens = lex(characters)
parser = globals()['parser']
ast = parser()(tokens, 0)
print(ast)
