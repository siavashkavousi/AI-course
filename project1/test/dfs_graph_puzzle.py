from unittest import TestCase
from problem.eight_puzzle import EightPuzzle
from solver.dfs import Dfs


class TestDfsGraphEightPuzzle(TestCase):
    def setUp(self):
        self.eight_puzzle = EightPuzzle()

    def test_solved(self):
        dfs = Dfs(self.eight_puzzle)
        print(dfs.solve())