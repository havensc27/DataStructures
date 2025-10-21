class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        popped_value = self.items.pop()
        return popped_value

    def empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def top(self):
        top_item = self.pop()
        self.push(top_item)
        return top_item

    def size(self):
        return len(self.items)

    def contains(self, checked_number):
        stack = Stack()
        result = False
        for i in range(self.size()):
            popped_value = self.pop()
            self.push(popped_value)
            if popped_value == checked_number:
                result = True
                break
        for i in range(self.size()):
            self.push(self.pop())
        return result












