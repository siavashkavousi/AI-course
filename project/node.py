class Node(object):
    def __init__(self, value, parent=None, action=None, depth=0, g=None, h=None):
        self.value = value
        self.parent = parent
        self.action = action
        self.depth = depth
        self.h = h
        self.g = g
        self.f = g + h

    def __eq__(self, other):
        if isinstance(other, Node):
            if self.value == other.value:
                return True
            return False
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, Node):
            if self.value == other.value:
                if self.f and self.f < other.f:
                    return True
                if self.g and self.g < other.g:
                    return True
            return False
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Node):
            if self.value == other.value:
                if self.f and self.f > other.f:
                    return True
                if self.g and self.g > other.g:
                    return True
            return False
        return NotImplemented

    def __hash__(self):
        return hash(self.value)
