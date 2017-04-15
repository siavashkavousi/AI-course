from collections import deque
from problem.problem import Problem
from .solver import Solver


class Bidirectional(Solver):
    def __init__(self, problem: Problem, tree_search=False):
        super().__init__(problem, tree_search)
        self.frontier_start = deque([problem.init_node])
        self.frontier_end = deque([problem.goal_node])
        self.explored_start = set()
        self.explored_end = set()
        self.mem_count = 0

    def solve(self):
        print('running problem on bidirectional bfs using {method}'.format(method=self._method()))
        while self.frontier_start and self.frontier_end:
            if self.frontier_start:
                node = self.next_node(self.frontier_start)
                if not self.tree_search:
                    self.explored_start.add(node)

                for action in self.problem.actions(node):
                    new_node = self.problem.result(action, node)
                    self.add_to_frontier(self.frontier_start, self.explored_start, new_node)

            if self.frontier_end:
                node = self.next_node(self.frontier_end)
                if not self.tree_search:
                    self.explored_end.add(node)

                for action in self.problem.actions(node):
                    new_node = self.problem.result(action, node)
                    self.add_to_frontier(self.frontier_end, self.explored_end, new_node)

            self.mem_count = max(self.mem_count,
                                 len(self.frontier_start) +
                                 len(self.frontier_end) +
                                 len(self.explored_start) +
                                 len(self.explored_end))
            common_nodes = self.has_intersection()
            if common_nodes:
                return self.solution(common_nodes)

    def add_to_frontier(self, frontier, explored, node):
        if self.tree_search:
            frontier.append(node)
        else:
            if node in frontier:
                return
            elif node in explored:
                return
            else:
                frontier.append(node)

    def next_node(self, frontier):
        return frontier.popleft()

    def has_intersection(self):
        for start_node in self.frontier_start:
            for end_node in self.frontier_end:
                if start_node == end_node:
                    return [start_node, end_node]
        return None

    def solution(self, nodes):
        start_path = self.problem.solution(nodes[0])
        start_path = start_path[::-1]
        end_path = self.problem.solution(nodes[1])
        return start_path + end_path
