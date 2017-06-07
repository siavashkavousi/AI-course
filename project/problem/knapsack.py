from functools import reduce
from random import randint

import numpy as np

from problem.problem import GeneticProblem


class Knapsack(GeneticProblem):
    def __init__(self, weights, values, W, init_state=None):
        super().__init__(init_state)
        self.weights = weights
        self.values = values
        self.W = W

    def random_state(self):
        while True:
            weight = reduce(lambda x, y: x + y, np.random.choice([0, 1], size=len(self.weights)) * self.weights)
            if weight < self.W:
                return weight

    def actions(self, state):
        pass
        # for i in range(len(self.items)):
        #     for combination in itertools.combinations(self.items, i):
        #         if sum(combination) < self.weight:
        #             yield combination

    def result(self, action, state):
        pass
        # return action

    def compute_cost(self, state):
        pass

    def fitness(self, population):
        return reduce(lambda x, y: x + y, population)

    def mutate(self, population):
        return np.random.choice([0, 1], size=len(self.weights)) * population

    def cross_over(self, ind1, ind2):
        slice_index = randint(0, len(ind1))
        temp = ind1[0:slice_index]
        ind1[0:slice_index] = ind2[0:slice_index]
        ind2[0:slice_index] = temp

    def solution(self, state):
        pass

    def get_h(self, node):
        pass


class Item(object):
    def __init__(self, value, weight):
        # we assume we have no negative value or weight
        self.value = abs(value)
        self.weight = abs(weight)

    def __str__(self):
        return 'value: {value} and weight: {weight}'.format(value=self.value, weight=self.weight)
