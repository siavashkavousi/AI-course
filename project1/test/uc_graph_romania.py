from unittest import TestCase
from problem.romania_routes import RomaniaRoutes
from solver.uniform_cost import UniformCost
import time


class TestUcGraphRomaniaRoutes(TestCase):
    def setUp(self):
        self.romania_routes = RomaniaRoutes()

    def test_solved(self):
        uc = UniformCost(self.romania_routes)
        start_time = time.process_time()
        path = uc.solve()
        finish_time = time.process_time()
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        if not uc.tree_search:
            print('number of explored nodes: {count}'.format(count=len(uc.explored)))
        print('maximum memory usage: {usage}'.format(usage=uc.mem_count))