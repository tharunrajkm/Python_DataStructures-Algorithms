class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(a.value)
print(c.nextnode.value)
print(b.nextnode.value)


class DoubleNode(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        self.prevnode = None

x = DoubleNode(1)
y = DoubleNode(2)
z = DoubleNode(3) 

x.nextnode = y
y.prevnode = x

y.nextnode = z
z.prevnode = y

print(x.value)
print(y.nextnode.value)
print(z.prevnode.value)