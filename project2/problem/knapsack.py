from random import randint

from node import Node
from problem.problem import Problem


class Knapsack(Problem):
    def __init__(self, init_node=None, weight=50):
        super().__init__()
        self.init_node = init_node
        self.best_node = self.init_node
        self.weight = weight

    @property
    def init_node(self):
        return self._init_node

    @init_node.setter
    def init_node(self, node):
        if node is None:
            self._init_node = Node([Item(randint(0, 30), randint(0, 15)) for _ in range(0, 10)])
        else:
            self._init_node = node

    def actions(self, node):
        pass

    def result(self, action, node):
        pass

    def compute_cost(self, node):
        pass

    def solution(self):
        pass


class Item(object):
    def __init__(self, value, weight):
        # we assume we have no negative value or weight
        self.value = abs(value)
        self.weight = abs(weight)

    def __str__(self):
        return 'value: {value} and weight: {weight}'.format(value=self.value, weight=self.weight)
