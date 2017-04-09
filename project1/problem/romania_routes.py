from problem.problem import Problem
from node import Node


class RomaniaRoutes(Problem):
    def __init__(self, init_node=None, goal_node=None):
        self.graph = [
            Node(City('arad', [('zerind', 75), ('timisoara', 118), ('sibiu', 140)])),
            Node(City('vaslui', [('urziceni', 142), ('lasi', 92)])),
            Node(City('zerind', [('arad', 75), ('oradea', 71)])),
            Node(City('oradea', [('zerind', 71), ('sibiu', 151)])),
            Node(City('timisoara', [('arad', 118), ('lugoj', 111)])),
            Node(City('lugoj', [('timisoara', 111), ('mehadia', 70)])),
            Node(City('mehadia', [('lugoj', 70), ('dobreta', 75)])),
            Node(City('dobreta', [('mehadia', 75), ('craiova', 120)])),
            Node(City('craiova', [('dobreta', 120), ('pitesti', 138), ('rimnicu vilcea', 146)])),
            Node(City('pitesti', [('craiova', 138), ('bucharest', 101), ('rimnicu vilcea', 97)])),
            Node(City('rimnicu vilcea', [('pitesti', 97), ('sibiu', 80), ('craiova', 146)])),
            Node(City('sibiu', [('rimnicu vilcea', 80), ('fagaras', 99), ('arad', 140)])),
            Node(City('fagaras', [('sibiu', 99), ('bucharest', 211)])),
            Node(City('bucharest', [('fagaras', 211), ('pitesti', 101), ('giurgiu', 90), ('urziceni', 85)])),
            Node(City('giurgiu', [('bucharest', 90)])),
            Node(City('urziceni', [('bucharest', 85), ('hirsova', 98), ('vaslui', 142)])),
            Node(City('hirsova', [('urziceni', 98), ('eforie', 86)])),
            Node(City('eforie', [('hirsova', 86)])),
            Node(City('lasi', [('neamt', 87), ('vaslui', 92)])),
            Node(City('neamt', [('lasi', 87)])),
        ]
        self.init_node = init_node
        self.goal_node = goal_node

    @property
    def init_node(self):
        return self._init_node

    @init_node.setter
    def init_node(self, node):
        if node is None:
            self._init_node = self.graph[0]
        else:
            self._init_node = node

    def actions(self, node):
        adjacents = node.value.adjacents
        return adjacents

    def result(self, action, node):
        for adjacent in node.value.adjacents:
            if adjacent == action:
                new_node = self.find_node(adjacent[0])
                new_node = Node(new_node.value, node, action)
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
            self._goal_node = self.graph[11]
        else:
            self._goal_node = node

    def solution(self, goal_node):
        path = []
        self.traverse(goal_node, path)
        return path

    def traverse(self, node, path=[]):
        path.append(node.value.city_name)
        if node.parent is None:
            return
        self.traverse(node.parent, path)

    def find_node(self, city_name):
        for node in self.graph:
            if node.value.city_name == city_name:
                return node


class City:
    def __init__(self, city_name, adjacents):
        self.city_name = city_name
        self.adjacents = adjacents

    def __eq__(self, other):
        if isinstance(other, City):
            if self.city_name == other.city_name and self.adjacents == other.adjacents:
                return True
            return False
        return NotImplemented

    def __ne__(self, other):
        return not self == other
