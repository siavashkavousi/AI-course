import time

from problem.romania_routes import RomaniaRoutes, City
from solver.a_star import AStar
from solver.bfs import Bfs
from solver.dfs import Dfs

if __name__ == '__main__':
    graph = [
        City('arad', [('zerind', 75), ('timisoara', 118), ('sibiu', 140)]),
        City('vaslui', [('urziceni', 142), ('lasi', 92)]),
        City('zerind', [('arad', 75), ('oradea', 71)]),
        City('oradea', [('zerind', 71), ('sibiu', 151)]),
        City('timisoara', [('arad', 118), ('lugoj', 111)]),
        City('lugoj', [('timisoara', 111), ('mehadia', 70)]),
        City('mehadia', [('lugoj', 70), ('dobreta', 75)]),
        City('dobreta', [('mehadia', 75), ('craiova', 120)]),
        City('craiova', [('dobreta', 120), ('pitesti', 138), ('rimnicu vilcea', 146)]),
        City('pitesti', [('craiova', 138), ('bucharest', 101), ('rimnicu vilcea', 97)]),
        City('rimnicu vilcea', [('pitesti', 97), ('sibiu', 80), ('craiova', 146)]),
        City('sibiu', [('rimnicu vilcea', 80), ('fagaras', 99), ('arad', 140)]),
        City('fagaras', [('sibiu', 99), ('bucharest', 211)]),
        City('bucharest', [('fagaras', 211), ('pitesti', 101), ('giurgiu', 90), ('urziceni', 85)]),
        City('giurgiu', [('bucharest', 90)]),
        City('urziceni', [('bucharest', 85), ('hirsova', 98), ('vaslui', 142)]),
        City('hirsova', [('urziceni', 98), ('eforie', 86)]),
        City('eforie', [('hirsova', 86)]),
        City('lasi', [('neamt', 87), ('vaslui', 92)]),
        City('neamt', [('lasi', 87)]),
    ]
    romania_routes = RomaniaRoutes(init_state=graph[0], goal_state=graph[1], graph=graph)

    a_star = AStar(romania_routes)
    start_time = time.process_time()
    path = a_star.solve()
    finish_time = time.process_time()
    for item in path:
        print(item)
    print('execution time: {time}'.format(time=finish_time - start_time))
    print('number of created nodes: {count}'.format(count=a_star.num_of_created_nodes))
    print('number of expanded nodes: {count}'.format(count=a_star.num_of_expanded_nodes))
    print('maximum memory usage: {usage}'.format(usage=a_star.mem_count))
    print()

    bfs = Bfs(romania_routes, tree_search=True)
    start_time = time.process_time()
    path = bfs.solve()
    finish_time = time.process_time()
    for item in path:
        print(item)
    print('execution time: {time}'.format(time=finish_time - start_time))
    print('number of created nodes: {count}'.format(count=bfs.num_of_created_nodes))
    print('number of expanded nodes: {count}'.format(count=bfs.num_of_expanded_nodes))
    print('maximum memory usage: {usage}'.format(usage=bfs.mem_count))
    print()

    dfs = Dfs(romania_routes, depth_limit=3)
    start_time = time.process_time()
    path = dfs.solve()
    finish_time = time.process_time()
    if path is None:
        print('solution in depth: {depth} was not found, try deeper!'.format(depth=8))
    else:
        for item in path:
            print(item)
        print('execution time: {time}'.format(time=finish_time - start_time))
        print('number of created nodes: {count}'.format(count=dfs.num_of_created_nodes))
        print('number of expanded nodes: {count}'.format(count=dfs.num_of_expanded_nodes))
        print('maximum memory usage: {usage}'.format(usage=dfs.mem_count))
        print()
