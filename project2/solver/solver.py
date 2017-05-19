from abc import ABCMeta, abstractmethod
from problem.problem import Problem


class Solver(object):
    __metaclass__ = ABCMeta

    def __init__(self, problem: Problem, steps):
        self.problem = problem
        self.steps = steps

    @abstractmethod
    def solve(self):
        steps = 0

        current_node = self.problem.init_node
        while steps < self.steps:
            pass
