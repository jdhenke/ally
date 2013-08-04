#!/bin/python

'''
Library for formulating and solving game trees as linear programs.
'''

class Node(object):
    '''Abstract class to represent a node in the game tree.'''

    def solve(self):
        '''
        Should populate the solutions dictionary.

        solutions: TerminalNode ==> list of lists of inequalities

        Basically, if you treat the inequalities as booleans, it stores
        the requirements to arrive at the terminal node in CDF form.

        '''
        raise NotImplementedError(
            "Solve is not defined for Node. \
             Instantiate a subclass instead")

class TerminalNode(Node):
    '''A leaf in the game tree.'''
    def __init__(self, name, utilities):
        '''
        @name - A string which uniquely identifies this node
        @utilities - Anything. 
                     Must mesh with FolderNode utility functions though

        '''
        self.name = name
        self.utilities = utilities
        self.solutions = {self: singleton(True)}
    def solve(self):
        # pass because the only solution is this node itself
        # stops the recursion
        pass
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __hash__(self):
        return hash(self.name)

class FolderNode(Node):
    def __init__(self, children, util_func):
        self.children = children
        self.solutions = {}
        self.util = util_func
    def solve(self):
        '''Calls solve on entire subtree too'''
        
        # if empty folder, no children
        if len(self.children) == 0:
            return

        # at least 1 child, so solve all of them
        for child in self.children:
            child.solve()
            for leaf in child.solutions:
                self.solutions[leaf] = singleton(False)

        # if only one child, there is no choice, so use decision makeing 
        # criteria of that child
        if len(self.children) == 1:
            self.solution = self.children[0].solutions
            return
        
        # if more than 1 child, will need to find all ways possible to arrive
        # at each leaf
        for leftLeaf, rightLeaf, leftChild, rightChild in self._gen_children():
            # requirements to come down to decision between these two leaves
            req = And(leftChild.solutions[leftLeaf], rightChild.solutions[rightLeaf])
            # get utilities of each leaf
            leftUtil = self.util(leftLeaf)
            rightUtil = self.util(rightLeaf)
            # to choose left leaf, need req and that left is better than right
            reqLeftWins = And(req, singleton( leftUtil >= rightUtil ))
            reqRightWins = And(req, singleton( rightUtil >= leftUtil ))
            # add this to possible solutions
            self.solutions[leftLeaf] = Or(self.solutions[leftLeaf], reqLeftWins)
            self.solutions[rightLeaf] = Or(self.solutions[rightLeaf], reqRightWins)

    def _gen_children(self):
        '''
        Generator for all pairs of leaves l1, l2 st. 
        l1 and l2 are in different immediate subtrees.

        Also includes these immediate subtrees roots i.e. this nodes
        direct children.

        So yields: (leftLeaf, rightLeaf, leftChild, rightChild, )
        '''
        for i in xrange(len(self.children)-1):
            for j in xrange(i + 1, len(self.children)):
                leftChild = self.children[i]
                rightChild = self.children[j]
                leftLeaves = leftChild.solutions.keys()
                rightLeaves = rightChild.solutions.keys()
                for leftLeaf in leftLeaves:
                    for rightLeaf in rightLeaves:
                        yield (leftLeaf, rightLeaf, leftChild, rightChild, )

# functions which maintain CDF form of inequalities

def And(a, b):
    output = []
    for x in a:
        for y in b:
            output.append(x+y)
    # must be tuple to be able to add together
    return tuple(output)

def Or(a, b):
    return a+b

def singleton(x):
    # must be a list of lists
    return ((x,),)

