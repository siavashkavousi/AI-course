from unittest import TestCase
from problem.eight_puzzle import EightPuzzle
from problem.romania_routes import RomaniaRoutes
from solver.bidirectional import Bidirectional
import time


class TestBidirectionalGraphEightPuzzle(TestCase):
    def setUp(self):
        self.eight_puzzle = EightPuzzle()
        self.instance = RomaniaRoutes()

    def test_solved(self):
        bidirectional = Bidirectional(self.eight_puzzle)
        start_time = time.process_time()
        path = bidirectional.solve()
        finish_time = time.process_time()
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        if not bidirectional.tree_search:
            print('number of explored nodes: {count}'.format(
                count=len(bidirectional.explored_start) + len(bidirectional.explored_end)))
            print('maximum memory usage: {usage}'.format(usage=bidirectional.mem_count))
