from collections import deque

from node import Node
from problem.problem import GoalBaseProblem
from .solver import GoalBaseSolver


class Bidirectional(GoalBaseSolver):
    def __init__(self, problem: GoalBaseProblem, tree_search=False):
        super().__init__(problem, tree_search)
        self.frontier_start = deque([Node(problem.init_state)])
        self.frontier_end = deque([Node(problem.goal_state)])
        self.closed_list_start = set()
        self.closed_list_end = set()
        self.mem_count = 0

    def solve(self):
        print('running problem on bidirectional bfs using {method}'.format(method=self._method()))
        while self.frontier_start and self.frontier_end:
            if self.frontier_start:
                node = self.frontier_start.popleft()
                if not self.tree_search:
                    self.closed_list_start.add(node)

                for action in self.problem.actions(node.value):
                    new_node = Node(value=self.problem.result(action, node.value),
                                    parent=node,
                                    action=action,
                                    depth=node.depth + 1,
                                    g=node.g + self.problem.compute_cost(node.value))
                    self.num_of_created_nodes += 1
                    self.add_to_frontier(self.frontier_start, self.closed_list_start, new_node)

            if self.frontier_end:
                node = self.frontier_end.popleft()
                if not self.tree_search:
                    self.closed_list_end.add(node)

                for action in self.problem.actions(node.value):
                    new_node = Node(value=self.problem.result(action, node.value),
                                    parent=node,
                                    action=action,
                                    depth=node.depth + 1,
                                    g=node.g + self.problem.compute_cost(node.value))
                    self.num_of_created_nodes += 1
                    self.add_to_frontier(self.frontier_end, self.closed_list_end, new_node)

            self.mem_count = max(self.mem_count,
                                 len(self.frontier_start) +
                                 len(self.frontier_end) +
                                 len(self.closed_list_start) +
                                 len(self.closed_list_end))
            common_nodes = self.has_intersection()
            if common_nodes:
                return self._solution(common_nodes)

    def add_to_frontier(self, frontier, closed_list, node):
        if self.tree_search:
            frontier.append(node)
            self.num_of_expanded_nodes += 1
        else:
            if node in frontier:
                return
            elif node in closed_list:
                return
            else:
                frontier.append(node)
                self.num_of_created_nodes += 1

    def has_intersection(self):
        for start_node in self.frontier_start:
            for end_node in self.frontier_end:
                if start_node == end_node:
                    return [start_node, end_node]
        return None

    def _solution(self, nodes):
        start_path = self.solution(nodes[0])
        start_path = start_path[::-1]
        end_path = self.solution(nodes[1])
        return start_path + end_path
