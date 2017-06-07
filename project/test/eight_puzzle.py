import time

from problem.eight_puzzle import EightPuzzle
from solver.dfs import Dfs
from solver.a_star import AStar

if __name__ == '__main__':
    eight_puzzle = EightPuzzle(init_state=(1, 2, 3, 4, 5, 6, 7, 0, 8),
                               goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0))
    dfs = Dfs(eight_puzzle)
    start_time = time.process_time()
    path = dfs.solve()
    finish_time = time.process_time()
    for item in path:
        print(item)
    print('execution time: {time}'.format(time=finish_time - start_time))
    if not dfs.tree_search:
        print('number of expanded nodes: {count}'.format(count=len(dfs.closed_list)))
    print('maximum memory usage: {usage}'.format(usage=dfs.mem_count))
