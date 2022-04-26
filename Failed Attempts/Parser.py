class Result:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos

        def __repr__(self):
            return f'Result {self.val} {self.pos}'

class Parser:
    def __call__(self, toks, pos):
        return None

    def __add__(self, other):
        return Concat(self, other)

    def __mul__(self, other):
        return Exp(self, other)

    def __or__(self, other):
        return Alt(self, other)

    def __xor__(self, other):
        return Process(self, other)

class Reserved(Parser):
    def __init__(self, val, tag):
        self.val = val
        self.tag = tag

    def __call__(self, toks, pos):
        if pos < len(toks) and toks[pos][0] == self.val and toks[pos][1] == self.tag:
            return Result(toks[pos][0], pos + 1)
        else:
            return None

class Tag(Parser):
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, toks, pos):
        if pos < len(toks) and toks[pos][1] == self.tag:
            return Result(toks[pos][0], pos + 1)
        else:
            return None

class Concat(Parser):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __call__(self, toks, pos):
        lres = self.left(toks, pos)
        if lres:
            rres = self.right(toks, lres.pos)
            if rres:
                return Result(lres.val + rres.val, rres.pos)
        return None

class Alt(Parser):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __call__(self, toks, pos):
        lres = self.left(toks, pos)
        if lres:
            return lres
        else:
            rres = self.right(toks, pos)
            return rres

class Opt(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, toks, pos):
        res = self.parser(toks, pos)
        if res:
            return res
        else:
            return Result(None, pos)

class Rep(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, toks, pos):
        ress = []
        res = self.parser(toks, pos)
        while res:
            ress.append(res.val)
            pos = res.pos
            res = self.parser(toks, pos)
        return Result(ress, pos)

class Process(Parser):
    def __init__(self, parser, fn):
        self.parser = parser
        self.fn = fn

    def __call__(self, toks, pos):
        res = self.parser(toks, pos)
        if res:
            res.val = self.fn(res.val)
            return res

class Lazy(Parser):
    def __init__(self, parserfn):
        self.parser = None
        self.parserfn = parserfn

    def __call__(self, toks, pos):
        if not self.parser:
            self.parser = self.parserfn()
        return self.parser(toks, pos)

class Phrase(Parser):
    def __init__(self, parser):
        self.parser = parser

    def __call__(self, toks, pos):
        res = self.parser(toks, pos)
        if res and res.pos == len(toks):
            return res
        else:
            return None

class Exp(Parser):
    def __init__(self, parser, sep):
        self.parser = parser
        self.sep = sep

    def __call__(self, toks, pos):
        res = self.parser(toks, pos)

        def process_next(parsed):
                (sepfn, r) = parsed
                return sepfn(res.val, r)
        next_parser = self.sep + self.parser ^ process_next

        next_res = res
        while next_res:
            next_res = next_parser(toks, res.pos)
            if next_res:
                res = next_res
        return res
