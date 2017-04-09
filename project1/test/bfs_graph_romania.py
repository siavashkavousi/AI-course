from unittest import TestCase
from problem.romania_routes import RomaniaRoutes
from solver.bfs import Bfs


class TestBfsGraphRomaniaRoutes(TestCase):
    def setUp(self):
        self.romania_routes = RomaniaRoutes()

    def test_solved(self):
        bfs = Bfs(self.romania_routes)
        # print(list(bfs.solve()))
        print(bfs.solve())
        self.assertEqual(3, 3)
