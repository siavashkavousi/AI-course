from collections import deque

from node import Node
from problem.problem import GoalBaseProblem
from .solver import GoalBaseSolver


class Bfs(GoalBaseSolver):
    def __init__(self, problem: GoalBaseProblem, tree_search=False):
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
                new_node = Node(value=self.problem.result(action, node.value),
                                parent=node,
                                action=action,
                                depth=node.depth + 1,
                                g=node.g + self.problem.compute_cost(node.value))
                self.num_of_created_nodes += 1
                if self.problem.is_goal(new_node.value):
                    return self.solution(new_node)
                self.add_to_frontier(new_node)
            self.mem_count = max(self.mem_count, len(self.frontier) + len(self.closed_list))

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
