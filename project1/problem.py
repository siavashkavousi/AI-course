from abc import ABCMeta, abstractmethod


class Problem(object):
    __metaclass__ = ABCMeta

    def __init__(self, graph, start, goal, tree_method=False):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.tree_method = tree_method

    def is_goal(self, node):
        return node == self.goal

    @abstractmethod
    def search(self):
        pass

    def shortest_path(self, paths):
        paths = list(map(lambda x: (len(x), x), paths))
        return min(paths, key=lambda x: x[0])
