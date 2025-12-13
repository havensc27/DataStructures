class Queue:
    def __init__(self):
        self.deque = None
        self.items = []

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return True if self.items else False

    def look(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def __contains__(self, temp):
        found = False
        for i in range(self.size()):
            b = self.dequeue()
            if b == temp:
                found = True
            self.enqueue(b)
        return found


