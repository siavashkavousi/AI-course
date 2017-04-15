from problem.problem import Problem
from node import Node
from heapq import heappush, heappop
from .solver import Solver


class AStar(Solver):
    def __init__(self, problem: Problem, tree_search=False):
        super().__init__(problem, tree_search)
        self.frontier = [Node(value=problem.init_node.value,
                              parent=problem.init_node.parent,
                              action=problem.init_node.action,
                              depth=problem.init_node.depth,
                              g=0,
                              h=0)]
        self.explored = set()
        self.mem_count = 0

    def solve(self):
        print('running problem on A* using {method}'.format(method=self._method()))
        while self.frontier:
            node = self.next_node()
            if self.problem.is_goal(node):
                return self.problem.solution(node)

            if not self.tree_search:
                self.explored.add(node)

            for action in self.problem.actions(node):
                new_node = self.problem.result(action, node)
                new_weighted_node = Node(new_node.value,
                                         new_node.parent,
                                         new_node.action,
                                         new_node.depth,
                                         node.g + self.problem.compute_cost(new_node, node),
                                         self.problem.get_h(new_node))
                self.add_to_frontier(new_weighted_node)
            self.mem_count = max(self.mem_count, len(self.frontier) + len(self.explored))

    def add_to_frontier(self, node):
        if not self.tree_search and node in self.explored:
            return

        for old_node in self.frontier:
            if node == old_node and node.f < old_node.f:
                self.frontier.remove(old_node)
                heappush(self.frontier, node)
                return
        heappush(self.frontier, node)

    def next_node(self):
        return heappop(self.frontier)
