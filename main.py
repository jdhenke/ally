#!/bin/python


from sympy import And, Or, Symbol
from sympy.core.relational import Relational
from sympy.logic.inference import satisfiable
from pprint import pprint


class Node(object):
    '''Abstract class to represent a node in a tree'''
    pass

class TerminalNode(object):
    def __init__(self, name, utilities):
        self.name = name
        self.utilities = utilities
        self.solutions = {self: True}
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
                self.solutions[leaf] = False
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

                        self.solutions[leafLeft] = Or(self.solutions[leafLeft],
                                                      self.flatten(And(childLeft.solutions[leafLeft],
                                                          childRight.solutions[leafRight],
                                                          self.util(leafLeft) > self.util(leafRight))))
                        self.solutions[leafRight] = Or(self.solutions[leafRight],
                                                      self.flatten(And(childLeft.solutions[leafLeft],
                                                        childRight.solutions[leafRight],
                                                        self.util(leafRight) > self.util(leafLeft))))
        self.solved = True

    def flatten(self, term):
        # term is and And of solutoins
        # solutions should always be a bool, inequality or Or of inequalities

        return term

        # if it was simplified
        if isinstance(term, Relational) or isinstance(term, bool):
            return term

        # if contains more than two terms
        elif isinstance(term, And):
            groups = []
            for arg in term.args:
                # args can be solutions, but not bools
                if isinstance(arg, Relational):
                    groups.append((arg,))
                elif isinstance(arg, Or):
                    groups.append(arg.args)
            lhs = 0
            rhs = 0
            # TODO: combine groups of inequalities anded together into a flat list of inequalities
            return lhs > rhs
        else:
            raise Exception("Weird class encountered: " + term)

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
    d0.solve()
    for leaf in d0.solutions:
        condition = d0.solutions[leaf]
        print "\t %s, %s"% (leaf, satisfiable(condition, algorithm="dpll2"), )

    '''
    # mini testing with tree solver
    nodes = [TerminalNode(letter) for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNOPQRSTUVWXYZ"[:16]]
    while len(nodes) > 1:
        newnodes = []
        for i in xrange(0, len(nodes), 2):
            newnodes.append(FolderNode(nodes[i:i+2]))
        nodes = newnodes
    root = nodes[0]
    root.solve()
    print root.solutions

    # mini testing with named booleans
    p = NamedPremise(True, "The sky is blue")
    q = NamedPremise(False, "The birds and the bees")

    assert not And(p,q)
    assert Or(p,q)
    assert And(p,p)
    assert not And(q,q)
    print p.__toString__(), q.__toString__()
    '''



if __name__ == '__main__':
    main()












