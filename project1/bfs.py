from collections import deque


class Bfs(object):
    def __init__(self, graph, start, goal, tree_method=False):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.tree_method = tree_method
        self.frontier = deque([(start, [start])])
        self.visited = set()
        self.expanded = set()

    def is_goal(self, node):
        return node == self.goal

    def search(self):
        while self.frontier:
            node, path = self.frontier.popleft()
            if not self.tree_method:
                self.visited.add(node)
            # extracts node adjacents
            for next in self.unvisited_nodes(node, path):
                self.expanded.add(node)
                if self.is_goal(next):
                    yield path + [next]
                else:
                    self.frontier.append((next, path + [next]))

    def unvisited_nodes(self, node, path):
        if self.tree_method:
            return self.graph[node]
        else:
            return self.graph[node] - set(path)

    def shortest_path(self, paths):
        distances = list(map(lambda x: len(x), paths))
        return min(distances)
