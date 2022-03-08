class Node(object):

    def __init__(self,value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = Node(1) # Header
b = Node(2)
c = Node(3) #Trailer

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b 

# Could also implement circular linked list where c.next_node = a and a.prev_node = c

