from unittest import TestCase
from problem.romania_routes import RomaniaRoutes
from solver.dfs import Dfs


class TestDfsGraphRomaniaRoutes(TestCase):
    def setUp(self):
        self.romania_routes = RomaniaRoutes()

    def test_solved(self):
        dfs = Dfs(self.romania_routes, depth_limit=5)
        print(dfs.solve())
