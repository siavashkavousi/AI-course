from copy import copy

from problem.problem import BestCaseProblem
from utils import rotate


class TravelingSalesMan(BestCaseProblem):
    def __init__(self, init_state, dmatrix):
        super().__init__(init_state)
        self.dmatrix = dmatrix

    def actions(self, state):
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                yield [i, j]

    def result(self, action, state):
        position1, position2 = action
        new_state = copy(state)
        new_state[position1], new_state[position2] = new_state[position2], new_state[position1]
        return new_state

    def compute_cost(self, state):
        distance = 0
        for start_city, target_city in zip(state, rotate(state, -1)):
            distance += self.dmatrix[start_city][target_city]
        return distance

    def solution(self, state):
        return {
            'cities': state,
            'distance': self.compute_cost(state)
        }

    def get_h(self, node):
        pass
