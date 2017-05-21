from problem.traveling_salesman import TravelingSalesMan
from solver.anneal import Annealer

if __name__ == '__main__':
    traveling_sales_man = TravelingSalesMan()
    annealer = Annealer(traveling_sales_man)
    annealer.solve()
