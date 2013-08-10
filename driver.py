from core import *
from pulp import *
from pprint import pprint

'''Runs Cooley's game and prints results in Markdown'''

def main():

    print "# Solutions to Cooley's Game"
    
    # Exogenous variables
    pd1 = .626
    pr1 = .283
    pa = .1
    pd2 = .426
    pr2 = .483
    k = .15
    
    # Starting conditions
    ba=pa
    bd=pd1
    br=pr1

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

    # endogenous variables
    xi = LpVariable("xi")
    xj = LpVariable("xj")
    xk = LpVariable("xk")
    yi = LpVariable("yi")
    yj = LpVariable("yj")
    yk = LpVariable("yk")

    # define this function here so can access endogenous variables
    def lpsolve(inequalities, root, winner):
        prob = LpProblem("LP Leading to %s" % winner, LpMaximize)
        obj = LpVariable("utility")
        prob += obj
        prob += obj == root.util(winner)
        for ineq  in inequalities:
            if ineq is False:
                return False, None, None
            elif ineq is True:
                continue
            else:
                prob += ineq
        
        # EXAMPLE CONSTRAINT
        # prob += xi == 0.1
        # prob += xj == 0.1
        # prob += xk == 0.1

        # D's decision
        prob += xi <= bd # can't offer more than d's worth
        prob += xi >= -1.0 * br # can't demand more than r's worth

        # D's decision
        prob += xj <= bd-xi # can't offer more than d's worth
        prob += xj >= -1.0 * ba # can't demand more than a's worth

        # R's decision
        prob += xk <= br + xi # can't offer more than r's worth
        prob += xk >= -1.0 * ba # can't demand more than a's worth

        # D's decision
        prob += yi <= bd - xi - xj # can't offer more than d's worth
        prob += -1.0 * yi <= br + xi # can't demand more than r's worth

        # D's decision
        prob += yi <= bd - xi - xj # can't offer more than d's worth
        prob += -1.0 * yi <= br + xi # can't demand more than r's worth

        # D's decision
        prob += yj <= bd - xi - xj # can't offer more than d's worth
        prob += -1.0 * yj <= br + xi # can't demand more than r's worth

        # D's decision
        prob += yk <= bd - xi - xj # can't offer more than d's worth
        prob += -1.0 * yk <= br + xi # can't demand more than r's worth
        
        prob.writeLP("temp.lp")
        prob.solve()
        return prob.status in (1, -2), prob, pulp.value(obj)

    # DEFINE THE GAME TREE

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
        "d": bd-xi-yj,
        "r": br+xi+yj,
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
        "d": bd - xi-yk,
        "r": br+xi-xk+yk,
        "a": ba+xk,
    })

    t11 = TerminalNode("t11", {
        "d": (bd-xi)+pd2*(br+xi+ba)-(pr2+pa)*(bd-xi)-k,
        "r": (br+xi-xk)+(pr2+pa)*(bd-xi)*(pr2/(pr2+pa))-pd2*(br+xi-xk)-k*(pr2/(pr2+pa)),
        "a": (ba+xk)+(pr2+pa)*(bd-xi)*(pa/(pr2+pa))-pd2*(ba+xk)-k*(pa/(pr2+pa)),
    })

    r3 = FolderNode((t10, t11), lambda x: x.utilities["r"])

    t5 = TerminalNode("t5", {
        "d": (bd-xi)+pd2*(br+xi+ba)-(pr2+pa)*(bd-xi)-k,
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

    # PROCESS THE GAME TREE

    root = d0 #d0 is true root
    root.solve()
    leaves = [(int(leaf.name[1:]), leaf) for leaf in list(root.solutions.keys())]
    leaves.sort()
    solvedLeaves = set()
    utilities = []
    for name, leaf in leaves:
        solutions = root.solutions[leaf]
        solved = False
        for option in solutions:
            success, solution, utility = lpsolve(option, root, leaf)
            if success:
                utilities.append((utility, leaf, pulp.value(xi), pulp.value(xj), pulp.value(xk), pulp.value(yi), ))
                if solved:
                    continue
                solvedLeaves.add(leaf)
                solved = True
                print '\n##  Solution leading to %s' % (leaf, )
                print '\n### Endogenous Variables\n'
                for v in solution.variables():
                    print "\t%s=%s" % (v.name, v.varValue, )
                print '\n### Utilties of Terminal Nodes\n'
                for t in terminals:
                    print "\t" + t.name
                    for u, util in t.utilities.iteritems():
                        if pulp.value(util) is None:
                            print "\t\t%s: ?None?  = %s" % (u, util, )
                        else:
                            print "\t\t%s: %.5f = %s" % (u, pulp.value(util), util, )
                
                print '\n### Linear Program Information\n'
                sol = str(solution)
                for line in sol.split('\n'):
                    print "\t%s" % (line, )

    print "## Total Results"
    solvedLeavesList = [leaf.name for leaf in solvedLeaves]
    solvedLeavesList.sort()
    print "%i leaves had at least 1 solution: `%s`" %\
     (len(solvedLeavesList), solvedLeavesList, )

    print '## Top Utilities %i' % (len(utilities), )
    utilities.sort(reverse=True)
    pprint(utilities[:20])

if __name__ == '__main__':
    main()












