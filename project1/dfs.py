from problem import Problem


class Dfs(Problem):
    def __init__(self, graph, start, goal, tree_method=False):
        super(Dfs, self).__init__(graph, start, goal, tree_method)
        self.frontier = ([(start, [start])])
        self.visited = set()
        self.expanded = set()

    def search(self):
        while self.frontier:
            node, path = self.frontier.pop()
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