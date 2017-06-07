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

    def solution(self, goal_node):
        def traverse(node, path=[]):
            self.problem.solution(node.value)
            path.append('action: {action}, cost: {cost}'.format(action=node.action, cost=node.g))
            if node.parent is None:
                return
            traverse(node.parent, path)

        path = []
        traverse(goal_node, path)
        return path

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
