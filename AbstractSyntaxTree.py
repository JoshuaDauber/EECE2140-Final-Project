class Equality:
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

class Aexp(Equality):
    pass

class IntAexp(Aexp):
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f'IntAexp({self.val})'

class VarAexp(Aexp):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'VarAexp({self.name})'

class BinopAexp(Aexp):
    def __init__(self, op, l, r):
        self.op = op
        self.l = l
        self.r = r

    def __repr__(self):
        return f'BinopAexp({self.op}, {self.l}, {self.r})'

class Bexp(Equality):
    pass

class RelopBexp(Bexp):
    def __init__(self, op, l, r):
        self.op = op
        self.l = l
        self.r = r

    def __repr__(self):
        return f'RelopBexp({self.op}, {self.l}, {self.r})'

class AndBexp(Bexp):
    def __init__(self, op, l, r):
        self.op = op
        self.l = l
        self.r = r

    def __repr__(self):
        return f'AndBexp({self.op}, {self.l}, {self.r})'

class OrBexp(Bexp):
    def __init__(self, op, l, r):
        self.op = op
        self.l = l
        self.r = r

    def __repr__(self):
        return f'OrBexp({self.op}, {self.l}, {self.r})'

class NotBexp(Bexp):
    def __init__(self, expr):
        self.expr = expr

    def __repr__(self):
        return f'NotBexp({self.expr})'

class Statement(Equality):
    pass

class AssignStatement(Statement):
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

    def __repr__(self):
        return f'AssignStatement({self.var}, {self.expr})'

class CompoundStatement(Statement):
    def __init__(self, frst, scnd):
        self.frst = frst
        self.scnd = scnd

    def __repr__(self):
        return f'CompoundStatement({self.frst}, {self.scnd})'

class IfStatement(Statement):
    def __init__(self, cond, tr, fls):
        self.cond = cond
        self.tr = tr
        self.fls = fls

    def __repr__(self):
        return f'IfStatement({self.cond}, {self.tr}, {self.fls})'

class WhileStatement(Statement):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

    def __repr__(self):
        return f'WhileStatement({self.cond}, {self.body})'

class ForStatement(Statement):
    def __init__(self, var, lo, hi, body): #This may need to be changed
        self.var = var
        self.lo = lo
        self.hi = hi
        self.body = body

    def __repr__(self):
        return f'ForStatement({self.var}, {self.lo}, {self.hi}, {self.body})'
