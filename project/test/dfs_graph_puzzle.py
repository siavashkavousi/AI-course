from unittest import TestCase
from problem.eight_puzzle import EightPuzzle
from solver.dfs import Dfs
import time


class TestDfsGraphEightPuzzle(TestCase):
    def setUp(self):
        self.eight_puzzle = EightPuzzle()

    def test_solved(self):
        dfs = Dfs(self.eight_puzzle)
        start_time = time.process_time()
        path = dfs.solve()
        finish_time = time.process_time()
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        if not dfs.tree_search:
            print('number of explored nodes: {count}'.format(count=len(dfs.closed_list)))
        print('maximum memory usage: {usage}'.format(usage=dfs.mem_count))