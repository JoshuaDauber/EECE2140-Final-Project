import pydot


class Graph:

    nodes = []
    ifs = []
    endifs = []
    whiles = []
    fors = []
    elses = []
    count = 0
    line = 0
    l = []

    @classmethod
    def make_nodes(cls, g, toks):
        while cls.count < len(toks):
            if toks[cls.count][1] != 'NEWLINE':
                cls.l.append(toks[cls.count][0])
            if toks[cls.count][1] == 'NEWLINE':
                if cls.l[0] == 'if':
                    cls.ifs.append(cls.line)
                    print('IF')
                    g.add_node(pydot.Node(
                        str(cls.line), label=' '.join(cls.l), shape='diamond'))
                #testing elses
                elif cls.l[0] == 'else':
                    cls.elses.append(cls.line)
                    print('ELSE')
                elif cls.l[0] == 'while':
                    cls.whiles.append(cls.line)
                    print('WHILE')
                    g.add_node(pydot.Node(
                        str(cls.line), label=' '.join(cls.l), shape='diamond'))
                elif cls.l[0] == 'for':
                    cls.fors.append(cls.line)
                    print('FOR')
                    g.add_node(pydot.Node(
                        str(cls.line), label=' '.join(cls.l), shape='diamond'))
                else:
                    g.add_node(pydot.Node(str(cls.line), label=' '.join(cls.l)))
                cls.nodes.append(cls.line)
                cls.l = []
            cls.count += 1
            cls.line += 1

        cls.nodes.append('END')

    @classmethod
    def make_edges(cls, g):
        i = 0
        skip = -1
        #for i in range(len(nodes) - 1):
        while i < len(cls.nodes) - 1:
            if cls.nodes[i+1] != 'END':
                if cls.nodes[i] in cls.ifs:
                    if not cls.elses:
                        g.add_edge(pydot.Edge(cls.nodes[i], cls.nodes[i+2], label='Else'))
                    if cls.elses:
                        g.add_edge(pydot.Edge(cls.nodes[i], cls.nodes[i+1]))
                        g.add_edge(pydot.Edge(cls.nodes[i], cls.nodes[i+3], label='Else'))
                        print(i)
                        g.add_edge(pydot.Edge(cls.nodes[i+1], cls.nodes[i+4]))
                        g.add_edge(pydot.Edge(cls.nodes[i+3], cls.nodes[i+4]))
                        skip = 2
                        cls.nodes.remove(cls.elses.pop())
                print(i)
                print(skip)
                print(cls.nodes)
                if not skip >= 0:
                    g.add_edge(pydot.Edge(cls.nodes[i], cls.nodes[i+1]))
                skip -= 1
                if cls.nodes[i - 1] in cls.whiles:
                    g.add_edge(pydot.Edge(cls.nodes[i], cls.nodes[i-1], label='Do'))
                if cls.nodes[i - 1] in cls.fors:
                    g.add_edge(pydot.Edge(cls.nodes[i], cls.nodes[i-1], label='Next'))
            i += 1
