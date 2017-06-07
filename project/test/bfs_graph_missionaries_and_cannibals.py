import time
from unittest import TestCase

from problem.missionaries_and_cannibals import MissionariesAndCannibals
from solver.bfs import Bfs


class TestBfsGraphMissionariesAndCannibals(TestCase):
    def setUp(self):
        self.instance = MissionariesAndCannibals()

    def test_solved(self):
        bfs = Bfs(self.instance)
        start_time = time.process_time()
        path = bfs.solve()
        finish_time = time.process_time()
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        if not bfs.tree_search:
            print('number of explored nodes: {count}'.format(count=len(bfs.closed_list)))
        print('maximum memory usage: {usage}'.format(usage=bfs.mem_count))
