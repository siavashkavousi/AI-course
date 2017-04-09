class Node:
    def __init__(self, value, parent=None, action=None, depth=0):
        self.value = value
        self.parent = parent
        self.action = action
        self.depth = depth

    def __eq__(self, other):
        if isinstance(other, Node):
            # if self.parent and self.parent == other.parent and self.value == other.value:
            #     return True
            # elif self.value == other.value:
            #     return True
            if self.value == other.value:
                return True
            return False
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    # def __hash__(self):
    #     return hash(tuple(sorted(self.value)))
