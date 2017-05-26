from abc import ABCMeta, abstractmethod


class Problem(object):
    __metaclass__ = ABCMeta

    def __init__(self, init_state):
        self.init_state = init_state

    @abstractmethod
    def actions(self, state):
        pass

    @abstractmethod
    def result(self, action, state):
        pass

    @abstractmethod
    def compute_cost(self, state):
        pass

    @abstractmethod
    def solution(self, state):
        pass

    @abstractmethod
    def get_h(self, node):
        pass


class GoalBaseProblem(Problem):
    __metaclass__ = ABCMeta

    def __init__(self, init_state, goal_state):
        super().__init__(init_state)
        self.goal_state = goal_state

    @abstractmethod
    def is_goal(self, node):
        pass


class BestCaseProblem(Problem):
    __metaclass__ = ABCMeta

    def __init__(self, init_state):
        super().__init__(init_state)
        self.best_state = init_state

    @abstractmethod
    def get_h(self, node):
        pass


class GeneticProblem(BestCaseProblem):
    __metaclass__ = ABCMeta

    @abstractmethod
    def cross_over(self):
        pass

    @abstractmethod
    def mutate(self):
        pass
