from node import Node


class WeightedNode(Node):
    def __init__(self, value, parent=None, action=None, depth=0, g=0):
        super().__init__(value, parent, action, depth)
        self.g = g

    def set(self, node):
        self.value = node.value
        self.parent = node.parent
        self.action = node.action
        self.depth = node.depth

    def __eq__(self, other):
        if isinstance(other, WeightedNode):
            # if self.parent and self.parent == other.parent and self.value == other.value:
            #     return True
            # elif self.value == other.value:
            #     return True
            # if self.value == other.value and self.g == other.g:
            if self.value == other.value:
                return True
            return False
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, WeightedNode):
            if self.value == other.value and self.g < other.g:
                return True
            return False
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, WeightedNode):
            if self.value == other.value and self.g > other.g:
                return True
            return False
        return NotImplemented

        # def __hash__(self):
        #     return hash(tuple(sorted(self.value)))
