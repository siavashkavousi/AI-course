from problem.problem import Problem
import math


class Dfs(object):
    def __init__(self, problem: Problem, tree_search=False, is_iterative=False, depth_limit=math.inf):
        self.problem = problem
        self.tree_search = tree_search
        self.depth_limit = depth_limit
        self.is_iterative = is_iterative
        self.frontier = [problem.init_node]
        self.expanded = []

    def next_node(self):
        return self.frontier.pop()

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
        if self.is_iterative:
            depth = 0
            found_solution = None
            while not found_solution:
                self.frontier = [self.problem.init_node]
                self.expanded = []
                found_solution = self.solve_in_depth(depth)
                depth += 1
            return found_solution
        else:
            return self.solve_in_depth(self.depth_limit)

    def solve_in_depth(self, depth):
        while self.frontier:
            node = self.next_node()
            if not self.tree_search:
                self.add_to_explored(node)

            for action in self.problem.actions(node):
                new_node = self.problem.result(action, node)
                if new_node.depth > depth:
                    return None
                else:
                    if self.problem.is_goal(new_node):
                        return self.problem.solution(new_node)
                self.add_to_frontier(new_node)
