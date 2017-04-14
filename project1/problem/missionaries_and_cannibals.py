from problem.problem import Problem
from node import Node


class MissionariesAndCannibals(Problem):
    def __init__(self, init_node=None, goal_node=None):
        self.init_node = init_node
        self.goal_node = goal_node

    @property
    def init_node(self):
        return self._init_node

    @init_node.setter
    def init_node(self, node):
        if node is None:
            self._init_node = Node(Map(3, 3, 0, 0))
        else:
            self._init_node = node

    def actions(self, node):
        def possible_actions(map):
            return [
                Map(map.left_missionaries - 2, map.left_cannibals,
                    map.right_missionaries + 2, map.right_cannibals),
                Map(map.left_missionaries, map.left_cannibals - 2,
                    map.right_missionaries, map.right_cannibals + 2),
                Map(map.left_missionaries - 1, map.left_cannibals - 1,
                    map.right_missionaries + 1, map.right_cannibals + 1),
                Map(map.left_missionaries - 1, map.left_cannibals,
                    map.right_missionaries + 1, map.right_cannibals),
                Map(map.left_missionaries, map.left_cannibals - 1,
                    map.right_missionaries, map.right_cannibals + 1),
            ]

        def is_valid(container):
            if container.left_missionaries >= 0 and container.right_missionaries >= 0 \
                    and container.left_cannibals >= 0 and container.right_cannibals >= 0 \
                    and (container.left_missionaries == 0 or container.left_missionaries >= container.left_cannibals) \
                    and (container.right_missionaries == 0 or container.right_cannibals >= container.right_cannibals):
                return True
            else:
                return False

        if node.value.boat == 'left':
            for possible_action in possible_actions(node.value):
                if is_valid(possible_action):
                    possible_action.boat = 'right'
                    yield possible_action
        else:
            for possible_action in possible_actions(node.value):
                if is_valid(possible_action):
                    yield possible_action

    def result(self, action, node):
        return Node(action, node)

    def is_goal(self, node):
        if node.value == self.goal_node.value:
            return True
        return False

    def compute_cost(self, current_node, parent_node):
        pass

    @property
    def goal_node(self):
        return self._goal_node

    @goal_node.setter
    def goal_node(self, node):
        if node is None:
            self._goal_node = Node(Map(0, 0, 3, 3))
        else:
            self._goal_node = node

    def solution(self, goal_node):
        def traverse(node, path=[]):
            path.append(str(node.value))
            if node.parent is None:
                return
            traverse(node.parent, path)

        path = []
        traverse(goal_node, path)
        return path

    def get_h(self, node):
        pass


class Map:
    def __init__(self, left_missionaries, left_cannibals, right_missionaries, right_cannibals, boat='left'):
        self.right_cannibals = right_cannibals
        self.right_missionaries = right_missionaries
        self.boat = boat
        self.left_cannibals = left_cannibals
        self.left_missionaries = left_missionaries

    def __eq__(self, other):
        if isinstance(other, Map):
            if self.left_missionaries == other.left_missionaries \
                    and self.left_cannibals == other.left_cannibals \
                    and self.right_missionaries == other.right_missionaries \
                    and self.right_cannibals == other.right_cannibals:
                return True
            return False
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((self.left_missionaries, self.left_cannibals,
                     self.boat, self.right_missionaries, self.right_cannibals))

    def __str__(self):
        return 'm={ml} and c={cl} - boat={boat} - m={mr} and c={cr}'.format(
            ml=self.left_missionaries,
            cl=self.left_cannibals,
            mr=self.right_missionaries,
            cr=self.right_cannibals,
            boat=self.boat,
        )
