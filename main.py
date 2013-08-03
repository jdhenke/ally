#!/bin/python


from sympy import And, Or, Symbol, solve
from sympy.core.relational import Relational
from sympy.logic.inference import satisfiable
from pprint import pprint
from sympy.core.relational import StrictGreaterThan, StrictLessThan
from pulp import *
from sympy.core.add import Add
from sympy.core.mul import Mul
from sympy.core.numbers import Number


class Node(object):
    '''Abstract class to represent a node in a tree'''
    pass

class TerminalNode(object):
    def __init__(self, name, utilities):
        self.name = name
        self.utilities = utilities
        self.solutions = {self: singleton(True)}
    def solve(self):
        pass
    def __hash__(self):
        return hash(self.name)
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

class FolderNode(object):
    def __init__(self, children, util_func):
        self.children = children
        self.solutions = {}
        self.util = util_func
        # self.util = lambda x: "abcd".index(x.name)
    def solve(self):
        # TODO: handle single child
        assert len(self.children) > 1
        for child in self.children:
            child.solve()
            for leaf in child.solutions.keys():
                self.solutions[leaf] = singleton(False)
        # TODO: refactor into generator
        for i in xrange(len(self.children)-1):
            for j in xrange(i + 1, len(self.children)):
                childLeft = self.children[i]
                childRight = self.children[j]
                leavesLeft = childLeft.solutions.keys()
                leavesRight = childRight.solutions.keys()

                for leafLeft in leavesLeft:
                    for leafRight in leavesRight:
                        # TODO: distribute and add ands of primitives
                        situation = JAnd(childLeft.solutions[leafLeft], childRight.solutions[leafRight])
                        leafLeftSituation = JAnd(situation, singleton(self.util(leafLeft) > self.util(leafRight)))
                        leafRightSituation = JAnd(situation, singleton(self.util(leafRight) > self.util(leafLeft)))
                        self.solutions[leafLeft] = JOr(self.solutions[leafLeft], leafLeftSituation)
                        self.solutions[leafRight] = JOr(self.solutions[leafRight], leafRightSituation)

class NamedPremise:
    def __init__(self, value, name):
        self.value = value
        self.name = name
    def __str__(self):
        return str(self.value)
    def __toString__(self):
        return self.name
    def __nonzero__(self):
        return False or self.value

def JAnd(a, b):
    output = []
    for x in a:
        for y in b:
            output.append(x+y)
    return tuple(output)

def JOr(a, b):
    return a+b

def singleton(x):
    return ((x,),)

lpvariables = {
        "xi": LpVariable("xi"),
        "xj": LpVariable("xj"),
        "xk": LpVariable("xk"),
        "yi": LpVariable("yi"),
    }

def convert(expr):
    if isinstance(expr, Number):
        return float(expr)
    elif isinstance(expr, Symbol):
        global lpvariables
        return lpvariables[expr.name]
    elif isinstance(expr, Add):
        answer = 0
        for arg in expr.args:
            answer += convert(arg)
        return answer
    elif isinstance(expr, Mul):
        answer = 1.0
        for arg in expr.args:
            answer *= convert(arg)
        return answer
    elif isinstance(expr, StrictGreaterThan):
        return convert(expr.lhs) >= convert(expr.rhs)
    elif isinstance(expr, StrictLessThan):
        return convert(expr.lhs) <= convert(expr.rhs)
    else:
        raise Exception("Can't convert this sympy type to LP type:\n%s - %s" % (expr.__class__, expr ))

def lpsolve(inequalities):
    prob = LpProblem("The Whiskas Problem",LpMinimize)
    obj = LpVariable("dummy")
    # dummy objective function
    prob += obj
    prob += obj == 1.0
    for ineq in inequalities:
        prob += convert(ineq)
    prob.writeLP("temp.lp")
    prob.solve()
    return prob

def main():

    pd1 = .626
    pr1 = .283
    pa = .1
    pd2 = .426
    pr2 = .483
    k = .15
    
    ba=pa
    bd=pd1
    br=pr1

    xi = Symbol("xi")
    xj = Symbol("xj")
    xk = Symbol("xk")
    yi = Symbol("yi")

    

    

    t6 = TerminalNode("t6", {
        "d": bd - xi - xj - yi,
        "r": br + xi + yi,
        "a": ba + xj,
    })

    t7 = TerminalNode("t7", {
        "d": (bd-xi-xj)+(pd2+pa)*(br+xi)*(pd2/(pd2+pa))-pr2*(bd-xi-xj)-k*(pd2/(pd2+pa)),
        "r": (br+xi)+pr2*(bd-xi+ba)-(pd2+pa)*(br+xi)-k,
        "a": (ba+xj)+(pd2+pa)*(br+xi)*(pa/(pd2+pa))-pr2*(ba+xj)-k*(pa/(pd2+pa)),
    })

    r1 = FolderNode((t6, t7), lambda x: x.utilities["r"])

    t3 = TerminalNode("t3", {
        "d": (bd-xi-xj)+(pd2+pa)*(br+xi)*(pd2/(pd2+pa))-pr2*(bd-xi-xj)-k*(pd2/(pd2+pa)),
        "r": (br+xi)+pr2*(bd-xi+ba)-(pd2+pa)*(br+xi)-k,
        "a": (ba+xj)+(pd2+pa)*(br+xi)*(pa/(pd2+pa))-pr2*(ba+xj)-k*(pa/(pd2+pa)),
    })

    d1 = FolderNode((r1, t3), lambda x: x.utilities["d"])

    t8 = TerminalNode("t8", {
        "d": bd-xi-yi,
        "r": br+xi+yi,
        "a": ba,
    })

    t9 = TerminalNode("t9", {
        "d": (bd-xi)+pd2*(br+xi)-pr2*(bd-xi)-k,
        "r": (br+xi)+pr2*(bd-xi)-pd2*(br+xi)-k,
        "a": ba,
    })

    r2 = FolderNode((t8, t9), lambda x: x.utilities["r"])

    t4 = TerminalNode("t4", {
        "d": (bd - xi)+pd2*(br+xi)-pr2*(bd-xi)-k,
        "r": (br+xi)+pr2*(bd-xi)-pd2*(br+xi)-k,
        "a": ba,
    })

    d2 = FolderNode((r2, t4), lambda x: x.utilities["d"])

    t10 = TerminalNode("t10", {
        "d": bd - xi-yi,
        "r": br+xi-xk+yi,
        "a": ba+xk,
    })

    t11 = TerminalNode("t11", {
        "d": (bd-xi)+pd2*(bd+xi+ba)-(pr2+pa)*(bd-xi)-k,
        "r": (br+xi-xk)+(pr2+pa)*(bd-xi)*(pr2/(pr2+pa))-pd2*(br+xi-xk)-k*(pr2/(pr2+pa)),
        "a": (ba+xk)+(pr2+pa)*(bd-xi)*(pa/(pr2+pa))-pd2*(ba+xk)-k*(pa/(pr2+pa)),
    })

    r3 = FolderNode((t10, t11), lambda x: x.utilities["r"])

    t5 = TerminalNode("t5", {
        "d": (bd-xi)+pd2*(bd+xi+ba)-(pr2+pa)*(bd-xi)-k,
        "r": (br+xi-xk)+(pr2+pa)*(bd-xi)*(pr2/(pr2+pa))-pd2*(br+xi-xk)-k*(pr2/(pr2+pa)),
        "a": (ba+xk)+(pr2+pa)*(bd-xi)*(pa/(pr2+pa))-pd2*(ba+xk)-k*(pa/(pr2+pa)),
    })

    d3 = FolderNode((r3, t5), lambda x: x.utilities["d"])

    a0 = FolderNode((d1,d2,d3), lambda x: x.utilities["a"])

    t2 = TerminalNode("t2", {
        "d": bd+pd1*br-pr1*bd-k,
        "r": br+pr1*bd-pd1*br-k,
        "a": ba,
    })

    r0 = FolderNode((a0, t2), lambda x: x.utilities["r"])

    t1 = TerminalNode("t1", {
        "d": bd+pd1*br-pr1*bd-k,
        "r": br+pr1*bd-pd1*br-k,
        "a": ba,
    })

    d0 = FolderNode((r0, t1), lambda x: x.utilities["d"])

    print "Solutions"
    root = d0
    root.solve()
    for leaf, solutions in root.solutions.iteritems():
        print leaf
        for option in solutions:
            simplified = And(*option)
            if simplified is not False:
                solution = lpsolve(simplified.args)
                if solution.status == 1:
                    print '\tLeaf %s solved it.' % (leaf, )
                    for v in solution.variables():
                        print "\t\t%s=%s" % (v.name, v.varValue, )

if __name__ == '__main__':
    main()












