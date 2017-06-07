from unittest import TestCase
from problem.romania_routes import RomaniaRoutes
from solver.bfs import Bfs
import time


class TestBfsTreeRomaniaRoutes(TestCase):
    def setUp(self):
        self.romania_routes = RomaniaRoutes()

    def test_solved(self):
        bfs = Bfs(self.romania_routes, tree_search=True)
        start_time = time.process_time()
        path = bfs.solve()
        finish_time = time.process_time()
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        if not bfs.tree_search:
            print('number of explored nodes: {count}'.format(count=len(bfs.closed_list)))
        print('maximum memory usage: {usage}'.format(usage=bfs.mem_count))
