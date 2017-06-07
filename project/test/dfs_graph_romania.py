from unittest import TestCase
from problem.romania_routes import RomaniaRoutes
from solver.dfs import Dfs
import time


class TestDfsGraphRomaniaRoutes(TestCase):
    def setUp(self):
        self.romania_routes = RomaniaRoutes()

    def test_solved(self):
        dfs = Dfs(self.romania_routes, depth_limit=8)
        start_time = time.process_time()
        path = dfs.solve()
        finish_time = time.process_time()
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        if not dfs.tree_search:
            print('number of explored nodes: {count}'.format(count=len(dfs.closed_list)))
        print('maximum memory usage: {usage}'.format(usage=dfs.mem_count))