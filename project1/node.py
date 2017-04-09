class Node:
    def __init__(self, value, parent=None, action=None):
        self.value = value
        self.parent = parent
        self.action = action

    def __eq__(self, other):
        if isinstance(other, Node):
            if self.value == other.value:
                return True
            return False
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    # def __hash__(self):
    #     return hash(tuple(sorted(self.value)))
