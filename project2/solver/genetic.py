from functools import reduce

from problem.problem import Problem
from solver.solver import Solver


class Genetic(Solver):
    def __init__(self, problem: Problem):
        super().__init__(problem)

    def solve(self):
        pass

    def fitness(self, node):
        return reduce(lambda x, y: x.value + y.value, node.value)
