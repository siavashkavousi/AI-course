from unittest import TestCase
from problem.romania_routes import RomaniaRoutes
from solver.a_star import Astar


class TestBfsGraphRomaniaRoutes(TestCase):
    def setUp(self):
        self.romania_routes = RomaniaRoutes()

    def test_solved(self):
        a_star = Astar(self.romania_routes)
        print(a_star.solve())
