from problem.problem import Problem
from solver.solver import Solver


class Genetic(Solver):
    def __init__(self, problem: Problem, population_size=10):
        super().__init__(problem)
        self.population_size = population_size
        self.population = self.create_init_population()

    def solve(self):
        while True:
            self.population = self.select()
            offsprings = self.cross_over()
            self.population = self.mutate_offsprings(offsprings)
            # self.population = self.select_new_population(offsprings)

    def select(self):
        self.population = sorted(self.population, key=self.eval_fitness)
        return self.population[:len(self.population) / 2]

    def cross_over(self):
        return [self.problem.cross_over(ind1, ind2) for ind1, ind2 in zip(self.population, self.population)]

    def mutate_offsprings(self, offsprings):
        return [self.problem.mutate(individual) for individual in offsprings]

    def select_new_population(self, offsprings):
        pass

    def create_init_population(self):
        return [self.problem.random_state for _ in range(self.population_size)]

    def eval_fitness(self, state):
        return self.problem.fitness(state)
