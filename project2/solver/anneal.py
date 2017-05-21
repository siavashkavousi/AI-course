import math

from problem.problem import Problem
from .solver import Solver
from random import random


class Annealer(Solver):
    def __init__(self, problem: Problem):
        super().__init__(problem)
        self.temperature = 10000
        self.cooling_rate = 0.03

    def solve(self):
        node = self.problem.init_node

        while self.temperature > 1:
            action = self.problem.actions(node)
            new_node = self.problem.result(action, node)

            if self.acceptance_probability(self.problem.compute_cost(node),
                                           self.problem.compute_cost(new_node)) > random():
                node = new_node
            if self.problem.compute_cost(node) > self.problem.compute_cost(self.problem.best_node):
                self.problem.best_node = node

            self.temperature = 1 - self.cooling_rate

        self.problem.solution()

    def acceptance_probability(self, current_energy, new_energy):
        if new_energy > current_energy:
            return 1
        return math.exp((current_energy - new_energy) / self.temperature)
