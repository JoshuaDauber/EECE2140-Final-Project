from Lexer import *
import pydot

with open('test.py') as f:
    g = pydot.Dot(graph_type='digraph')
    nodes = []
    ifs = []
    for i, line in enumerate(f):
        ltok = lex(line, tokens)

        if ltok:
            if ltok[0][1] == 'IF':
                g.add_node(pydot.Node(i, label=line.strip(),shape='diamond'))
                nodes.append(i)
                ifs.append(i)
            if ltok[0][1] == 'ID':
                g.add_node(pydot.Node(i, label=line.strip(),shape='circle'))
                nodes.append(i)

    print(nodes)
    print(ifs)


    for i in range(len(nodes) - 1):
        if nodes[i] in ifs:
            print('Here!')
            g.add_edge(pydot.Edge(nodes[i], nodes[i+2], label='Else'))
        g.add_edge(pydot.Edge(nodes[i], nodes[i+1]))

g.write_png('testing.png')


