from abc import ABCMeta, abstractmethod

from problem.problem import Problem


class Solver(object):
    __metaclass__ = ABCMeta

    def __init__(self, problem: Problem):
        self.problem = problem
        self.num_of_created_nodes = 1
        self.num_of_expanded_nodes = 1

    @abstractmethod
    def solve(self):
        pass


class GoalBaseSolver(Solver):
    __metaclass__ = ABCMeta

    def __init__(self, problem: Problem, tree_search=False):
        super().__init__(problem)
        self.tree_search = tree_search

    @abstractmethod
    def solution(self, goal_node):
        pass

    def _method(self):
        if self.tree_search:
            return 'tree search'
        else:
            return 'graph search'


class BestCaseSolver(Solver):
    __metaclass__ = ABCMeta

    @abstractmethod
    def solution(self):
        pass
