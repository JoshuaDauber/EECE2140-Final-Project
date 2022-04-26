from Lexer import *
import pydot
import sys

with open(str(sys.argv[1])) as f:
    code = f.read()
    toks = lex(code, tokens)

print(toks)

g = pydot.Dot(graph_type='digraph')
count = 0
line = 0
l = []

nodes = []
ifs = []
endifs = []
whiles = []
fors = []
while count < len(toks):
    if toks[count][1] != 'NEWLINE':
        l.append(toks[count][0])
    if toks[count][1] == 'NEWLINE':
        if l[0] == 'if':
            ifs.append(line)
            print('IF')
            g.add_node(pydot.Node(
                str(line), label=' '.join(l), shape='diamond'))
            #check for indents to see when if statement ends
    # lexer isn't getting indents properly
#            ifc = 0
#            for i in range(count+1, len(toks)):
#                if (toks[i][1] != 'NEWLINE'):
#                    print(toks[i][1])
#                    if toks[i][1] != 'INDENT':
#                        ifc += 1
#                    else:
#                        endifs.append(count+ifc)
#                        break
        elif l[0] == 'while':
            whiles.append(line)
            print('WHILE')
            g.add_node(pydot.Node(
                str(line), label=' '.join(l), shape='diamond'))
        elif l[0] == 'for':
            fors.append(line)
            print('FOR')
            g.add_node(pydot.Node(
                str(line), label=' '.join(l), shape='diamond'))
        else:
            g.add_node(pydot.Node(str(line), label=' '.join(l)))
        nodes.append(line)
        l = []
    count += 1
    line += 1

print(endifs)


for i in range(len(nodes) - 1):
    if nodes[i] in ifs:
        g.add_edge(pydot.Edge(nodes[i], nodes[i+2], label='Else'))
    g.add_edge(pydot.Edge(nodes[i], nodes[i+1]))
    if nodes[i - 1] in whiles:
        g.add_edge(pydot.Edge(nodes[i], nodes[i-1], label='Do'))
    if nodes[i - 1] in fors:
        g.add_edge(pydot.Edge(nodes[i], nodes[i-1], label='Next'))


g.write_png(str(sys.argv[2]))
