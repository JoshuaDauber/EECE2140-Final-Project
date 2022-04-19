import pydot

#options for statements
ifs = []
whiles = []
fors = []
nodes = []
g = pydot.Dot(graph_type='digraph')
g.add_node(pydot.Node(0, label='start'))
#pasrsing the file
with open('testInput.py') as f:
    i = 1
    for j, line in enumerate(f):
        if '#' in line:
            line = line.split('#')[0]
        if 'if' in line:
            ifs.append(line)
            g.add_node(pydot.Node(
                i, label='if ' + str([line.split('if')[1].split(':')[0].lstrip()]), shape='diamond'))
            nodes.append(i)
            i += 1
        if 'while' in line:
            whiles.append(line)
            g.add_node(pydot.Node(i, label='while ' +
                       str([line.split('while')[1].split(':')[0].lstrip()]), shape='diamond'))
            nodes.append(i)
            i += 1
        if 'for' in line:
            fors.append(line)

#split ifs between if and :
ifConds = [ifs[i].split('if')[1].split(':')[0].lstrip()
           for i in range(len(ifs))]
#split whiles between while and :
whileConds = [whiles[i].split('while')[1].split(
    ':')[0].lstrip() for i in range(len(whiles))]


#graph stuff
#g = graphviz.Digraph('G', filename='graph.gv')
#for i in range(len(ifs)):
#    g.node(str(i), 'if block') #swap this out for what actually happens in the if statement
#    g.edge(str(i), str(i+1), label=' if ' + ifConds[i])
#for i in range(len(whiles)):
#    g.node(str(i+len(ifs)), 'while ' + whileConds[i])
#    g.edge(str(i+len(ifs)), str(i+len(ifs)+1))
#for i in range(len(fors)):
#    g.node(str(i+len(ifs)+len(whiles)), fors[i])
#    g.edge(str(i+len(ifs)+len(whiles)), str(i+len(ifs)+len(whiles)+1))
#g.view()

#g = pydot.Dot(graph_type='digraph')
#nodes = []
#for i, j in enumerate(ifs):
#    g.add_node(pydot.Node(i, label='if ' + str(ifConds[i]), shape='diamond'))
#    nodes.append(i)

for n in range(len(nodes) - 1):
    g.add_edge(pydot.Edge(n, n+1))

g.write_png('ifs.png')
