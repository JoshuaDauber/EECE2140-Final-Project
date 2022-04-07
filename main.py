import graphviz

#options for statements
ifs = []
whiles = []
fors = []

#pasrsing the file
with open('testInput.py') as f:
    for line in f:
        if '#' in line:
            line = line.split('#')[0]
        if 'if' in line:
            ifs.append(line)
        if 'while' in line:
            whiles.append(line)
        if 'for' in line:
            fors.append(line)

#split ifs between if and :
ifConds = [ifs[i].split('if')[1].split(':')[0].lstrip()
           for i in range(len(ifs))]
#split whiles between while and :
whileConds = [whiles[i].split('while')[1].split(
    ':')[0].lstrip() for i in range(len(whiles))]


#graph stuff
g = graphviz.Digraph('G', filename='graph.gv')
for i in range(len(ifs)):
    g.node(str(i), 'if block') #swap this out for what actually happens in the if statement
    g.edge(str(i), str(i+1), label=' if ' + ifConds[i])
for i in range(len(whiles)):
    g.node(str(i+len(ifs)), 'while ' + whileConds[i])
    g.edge(str(i+len(ifs)), str(i+len(ifs)+1))
for i in range(len(fors)):
    g.node(str(i+len(ifs)+len(whiles)), fors[i])
    g.edge(str(i+len(ifs)+len(whiles)), str(i+len(ifs)+len(whiles)+1))
g.view()
