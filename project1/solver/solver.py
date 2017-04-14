from abc import ABCMeta, abstractmethod
from problem.problem import Problem


class Solver(object):
    __metaclass__ = ABCMeta

    def __init__(self, problem: Problem, tree_search=False):
        self.problem = problem
        self.tree_search = tree_search

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def next_node(self):
        pass

    def _method(self):
        if self.tree_search:
            return 'tree search'
        else:
            return 'graph search'
