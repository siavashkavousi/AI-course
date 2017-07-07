from functools import reduce

from problem.problem import GoalBaseProblem


class EightPuzzle(GoalBaseProblem):
    def __init__(self, init_state=None, goal_state=None):
        super().__init__(init_state, goal_state)

    def actions(self, state):
        index = state.index(0)
        if index == 0:
            return 'right', 'down'
        elif index == 1:
            return 'left', 'right', 'down'
        elif index == 2:
            return 'left', 'down'
        elif index == 3:
            return 'right', 'up', 'down'
        elif index == 4:
            return 'left', 'right', 'up', 'down'
        elif index == 5:
            return 'left', 'up', 'down'
        elif index == 6:
            return 'right', 'up'
        elif index == 7:
            return 'left', 'right', 'up'
        elif index == 8:
            return 'left', 'up'

    def result(self, action, state):
        zero_idx = state.index(0)
        repr_idx = None
        if action == 'left':
            repr_idx = zero_idx - 1
        elif action == 'right':
            repr_idx = zero_idx + 1
        elif action == 'up':
            repr_idx = zero_idx - 3
        elif action == 'down':
            repr_idx = zero_idx + 3

        repr_value = state[repr_idx]

        value = list(state)
        value[repr_idx] = 0
        value[zero_idx] = repr_value
        return tuple(value[:])

    def is_goal(self, state):
        if state == self.goal_state:
            return True
        return False

    def compute_cost(self, state):
        return 1

    def solution(self, state):
        return {
            'puzzle': state,
        }

    def get_h(self, state):
        return reduce(lambda x, y: x + y, map(lambda i: abs(state.index(i) - self.goal_state.index(i)), state))
