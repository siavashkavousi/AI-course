from heapq import heappush, heappop

from node import Node
from problem.problem import Problem
from .solver import GoalBaseSolver


class UniformCost(GoalBaseSolver):
    def __init__(self, problem: Problem, tree_search=False):
        super().__init__(problem, tree_search)
        self.frontier = [Node(value=problem.init_state, g=0)]
        self.closed_list = set()
        self.mem_count = 0

    def solve(self):
        print('running problem on uniform cost using {method}'.format(method=self._method()))
        while self.frontier:
            node = heappop(self.frontier)
            if self.problem.is_goal(node):
                return self.solution(node)

            if not self.tree_search:
                self.closed_list.add(node)

            for action in self.problem.actions(node.value):
                new_node = Node(value=self.problem.result(action, node.value),
                                parent=node,
                                action=action,
                                depth=node.depth + 1,
                                g=node.g + self.problem.compute_cost(node.value))
                self.num_of_created_nodes += 1
                self.add_to_frontier(new_node)
            self.mem_count = max(self.mem_count, len(self.frontier) + len(self.closed_list))

    def add_to_frontier(self, node):
        if not self.tree_search and node in self.closed_list:
            return

        for old_node in self.frontier:
            if node == old_node and node.g < old_node.g:
                self.frontier.remove(old_node)
                heappush(self.frontier, node)
                self.num_of_expanded_nodes += 1
                return
        heappush(self.frontier, node)
        self.num_of_expanded_nodes += 1
