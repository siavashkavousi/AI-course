from unittest import TestCase
from problem.missionaries_and_cannibals import MissionariesAndCannibals
from solver.dfs import Dfs


class TestDfsGraphMissionariesAndCannibals(TestCase):
    def setUp(self):
        self.instance = MissionariesAndCannibals()

    def test_solved(self):
        dfs = Dfs(self.instance, is_iterative=True)
        print(dfs.solve())
