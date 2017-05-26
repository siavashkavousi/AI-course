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
            self._init_node = Node((1, 2, 3, 4, 5, 6, 7, 0, 8))
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

        value = list(node.value)
        value[repr_idx] = 0
        value[zero_idx] = repr_value
        return Node(tuple(value[:]), node, action)

    def is_goal(self, node):
        if node.value == self.goal_node.value:
            return True
        return False

    def compute_cost(self, current_node, parent_node):
        return 1

    @property
    def goal_node(self):
        return self._goal_node

    @goal_node.setter
    def goal_node(self, node):
        if node is None:
            self._goal_node = Node((1, 2, 3, 4, 5, 6, 7, 8, 0))
        else:
            self._goal_node = node

    def solution(self, goal_node):
        def traverse(node, path=[], cost=0):
            path.append('puzzle: {puzzle}, action: {action}, cost: {cost}'.format(
                puzzle=node.value, action=node.action, cost=cost
            ))
            if node.parent is None:
                return
            traverse(node.parent, path, cost + 1)

        path = []
        traverse(goal_node, path)
        return path

    def get_h(self, node):
        h = 0
        for i in node.value:
            current_idx = node.value.index(i)
            goal_idx = self.goal_node.value.index(i)
            h += abs(current_idx - goal_idx)
        return h
