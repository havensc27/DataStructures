class Node:
    def __init__(self, val):
        self.value = val
        self.left_child = None
        self.right_child = None

    def set_left(self, n):
        self.left_child = n

    def set_right(self, n):
        self.right_child = n

    def set_value(self, val):
        self.value = val

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

    def get_value(self):
        return self.value

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

    def __str__(self):
        s = "{" + str(self.get_value())
        if self.get_left() != None:
            s = s + ", Left: " +  str(self.get_left())
        if self.get_right() != None:
            s = s + ", Right: " +  str(self.get_right())
        s = s + "}"
        return s

class BinaryTree:
    def __init__(self, n):
        self.root = n

    def get_root(self):
        return self.root

    def __str__(self):
        return "Tree: " + str(self.get_root())