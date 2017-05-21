from enum import Enum, auto

from problem.problem import Problem
from solver.solver import Solver
import random


class HillClimbing(Solver):
    def __init__(self, problem: Problem, mode):
        super().__init__(problem)
        self.mode = mode

    def solve(self):
        if self.mode == Mode.RANDOM_RESTART:
            nodes = []
            for _ in range(10):
                nodes.append(self._solve())
            best_node = nodes[0]
            for node in nodes:
                if self.problem.compute_cost(node) < self.problem.compute_cost(best_node):
                    best_node = node
            self.problem.best_node = best_node
        else:
            self.problem.best_node = self._solve()
        self.problem.solution()

    def _solve(self):
        node = self.problem.init_node

        while True:
            actions = self.problem.actions(node)
            if self.mode == Mode.SIMPLE or self.mode == Mode.RANDOM_RESTART:
                if self.find_best_node(node, actions):
                    node = self.find_best_node(node, actions)
                else:
                    break
            elif self.mode == Mode.STOCHASTIC:
                new_nodes = list(self.find_better_nodes(node, actions))
                if len(new_nodes) > 0:
                    node = random.choice(new_nodes)
                else:
                    break
            elif self.mode == Mode.FIRST_CHOICE:
                if self.find_better_node(node, actions):
                    node = self.find_better_node(node, actions)
                else:
                    break

        return node

    def find_best_node(self, node, actions):
        best_node = node
        for action in actions:
            new_node = self.problem.result(action, node)
            if self.problem.compute_cost(new_node) < self.problem.compute_cost(best_node):
                best_node = new_node
        return best_node

    def find_better_nodes(self, node, actions):
        for action in actions:
            new_node = self.problem.result(action, node)
            if self.problem.compute_cost(new_node) < self.problem.compute_cost(node):
                yield new_node

    def find_better_node(self, node, actions):
        for action in actions:
            new_node = self.problem.result(action, node)
            if self.problem.compute_cost(new_node) < self.problem.compute_cost(node):
                return new_node


class Mode(Enum):
    SIMPLE = auto()
    STOCHASTIC = auto()
    FIRST_CHOICE = auto()
    RANDOM_RESTART = auto()
