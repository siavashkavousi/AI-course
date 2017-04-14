from unittest import TestCase
from problem.missionaries_and_cannibals import MissionariesAndCannibals
from solver.bfs import Bfs


class TestBfsGraphMissionariesAndCannibals(TestCase):
    def setUp(self):
        self.instance = MissionariesAndCannibals()

    def test_solved(self):
        bfs = Bfs(self.instance)
        print(bfs.solve())
