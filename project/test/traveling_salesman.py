from problem.traveling_salesman import TravelingSalesMan
from solver.anneal import Annealer, LinearMultiplicativeScheduler, LogarithmicMultiplicativeScheduler, \
    QuadraticMultiplicativeScheduler
from solver.hill_climbing import HillClimbing, Mode


def parse_distance_matrix(city_dm, num_cities):
    dm = city_dm.split(' ')
    if len(dm) < num_cities:
        raise Exception('Wrong number of distances, please enter distances equivalent to number of cities')
    return list(map(lambda x: int(x), dm[:num_cities]))


def print_annealer_solution(annealer):
    print('annealer with {cooling_scheduler} cooling scheduler'.format(cooling_scheduler=annealer.cooling_scheduler))
    print('number of created nodes: {n}'.format(n=annealer.num_of_created_nodes))
    print('number of expanded nodes: {n}'.format(n=annealer.num_of_expanded_nodes))
    print('solution: {solution}'.format(solution=annealer.solution()))


def print_hill_climbing_solution(hill_climbing):
    print('hill climbing in {mode} mode'.format(mode=hill_climbing.mode))
    print('number of created nodes: {n}'.format(n=hill_climbing.num_of_created_nodes))
    print('number of expanded nodes: {n}'.format(n=hill_climbing.num_of_expanded_nodes))
    print('solution: {solution}'.format(solution=hill_climbing.solution()))


if __name__ == '__main__':
    # num_cities = int(input('Please enter number of cities: '))
    # cities = [
    #     parse_distance_matrix(input('Enter distance matrix for city {number}: '.format(number=i)), num_cities)
    #     for i in range(num_cities)
    # ]

    num_cities = 5
    cities = [
        [0, 10, 5, 7, 4],
        [10, 0, 2, 3, 7],
        [5, 2, 0, 8, 8],
        [7, 3, 8, 0, 5],
        [4, 7, 8, 5, 0]
    ]

    traveling_sales_man = TravelingSalesMan(init_state=[i for i in range(num_cities)], dmatrix=cities)
    # Annealer
    annealer = Annealer(traveling_sales_man, LinearMultiplicativeScheduler(50))
    annealer.solve()
    print_annealer_solution(annealer)

    annealer = Annealer(traveling_sales_man, LogarithmicMultiplicativeScheduler(5))
    annealer.solve()
    print_annealer_solution(annealer)

    annealer = Annealer(traveling_sales_man, QuadraticMultiplicativeScheduler(5))
    annealer.solve()
    print_annealer_solution(annealer)

    # Hill climbing
    hill_climbing = HillClimbing(traveling_sales_man, mode=Mode.SIMPLE)
    hill_climbing.solve()
    print_hill_climbing_solution(hill_climbing)

    hill_climbing = HillClimbing(traveling_sales_man, mode=Mode.STOCHASTIC)
    hill_climbing.solve()
    print_hill_climbing_solution(hill_climbing)

    hill_climbing = HillClimbing(traveling_sales_man, mode=Mode.FIRST_CHOICE)
    hill_climbing.solve()
    print_hill_climbing_solution(hill_climbing)

    hill_climbing = HillClimbing(traveling_sales_man, mode=Mode.RANDOM_RESTART)
    hill_climbing.solve()
    print_hill_climbing_solution(hill_climbing)
