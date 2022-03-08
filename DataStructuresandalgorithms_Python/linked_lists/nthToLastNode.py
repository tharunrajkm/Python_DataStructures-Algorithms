class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None


def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n-1):
        #edge case: 
        if not right_pointer.nextnode: # nextnode is None
            return LookupError("Error: n is larger than the linked list.") 
        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode: #Until not None
        
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer
    


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

target_node = nth_to_last_node(2, a) 

print(target_node.value)