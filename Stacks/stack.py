class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return False if self.items else True

    def top(self):
        top = self.pop()
        self.push(top)
        return top

    def size(self):
        return len(self.items)

    def contains(self, value):
        temp = Stack()
        contain = False
        for i in range(self.size()):
            top = self.pop()
            temp.push(top)
            if top == value:
                contain = True
                break

        for i in range(temp.size()):
            top = temp.pop()
            self.push(top)

        return contain