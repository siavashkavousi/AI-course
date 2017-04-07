from unittest import TestCase
from bfs import Bfs


class TestBfsGraph(TestCase):
    def setUp(self):
        self.graph = {'A': {'B', 'C'},
                      'B': {'A', 'D', 'E'},
                      'C': {'A', 'F'},
                      'D': {'B'},
                      'E': {'B', 'F'},
                      'F': {'C', 'E'}}

    def test_search(self):
        bfs = Bfs(self.graph, 'A', 'F')
        self.assertListEqual([['A', 'C', 'F'], ['A', 'B', 'E', 'F']], list(bfs.search()))

    def test_visited(self):
        bfs = Bfs(self.graph, 'A', 'F')
        list(bfs.search())
        self.assertEqual(5, len(bfs.visited))

    def test_expanded(self):
        bfs = Bfs(self.graph, 'A', 'F')
        list(bfs.search())
        self.assertEqual(4, len(bfs.expanded))

    def test_shortest_path(self):
        bfs = Bfs(self.graph, 'A', 'F')
        self.assertEqual(3, bfs.shortest_path(list(bfs.search())))
