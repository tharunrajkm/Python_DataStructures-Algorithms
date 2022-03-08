class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueque(self,item):
        self.items.insert(0,item)

    def dequeque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()

print(q.isEmpty())

q.enqueque(1)
q.enqueque("one")
q.enqueque("T")

print(q.size())

print(q.items)

print(q.dequeque())

print(q.items)

print(q.dequeque())

print(q.items)

print(q.dequeque())

print(q.isEmpty())