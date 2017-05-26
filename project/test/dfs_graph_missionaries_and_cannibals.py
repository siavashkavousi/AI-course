from unittest import TestCase
from problem.missionaries_and_cannibals import MissionariesAndCannibals
from solver.dfs import Dfs
import time


class TestDfsGraphMissionariesAndCannibals(TestCase):
    def setUp(self):
        self.instance = MissionariesAndCannibals()

    def test_solved(self):
        dfs = Dfs(self.instance, is_iterative=True)
        start_time = time.process_time()
        path = dfs.solve()
        finish_time = time.process_time()
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        if not dfs.tree_search:
            print('number of explored nodes: {count}'.format(count=len(dfs.explored)))
        print('maximum memory usage: {usage}'.format(usage=dfs.mem_count))