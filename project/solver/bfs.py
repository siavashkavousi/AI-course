from collections import deque

from node import Node
from problem.problem import Problem
from .solver import GoalBaseSolver


class Bfs(GoalBaseSolver):
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

            for action in self.problem.actions(node.value):
                new_node = Node(self.problem.result(action, node.value), node, action, node.depth + 1)
                self.num_of_created_nodes += 1
                if self.problem.is_goal(new_node.value):
                    return self.solution(new_node)
                self.add_to_frontier(new_node)
            self.mem_count = max(self.mem_count, len(self.frontier) + len(self.closed_list))

    def solution(self, goal_node):
        def traverse(node, path=[], cost=0):
            self.problem.solution(node.value)
            path.append('action: {action}, cost: {cost}'.format(action=node.action, cost=cost))
            if node.parent is None:
                return
            traverse(node.parent, path, cost + self.problem.compute_cost(node.value))

        path = []
        traverse(goal_node, path)
        return path

    def add_to_frontier(self, node):
        if self.tree_search:
            self.frontier.append(node)
            self.num_of_expanded_nodes += 1
        else:
            if node in self.frontier:
                return
            elif node in self.closed_list:
                return
            else:
                self.frontier.append(node)
                self.num_of_expanded_nodes += 1
