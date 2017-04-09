from collections import deque
from problem.problem import Problem


class Bfs(object):
    def __init__(self, problem: Problem, tree_search=False):
        self.problem = problem
        self.tree_search = tree_search
        self.frontier = deque([problem.init_node])
        self.expanded = []

    def next_node(self):
        return self.frontier.popleft()

    def add_to_frontier(self, node):
        if self.tree_search:
            self.frontier.append(node)
        else:
            if node in self.frontier:
                return
            elif node in self.expanded:
                return
            else:
                self.frontier.append(node)

    def add_to_explored(self, node):
        if node in self.expanded:
            return
        self.expanded.append(node)

    def solve(self):
        while self.frontier:
            node = self.next_node()
            if not self.tree_search:
                self.add_to_explored(node)

            for action in self.problem.actions(node):
                new_node = self.problem.result(action, node)
                if self.problem.is_goal(new_node):
                    return self.problem.solution(new_node)
                self.add_to_frontier(new_node)
