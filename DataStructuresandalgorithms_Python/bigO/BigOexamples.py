#O[1] constant
def func(values):
    return print(values[0])

lst = [1,2,3,4]
func(lst)


#O[n] linear
def fun_lin(lst):
    for val in lst:
        print(val)
    
fun_lin(lst)

#O[n^2] quadratic
def func_quad(lst):
    for item1 in lst:
        for item2 in lst:
            print (item1,item2)

func_quad(lst)

#Dropping insignificant terms
#Example1: O[n+n] = O[2n] = O[n]
def fun_lin1(lst):
    for val in lst:
        print(val)
    for val in lst:
        print(val)
    
fun_lin1(lst)

#Example2:  O(1 + n/2 + 10) = O(n)
def comp(lst):
    #### O[1]
    print (lst[0])

    #### O[n/2]
    midpoint = int(len(lst)/2)
    for val in lst[:midpoint]:
        print (val)

    #### O[10]
    for val in range(10):
        print ("Hello world")
    
comp(lst)

#Example3:  
def matcher(lst, match):

    for item in lst:
        if item == match:
            return print(True)
        return print(False)

matcher(lst,1) #Best case O(1) because first element
matcher(lst,5) #Worst case O(n) because may be last element

# Space complexity O(1) and time O(n)
# we only assign the 'hello world!' variable once, not every
# time we print. So the algorithm has O(1) space complexity and an O(n) time complexity.

def printer(n=10):
    '''
    Prints "hello world!" n times
    '''
    for x in range(n):
        print ('Hello World!')

printer()

# Space complexity O(n) and time O(n)
# the size of the new_list object scales with the input n, this shows that it is an O(n) algorithm with regards to space complexity.

def create_list(n):
    new_list = []
    
    for num in range(n):
        new_list.append('new')
    
    return new_list

print(create_list(5))