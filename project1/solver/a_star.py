from problem.problem import Problem
from weighted_node import HNode
from heapq import heappush, heappop


class Astar(object):
    def __init__(self, problem: Problem, tree_search=False):
        self.problem = problem
        self.tree_search = tree_search
        self.frontier = [HNode(problem.init_node.value,
                               problem.init_node.parent,
                               problem.init_node.action,
                               problem.init_node.depth)]
        self.expanded = []

    def next_node(self):
        return heappop(self.frontier)

    def add_to_frontier(self, node):
        if not self.tree_search and node in self.expanded:
            return

        for old_node in self.frontier:
            if node == old_node and node.f < old_node.f:
                self.frontier.remove(old_node)
                heappush(self.frontier, node)
                return
        heappush(self.frontier, node)

    def add_to_explored(self, node):
        if node in self.expanded:
            return
        self.expanded.append(node)

    def solve(self):
        while self.frontier:
            node = self.next_node()
            if self.problem.is_goal(node):
                return self.problem.solution(node)

            if not self.tree_search:
                self.add_to_explored(node)

            for action in self.problem.actions(node):
                new_node = self.problem.result(action, node)
                new_weighted_node = HNode(new_node.value,
                                          new_node.parent,
                                          new_node.action,
                                          new_node.depth,
                                          node.g + self.problem.compute_cost(new_node, node),
                                          self.problem.get_h(new_node))
                self.add_to_frontier(new_weighted_node)
