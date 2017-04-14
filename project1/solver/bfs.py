from collections import deque
from problem.problem import Problem
from .solver import Solver


class Bfs(Solver):
    def __init__(self, problem: Problem, tree_search=False):
        super().__init__(problem, tree_search)
        self.frontier = deque([problem.init_node])
        self.explored = set()

    def solve(self):
        print('running problem on bfs using {method}'.format(method=self._method()))
        while self.frontier:
            node = self.next_node()
            if not self.tree_search:
                self.explored.add(node)

            for action in self.problem.actions(node):
                new_node = self.problem.result(action, node)
                if self.problem.is_goal(new_node):
                    return self.problem.solution(new_node)
                self.add_to_frontier(new_node)

    def add_to_frontier(self, node):
        if self.tree_search:
            self.frontier.append(node)
        else:
            if node in self.frontier:
                return
            elif node in self.explored:
                return
            else:
                self.frontier.append(node)

    def next_node(self):
        return self.frontier.popleft()
