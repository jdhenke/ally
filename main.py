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
                        leafLeftSituation = JAnd(situation, singleton(self.util(leafLeft) >= self.util(leafRight)))
                        leafRightSituation = JAnd(situation, singleton(self.util(leafRight) >= self.util(leafLeft)))
                        self.solutions[leafLeft] = JOr(self.solutions[leafLeft], leafLeftSituation)
                        self.solutions[leafRight] = JOr(self.solutions[leafRight], leafRightSituation)

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

def lpsolve(inequalities, root, terminals, winner):
    prob = LpProblem("LP Leading to %s" % winner,LpMaximize)
    obj = LpVariable("ignore")
    # dummy objective function
    prob += obj
    prob += obj == 1.0
    for ineq  in inequalities:
        if ineq is False:
            return False, None
        elif ineq is True:
            continue
        else:
            prob += ineq
    prob.writeLP("temp.lp")
    prob.solve()
    return prob.status == 1, prob

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

    xi = LpVariable("xi")
    xj = LpVariable("xj")
    xk = LpVariable("xk")
    yi = LpVariable("yi")

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

    terminals = (t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11)

    d0 = FolderNode((r0, t1), lambda x: x.utilities["d"])

    print "# Solutions to Cooley's Game\n"
    print '## Intro'
    print '''
Sup B. Here are my findings.

Basically, you can arrive at any terminal node from the top. 
I formulated the entire thing as a linear program, case you're interested.
I'm not sure how what this means for your model, but it could also definitely be my implementation.
Fortunately, there is a really easy/terrible way to check this hypothesis: **manually check the answers I got.**
I love helping you out bud, but really not feeling like crunching these numbers by hand, but I figured I'd share them with you if you want to do so yourself.

Below I list the

  - exogenous variables I used and their values
  - each solution i found leading to each of the terminal nodes, named per your PDF
    - note: these are just one solution of many I found per node
  - the actual code from my program which plugs in the equations

Bottom line, I think you should double check these results and my equations to confirm that the model you proposed can't be decided just given exogenous variables.
I think of this as a proof by contradiction :-)
    '''
    print "## Exogenous Variables"
    print "\tpd1=%s" % (pd1,)
    print "\tpr1=%s" % (pr1,)
    print "\tpa=%s" % (pa, )
    print "\tpd2=%s" % (pd2, )
    print "\tpr2=%s" % (pr2, )
    print "\tk=%s" % (k, )
    print ""
    print "\tba=%s" % (ba, )
    print "\tbd=%s" % (bd, )
    print "\tbr=%s" % (br, )




    root = d0
    root.solve()
    # pprint(root.solutions)
    leaves = [(int(leaf.name[1:]), leaf) for leaf in list(root.solutions.keys())]
    leaves.sort()
    print leaves
    for name, leaf in leaves:
        solutions = root.solutions[leaf]
        solved = False
        for option in solutions:
            if solved:
                continue
            success, solution = lpsolve(option, root, terminals, leaf)
            if success:
                solved = True
                print '\n##  Solution leading to terminal node %s' % (leaf, )
                print '\n### Here are the values of the endogenous variables\n'
                for v in solution.variables():
                    print "\t%s=%s" % (v.name, v.varValue, )
                print '\n### Here are the utilities of each actor at each terminal node\n'
                for t in terminals:
                    print "\t " + t.name
                    for u, util in t.utilities.iteritems():
                        if pulp.value(util) is None:
                            print "\t\t%s: ?None?  = %s" % (u, util, )
                        else:
                            print "\t\t%s: %.5f = %s" % (u, pulp.value(util), util, )
                
                print '\n### Here is information about the linear program that was formulated\n'
                sol = str(solution)
                for line in sol.split('\n'):
                    print "\t%s" % (line, )
    print "\n## Here's the actual equations in my code"


if __name__ == '__main__':
    main()












