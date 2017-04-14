from unittest import TestCase
from problem.romania_routes import RomaniaRoutes
from solver.uniform_cost import UniformCost


class TestUcGraphRomaniaRoutes(TestCase):
    def setUp(self):
        self.romania_routes = RomaniaRoutes()

    def test_solved(self):
        uc = UniformCost(self.romania_routes)
        print(uc.solve())
