from problem.problem import Problem
from node import Node


class EightPuzzle(Problem):
    def __init__(self, init_node=None, goal_node=None):
        self.init_node = init_node
        self.goal_node = goal_node

    @property
    def init_node(self):
        return self._init_node

    @init_node.setter
    def init_node(self, node):
        if node is None:
            self._init_node = Node([1, 2, 3, 4, 5, 0, 7, 8, 6])
        else:
            self._init_node = node

    def actions(self, node):
        index = node.value.index(0)
        if index == 0:
            return 'right', 'down'
        elif index == 1:
            return 'left', 'right', 'down'
        elif index == 2:
            return 'left', 'down'
        elif index == 3:
            return 'right', 'up', 'down'
        elif index == 4:
            return 'left', 'right', 'up', 'down'
        elif index == 5:
            return 'left', 'up', 'down'
        elif index == 6:
            return 'right', 'up'
        elif index == 7:
            return 'left', 'right', 'up'
        elif index == 8:
            return 'left', 'up'

    def result(self, action, node):
        zero_idx = node.value.index(0)
        repr_idx = None
        if action == 'left':
            repr_idx = zero_idx - 1
        elif action == 'right':
            repr_idx = zero_idx + 1
        elif action == 'up':
            repr_idx = zero_idx - 3
        elif action == 'down':
            repr_idx = zero_idx + 3

        repr_value = node.value[repr_idx]

        new_node = Node(node.value[:], node, action)
        new_node.value[repr_idx] = 0
        new_node.value[zero_idx] = repr_value
        return new_node

    def is_goal(self, node):
        if node.value == self.goal_node.value:
            return True
        return False

    def compute_cost(self):
        pass

    @property
    def goal_node(self):
        return self._goal_node

    @goal_node.setter
    def goal_node(self, node):
        if node is None:
            self._goal_node = Node([1, 2, 3, 4, 5, 6, 7, 8, 0])
        else:
            self._goal_node = node

    def solution(self, goal_node, path=[]):
        def traverse(node, path=[]):
            if node.parent is None:
                return
            path.append(node.action)
            traverse(node.parent, path)

        path = []
        traverse(goal_node, path)
        return path
