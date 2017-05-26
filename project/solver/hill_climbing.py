import random
from enum import Enum, auto

from node import Node
from problem.problem import BestCaseProblem
from solver.solver import Solver


class HillClimbing(Solver):
    def __init__(self, problem: BestCaseProblem, mode):
        super().__init__(problem)
        self.mode = mode

    def solve(self):
        if self.mode == Mode.RANDOM_RESTART:
            nodes = []
            for _ in range(10):
                nodes.append(self._solve())
            best_node = nodes[0]
            for node in nodes:
                if self.problem.compute_cost(node.value) < self.problem.compute_cost(best_node.value):
                    best_node = node
            self.problem.best_state = best_node.value
        else:
            self.problem.best_state = self._solve().value

    def _solve(self):
        node = Node(self.problem.init_state)

        while True:
            actions = list(self.problem.actions(node.value))
            if self.mode == Mode.SIMPLE or self.mode == Mode.RANDOM_RESTART:
                if self.find_best_state(node.value, actions):
                    node = Node(self.find_best_state(node.value, actions))
                else:
                    break
            elif self.mode == Mode.STOCHASTIC:
                new_nodes = list(map(lambda x: Node(x), self.find_better_states(node.value, actions)))
                if len(new_nodes) > 0:
                    node = random.choice(new_nodes)
                else:
                    break
            elif self.mode == Mode.FIRST_CHOICE:
                if self.find_better_state(node.value, actions):
                    node = Node(self.find_better_state(node.value, actions))
                else:
                    break

        return node

    def solution(self):
        return self.problem.solution(self.problem.best_state)

    def find_best_state(self, state, actions):
        best_state = state
        for action in actions:
            new_state = self.problem.result(action, state)
            if self.problem.compute_cost(new_state) < self.problem.compute_cost(best_state):
                best_state = new_state
        return best_state

    def find_better_states(self, state, actions):
        for action in actions:
            new_state = self.problem.result(action, state)
            if self.problem.compute_cost(new_state) < self.problem.compute_cost(state):
                yield new_state

    def find_better_state(self, state, actions):
        for action in actions:
            new_state = self.problem.result(action, state)
            if self.problem.compute_cost(new_state) < self.problem.compute_cost(state):
                return new_state


class Mode(Enum):
    SIMPLE = auto()
    STOCHASTIC = auto()
    FIRST_CHOICE = auto()
    RANDOM_RESTART = auto()
