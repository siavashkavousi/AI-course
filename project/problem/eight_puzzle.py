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
        # return Node(tuple(value[:]), state, action)

    def is_goal(self, state):
        if state == self.goal_state:
            return True
        return False

    def compute_cost(self, current_node, parent_node):
        return 1

    def solution(self, goal_node):
        def traverse(node, path=[], cost=0):
            path.append('puzzle: {puzzle}, action: {action}, cost: {cost}'.format(
                puzzle=node.value, action=node.action, cost=cost
            ))
            if node.parent is None:
                return
            traverse(node.parent, path, cost + 1)

        path = []
        traverse(goal_node, path)
        return path

    def get_h(self, node):
        h = 0
        for i in node.value:
            current_idx = node.value.index(i)
            goal_idx = self.goal_node.value.index(i)
            h += abs(current_idx - goal_idx)
        return h
