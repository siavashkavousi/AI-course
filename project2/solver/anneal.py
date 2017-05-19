from problem.problem import Problem
from .solver import Solver


class Annealer(Solver):
    def __init__(self, problem: Problem, steps):
        super().__init__(problem, steps)

    def solve(self):
        self.problem.compute_cost()
