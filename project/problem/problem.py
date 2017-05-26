from abc import ABCMeta, abstractmethod


class Problem(object):
    __metaclass__ = ABCMeta

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
    def solution(self, goal_node):
        pass

    @abstractmethod
    def get_h(self, node):
        pass


class GoalBaseProblem(Problem):
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def init_node(self):
        pass

    @init_node.setter
    @abstractmethod
    def init_node(self, node):
        pass

    @abstractmethod
    def is_goal(self, node):
        pass

    @property
    @abstractmethod
    def goal_node(self):
        pass

    @goal_node.setter
    @abstractmethod
    def goal_node(self, node):
        pass


class BestCaseProblem(Problem):
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def random_node(self):
        pass

    @property
    @abstractmethod
    def best_node(self):
        pass

    @best_node.setter
    @abstractmethod
    def best_node(self, node):
        pass


class GeneticProblem(BestCaseProblem):
    __metaclass__ = ABCMeta

    @abstractmethod
    def cross_over(self):
        pass

    @abstractmethod
    def mutate(self):
        pass
