from abc import ABCMeta, abstractmethod
from problem.problem import Problem


class Solver(object):
    __metaclass__ = ABCMeta

    def __init__(self, problem: Problem):
        self.problem = problem

    @abstractmethod
    def solve(self):
        pass
