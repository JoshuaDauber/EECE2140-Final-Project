import pydot


class Graph:
    """Graph."""

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
        """make_nodes.
        Make nodes from tokens.

        :param g: graph object
        :param toks: list of tokens
        """
        while cls.count < len(toks):
            if toks[cls.count][1] != 'NEWLINE':
                cls.l.append(toks[cls.count][0])  # splitting into lines
            if toks[cls.count][1] == 'NEWLINE':
                if cls.l[0] == 'if':
                    cls.ifs.append(cls.line)
                    g.add_node(pydot.Node(
                        str(cls.line), label=' '.join(cls.l), shape='diamond'))
                elif cls.l[0] == 'else':
                    cls.elses.append(cls.line)
                elif cls.l[0] == 'while':
                    cls.whiles.append(cls.line)
                    g.add_node(pydot.Node(
                        str(cls.line), label=' '.join(cls.l), shape='diamond'))
                elif cls.l[0] == 'for':
                    cls.fors.append(cls.line)
                    g.add_node(pydot.Node(
                        str(cls.line), label=' '.join(cls.l), shape='diamond'))
                else:
                    g.add_node(pydot.Node(
                        str(cls.line), label=' '.join(cls.l)))
                cls.nodes.append(cls.line)
                cls.l = []  # reset line
            cls.count += 1
            cls.line += 1

        cls.nodes.append('END')  # add end node which will show if needed

    @classmethod
    def make_edges(cls, g):
        """make_edges.
        Make connections between nodes.

        :param g: graph object
        """
        i = 0
        skip = -1
        while i < len(cls.nodes) - 1:
            if cls.nodes[i+1] != 'END':
                if cls.nodes[i] in cls.ifs:
                    #else statement handling
                    if not cls.elses:
                        g.add_edge(pydot.Edge(
                            cls.nodes[i], cls.nodes[i+2], label='Else'))
                    if cls.elses:
                        g.add_edge(pydot.Edge(cls.nodes[i], cls.nodes[i+1]))
                        g.add_edge(pydot.Edge(
                            cls.nodes[i], cls.nodes[i+3], label='Else'))
                        g.add_edge(pydot.Edge(cls.nodes[i+1], cls.nodes[i+4]))
                        g.add_edge(pydot.Edge(cls.nodes[i+3], cls.nodes[i+4]))
                        skip = 2 #skip the add statement for the next 2
                        cls.nodes.remove(cls.elses.pop())
                if not skip >= 0:
                    g.add_edge(pydot.Edge(cls.nodes[i], cls.nodes[i+1]))
                skip -= 1 #just goes every time, it doesn't matter as long as it stays negative
                if cls.nodes[i - 1] in cls.whiles:
                    g.add_edge(pydot.Edge(
                        cls.nodes[i], cls.nodes[i-1], label='Do'))
                if cls.nodes[i - 1] in cls.fors:
                    g.add_edge(pydot.Edge(
                        cls.nodes[i], cls.nodes[i-1], label='Next'))
            i += 1
