import math
from abc import ABCMeta, abstractmethod
from random import random, choice

from node import Node
from problem.problem import BestCaseProblem
from solver.solver import Solver


class CoolingScheduler(object):
    __metaclass__ = ABCMeta

    def __init__(self, t0, a=0.8):
        self.t0 = t0
        self.a = a

    @abstractmethod
    def tn(self, n):
        pass


class ExponentialMultiplicativeScheduler(CoolingScheduler):
    def tn(self, n):
        return self.t0 - math.pow(self.a, n)

    def __str__(self):
        return 'Exponential Multiplicative Scheduler'


class LogarithmicMultiplicativeScheduler(CoolingScheduler):
    def tn(self, n):
        return self.t0 / (1 + self.a * math.log(1 + n))

    def __str__(self):
        return 'Logarithmic Multiplicative Scheduler'


class LinearMultiplicativeScheduler(CoolingScheduler):
    def tn(self, n):
        return self.t0 / (1 + self.a * n)

    def __str__(self):
        return 'Linear Multiplicative Scheduler'


class QuadraticMultiplicativeScheduler(CoolingScheduler):
    def tn(self, n):
        return self.t0 / (1 + self.a * math.pow(n, 2))

    def __str__(self):
        return 'Quadratic Multiplicative Scheduler'


class Annealer(Solver):
    def __init__(self, problem: BestCaseProblem, cooling_scheduler: CoolingScheduler, temperature=5000, threshold=1):
        super().__init__(problem)
        self.temperature = temperature
        self.threshold = threshold
        self.cooling_scheduler = cooling_scheduler

    def solve(self):
        n = 0
        node = Node(self.problem.init_state)

        while self.temperature > self.threshold:
            actions = list(self.problem.actions(node.value))
            new_node = Node(self.problem.result(choice(actions), node.value), node)
            self.num_of_created_nodes += 1

            # check if new node has a higher energy or not and if not randomly accept new node
            if self.acceptance_probability(self.problem.compute_cost(node.value),
                                           self.problem.compute_cost(new_node.value)) > random():
                self.num_of_expanded_nodes += 1
                node = new_node

            # keep best state
            if self.problem.compute_cost(node.value) < self.problem.compute_cost(self.problem.best_state):
                self.problem.best_state = node.value

            n += 1
            self.temperature = self.cooling_scheduler.tn(n)

    def solution(self):
        return self.problem.solution(self.problem.best_state)

    def print_solution(self):
        print('annealer with {cooling_scheduler} cooling scheduler'.format(cooling_scheduler=self.cooling_scheduler))
        print('number of created nodes: {n}'.format(n=self.num_of_created_nodes))
        print('number of expanded nodes: {n}'.format(n=self.num_of_expanded_nodes))
        print('solution: {solution}'.format(solution=self.solution()))

    def acceptance_probability(self, current_energy, new_energy):
        if new_energy < current_energy:
            return 1
        return math.exp((current_energy - new_energy) / self.temperature)
