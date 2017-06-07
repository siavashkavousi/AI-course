from collections import deque

from node import Node
from problem.problem import Problem
from .solver import Solver


class Bfs(Solver):
    def __init__(self, problem: Problem, tree_search=False):
        super().__init__(problem, tree_search)
        self.frontier = deque([Node(problem.init_state)])
        self.closed_list = set()
        self.mem_count = 0

    def solve(self):
        print('running problem on bfs using {method}'.format(method=self._method()))
        while self.frontier:
            node = self.frontier.popleft()
            if not self.tree_search:
                self.closed_list.add(node)

            for action in self.problem.actions(node):
                new_node = Node(self.problem.result(action, node), node, action)
                if self.problem.is_goal(new_node):
                    return self.problem.solution(new_node)
                self.add_to_frontier(new_node)
            self.mem_count = max(self.mem_count, len(self.frontier) + len(self.closed_list))

    def solution(self):
        return self.problem.solution()

    def add_to_frontier(self, node):
        if self.tree_search:
            self.frontier.append(node)
        else:
            if node in self.frontier:
                return
            elif node in self.closed_list:
                return
            else:
                self.frontier.append(node)
