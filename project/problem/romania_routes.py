from problem.problem import GoalBaseProblem


class RomaniaRoutes(GoalBaseProblem):
    def __init__(self, init_state, goal_state, graph):
        super().__init__(init_state, goal_state)
        self.graph = graph
        self.next_city = None

    def actions(self, state):
        return state.neighbors

    def result(self, action, state):
        city_name, __ = action
        self.next_city = city_name
        for neighbor in state.neighbors:
            if neighbor == action:
                for city in self.graph:
                    if city.match_city(city_name):
                        return city

    def is_goal(self, state):
        if state == self.goal_state:
            return True
        return False

    def compute_cost(self, state):
        return state.calc_distance_to(self.next_city)

    def solution(self, state):
        return {
            'city': state.city_name,
        }

    def get_h(self, state):
        return 112


class City:
    def __init__(self, city_name, neighbors):
        self.city_name = city_name
        self.neighbors = neighbors

    def match_city(self, city_name):
        if self.city_name == city_name:
            return True
        return False

    def calc_distance_to(self, city_name):
        for neighbor in self.neighbors:
            if city_name == neighbor[0]:
                return neighbor[1]

    def __eq__(self, other):
        if isinstance(other, City):
            if self.city_name == other.city_name:
                return True
            return False
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.city_name)
