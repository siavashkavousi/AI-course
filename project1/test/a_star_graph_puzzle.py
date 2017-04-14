from unittest import TestCase
from problem.eight_puzzle import EightPuzzle
from solver.a_star import Astar


class TestDfsGraphEightPuzzle(TestCase):
    def setUp(self):
        self.eight_puzzle = EightPuzzle()

    def test_solved(self):
        a_star = Astar(self.eight_puzzle)
        print(a_star.solve())
