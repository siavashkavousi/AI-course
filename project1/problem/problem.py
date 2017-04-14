from abc import ABCMeta, abstractmethod


class Problem(object):
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
    def actions(self, node):
        pass

    @abstractmethod
    def result(self, action, node):
        pass

    @abstractmethod
    def is_goal(self, node):
        pass

    @abstractmethod
    def compute_cost(self, current_node=None, parent_node=None):
        pass

    @property
    @abstractmethod
    def goal_node(self):
        pass

    @goal_node.setter
    @abstractmethod
    def goal_node(self, node):
        pass

    @abstractmethod
    def solution(self, goal_node):
        pass

    @abstractmethod
    def get_h(self, node):
        pass
