# Uses lists instead of your own Stack class.

class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        self.stack1.append(element)
        self.stack2 = self.stack1[::-1]
                
    
    def dequeue(self):        
        return self.stack2.pop()
        

"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q = Queue2Stacks()

for i in range(8):
    q.enqueue(i)
    
for i in range(8):
    print(q.dequeue())


#Method 2
print("Method2")

class Queue2Stacks1(object):
    
    def __init__(self):
        
        # Two Stacks
        self.instack = []
        self.outstack = []
     
    def enqueue(self,element):
        self.instack.append(element)
                
    
    def dequeue(self): 
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())       
        return self.outstack.pop()
        

"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q1 = Queue2Stacks1()

for i in range(10):
    q1.enqueue(i)
    
for i in range(10):
    print(q1.dequeue()) 