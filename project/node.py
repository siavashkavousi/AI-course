class Node(object):
    def __init__(self, value, parent=None, action=None, depth=0, g=None, h=None):
        self.depth = depth
        self.action = action
        self.parent = parent
        self.h = h
        self.g = g
        self.value = value
        self.f = [g, h]

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        if value[0] and value[1]:
            self._f = value[0] + value[1]
        else:
            self._f = None

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
