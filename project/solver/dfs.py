import math

from node import Node
from problem.problem import Problem
from .solver import Solver


class Dfs(Solver):
    def __init__(self, problem: Problem, tree_search=False, is_iterative=False, depth_limit=math.inf):
        super().__init__(problem, tree_search)
        self.depth_limit = depth_limit
        self.is_iterative = is_iterative
        self.frontier = [Node(problem.init_state)]
        self.closed_list = set()
        self.mem_count = 0

    def solve(self):
        if self.is_iterative:
            print('running problem on iterative deepening dfs using {method}'.format(method=self._method()))
            depth = 0
            found_solution = None
            while not found_solution:
                self.frontier = [Node(self.problem.init_state)]
                self.closed_list = set()
                found_solution = self.solve_in_depth(depth)
                depth += 1
            print('solution has found in depth: {depth} using {method}'.format(
                depth=depth - 1,
                method=self._method()
            ))
            return found_solution
        else:
            if self.depth_limit == math.inf:
                print('running problem on dfs using {method}'.format(method=self._method()))
            else:
                print('running problem on limited depth dfs using {method}'.format(method=self._method()))
            return self.solve_in_depth(self.depth_limit)

    def solve_in_depth(self, depth):
        while self.frontier:
            node = self.frontier.pop()
            if not self.tree_search:
                self.closed_list.add(node)

            for action in self.problem.actions(node):
                new_node = Node(self.problem.result(action, node),node,action, node.depth+1)
                if new_node.depth > depth:
                    return None
                else:
                    if self.problem.is_goal(new_node):
                        path = self.problem.solution(new_node)
                        return path
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
