
class Node:
    __slots__ = ('value', 'next')

    def __init__(self, value, next = None):
        self.value = value
        self.next = next
