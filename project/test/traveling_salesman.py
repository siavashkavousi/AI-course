from problem.traveling_salesman import TravelingSalesMan
from solver.anneal import Annealer, ExponentialMultiplicativeScheduler
from solver.hill_climbing import HillClimbing, Mode

if __name__ == '__main__':
    traveling_sales_man = TravelingSalesMan()
    annealer = Annealer(traveling_sales_man, ExponentialMultiplicativeScheduler(5000))
    hill_climbing = HillClimbing(traveling_sales_man, mode=Mode.SIMPLE)
    annealer.solve()
    hill_climbing.solve()
