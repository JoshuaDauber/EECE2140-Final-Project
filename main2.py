import pydot
from Lexer import *


with open('testInput.py') as f:
    code = f.read()
toke = lex(code, tokens)


def parseIfs(toks):
    res = []
    for i, t in enumerate(toks):
        if t[1] == 'IF':
            res.append(t)
            for t2 in toks[i+1:]:
                if t2[1] != 'COLON':
                    res.append(t2)
                else:
                    break
        if t[1] == 'WHILE':
            res.append(t)
            for t2 in toks[i+1:]:
                if t2[1] != 'COLON':
                    res.append(t2)
                else:
                    break
    return res





def ifStatements(toks):
    ifs = parseIfs(toks)
    stmnt = []
    s = ''
    for t in ifs:
        if t[1] != 'COLON':
            s += t[0]
    #split by if and while
    stmnt = s.split('if')
    stmnt.remove('')
    stmnt = [x.split('while') for x in stmnt]
    stmnt = [item for sublist in stmnt for item in sublist]
    return stmnt

print(ifStatements(toke))


def whileStatements(toks):
    #whiles = parseWhile(toks)
    whiles = []
    stmnt = []
    s = ''
    for t in whiles:
        if t[1] != 'COLON':
            s += t[0]
    stmnt = s.split('while')
    stmnt.remove('')
    return stmnt



ifs = ifStatements(toke)


#g = graphviz.Digraph('G', filename='grrrr.gv')
g = pydot.Dot(graph_type='digraph')
#make a node for each if and connect them all
nodes = []
for i, j in enumerate(ifs):
    g.add_node(pydot.Node(i, label="if " + str(ifs[i]), shape='diamond'))
    nodes.append(i)

for n in range(len(nodes) - 1):
    g.add_edge(pydot.Edge(n, n+1))


g.write_png('test.png')
