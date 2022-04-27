from lexerButAClass import *
from GraphClass import *
import pydot
import sys

with open(str(sys.argv[1])) as f:  # open file and read/lex it
    code = f.read()
    toks = Lexer.lex(code, tokens)


g = pydot.Dot(graph_type='digraph')

Graph.make_nodes(g, toks)
Graph.make_edges(g)


g.write_png(str(sys.argv[2]))
