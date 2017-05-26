from abc import ABCMeta, abstractmethod


class Problem(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.best_node = None

    @property
    @abstractmethod
    def init_node(self):
        pass

    @init_node.setter
    @abstractmethod
    def init_node(self, node):
        pass

    @abstractmethod
    def actions(self, node):
        pass

    @abstractmethod
    def result(self, action, node):
        pass

    @abstractmethod
    def compute_cost(self, node):
        pass

    @abstractmethod
    def solution(self):
        pass


class GeneticProblem(Problem):
    __metaclass__ = ABCMeta

    @abstractmethod
    def cross_over(self):
        pass

    @abstractmethod
    def mutate(self):
        pass
