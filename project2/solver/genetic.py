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
            self.mutate_offsprings(offsprings)
            self.population = self.select_new_population(offsprings)

    def select(self):
        self.population = sorted(self.population, key=self.eval_fitness)
        return self.population[:len(self.population) / 2]

    def cross_over(self):
        return [self.problem.cross_over() for _ in self.population]

    def mutate_offsprings(self, offsprings):
        for individual in offsprings:
            individual.mutate()

    def select_new_population(self, offsprings):
        pass

    def create_init_population(self):
        return [self.problem.init_node for _ in range(self.population_size)]

    def eval_fitness(self, node):
        return self.problem.fitness(node)
        # return reduce(lambda x, y: x.value + y.value, node.value)
