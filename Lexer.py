#control flow options
# if - elif - else
# for
# while
# break
# continue
# pass
# def
# class
# import

import re

tokens = [
    (r'^[ ]+', 'INDENT'),  # indent
    (r'[\r\n]+', 'NEWLINE'),  # newline
    (r'[ \n\t]+', None),  # whitespace
    (r'#[^\n]*', None),  # comment
    (r'\=', 'ASSIGN'),  # assignment
    (r'\+', 'PLUS'),  # addition
    (r'\-', 'MINUS'),  # subtraction
    (r'\*', 'MULT'),  # multiplication
    (r'\/', 'DIV'),  # division
    (r'\(', 'LPAREN'),  # left parenthesis
    (r'\)', 'RPAREN'),  # right parenthesis
    (r'<', 'LT'),  # less than
    (r'>', 'GT'),  # greater than
    (r'<=', 'LE'),  # less than or equal
    (r'>=', 'GE'),  # greater than or equal
    (r'==', 'EQ'),  # equal
    (r'!=', 'NE'),  # not equal
    (r'and', 'AND'),  # and
    (r'or', 'OR'),  # or
    (r'not', 'NOT'),  # not
    (r'if', 'IF'),  # if
    (r'elif', 'ELIF'),  # elif
    (r'else', 'ELSE'),  # else
    (r'while', 'WHILE'),  # while
    (r'break', 'BREAK'),  # break
    (r'continue', 'CONTINUE'),  # continue
    (r'pass', 'PASS'),  # pass
    (r'\:', 'COLON'),  # colon
    (r'\d+', 'INT'),  # integer
    (r'^-?\\d*(\\.\\d+)?$', 'NUMBER'),  # number
    (r'[A-Za-z][A-Za-z0-9_]*', 'ID'),  # identifier
    (r'.*', 'ALL')  # all
]


def lex(chars, toks):
    pos = 0
    tokens = []
    while pos < len(chars):
        match = None
        for tok in toks:
            pat, tag = tok
            regex = re.compile(pat)
            match = regex.match(chars, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            raise RuntimeError('invalid syntax')
        else:
            pos = match.end(0)
    return tokens
