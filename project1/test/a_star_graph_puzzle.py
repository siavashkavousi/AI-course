from unittest import TestCase
from problem.eight_puzzle import EightPuzzle
from solver.a_star import AStar
import time


class TestDfsGraphEightPuzzle(TestCase):
    def setUp(self):
        self.eight_puzzle = EightPuzzle()

    def test_solved(self):
        a_star = AStar(self.eight_puzzle)
        start_time = time.process_time()
        path = a_star.solve()
        finish_time = time.process_time()
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        if not a_star.tree_search:
            print('number of explored nodes: {count}'.format(count=len(a_star.explored)))
        print('maximum memory usage: {usage}'.format(usage=a_star.mem_count))