import time
from unittest import TestCase

from problem.romania_routes import RomaniaRoutes
from solver.a_star import AStar


class TestBfsGraphRomaniaRoutes(TestCase):
    def setUp(self):
        self.romania_routes = RomaniaRoutes()

    def test_solved(self):
        a_star = AStar(self.romania_routes)
        start_time = time.process_time()
        path = a_star.solve()
        finish_time = time.process_time()
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        if not a_star.tree_search:
            print('number of explored nodes: {count}'.format(count=len(a_star.closed_list)))
        print('maximum memory usage: {usage}'.format(usage=a_star.mem_count))
