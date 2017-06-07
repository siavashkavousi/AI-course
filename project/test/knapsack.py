import numpy as np

from problem.knapsack import Knapsack, Item

if __name__ == '__main__':
    # num_items = int(input('Please enter number of cities: '))
    # items = [
    #     parse_distance_matrix(input('Enter distance matrix for city {number}: '.format(number=i)), num_items)
    #     for i in range(num_items)
    # ]

    num_items = 5
    weights = [10, 12, 3, 6, 9]
    values = [12, 14, 9, 12, 14]
    W = 25

    items = [Item(value, weight) for value, weight in zip(values, weights)]
    knapsack = Knapsack(items, W)
