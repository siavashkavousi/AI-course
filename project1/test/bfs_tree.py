from unittest import TestCase
from bfs import Bfs


class TestBfsTree(TestCase):
    def setUp(self):
        self.tree = {'A': {'B', 'C'},
                     'B': {'D', 'E'},
                     'C': {'F'},
                     'D': {},
                     'E': {}}

    def test_search(self):
        bfs = Bfs(self.tree, 'A', 'F', tree_method=True)
        self.assertListEqual([['A', 'C', 'F']], list(bfs.search()))

    def test_expanded(self):
        bfs = Bfs(self.tree, 'A', 'F', tree_method=True)
        list(bfs.search())
        self.assertEqual(3, len(bfs.expanded))
