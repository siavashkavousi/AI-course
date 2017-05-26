from problem.problem import Problem
from math import sqrt, pow
from random import randint
from node import Node
from copy import copy


class TravelingSalesMan(Problem):
    def __init__(self, init_node=None):
        super().__init__()
        self.init_node = init_node
        self.best_node = self.init_node

    @property
    def init_node(self):
        return self._init_node

    @init_node.setter
    def init_node(self, node):
        if node is None:
            self._init_node = Node([City(randint(0, 30), randint(0, 30)) for _ in range(0, 10)])
        else:
            self._init_node = node

    def actions(self, node):
        for i in range(len(node.value)):
            for j in range(i + 1, len(node.value)):
                yield [i, j]

    def result(self, action, node):
        new_node = copy(node)
        position1, position2 = action
        cities = new_node.value
        cities[position1], cities[position2] = cities[position2], cities[position1]
        return new_node

    def compute_cost(self, node):
        distance = 0
        for start_city, target_city in zip(node.value, rotate(node.value, -1)):
            distance += start_city.distance(target_city)
        return distance

    def solution(self):
        print('best solution:')
        for city in self.best_node.value:
            print(city)
        print('distance: {distance}'.format(distance=self.compute_cost(self.best_node)))


class City(object):
    def __init__(self, x=randint(0, 30), y=randint(0, 30)):
        self.x = x
        self.y = y

    def distance(self, city):
        if isinstance(city, City):
            return sqrt(abs(pow(self.x - city.x, 2)) + abs(pow(self.y - city.y, 2)))
        raise Exception('argument is not an instance of City class')

    def __str__(self):
        return 'x: {x} and y: {y}'.format(x=self.x, y=self.y)


def rotate(l, n):
    return l[-n:] + l[:-n]
