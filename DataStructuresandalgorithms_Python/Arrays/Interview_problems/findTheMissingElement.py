"""Consider an array of non-negative integers. A second array is formed by shuffling the elements of the 
first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
Input:
finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:
5 is the missing number
"""

import collections #for adding a default python dictionary


#my solution O(NlogN)
def finder(arr1,arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    for i in range(len(arr1)):
        print(i)
        if arr1[i] == arr2[i]:
            print(i)
        else:
            print("{} is the missing number".format(arr1[i]))
            break
    pass


#finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
#finder([1,2,4,5,6,7],[7,2,1,4,6])
#finder([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1])






# method udemy 1 O(NlogN)
# Using zip function
def finder1(arr1,arr2):
    arr1.sort()
    arr2.sort()
    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
        
    return arr1[-1] #last element


# print(finder1([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
# print(finder1([1,2,4,5,6,7],[7,2,1,4,6]))
# print(finder1([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))







# method udemy 2 using hash table linear time complexity for interviews
# Two for loops O(2N) = O(N)
# Using default python dictionary
def finder2(arr1,arr2):
    # Using default dict to avoid key errors
    d = collections.defaultdict(int) #takes  in integers
    for num2 in arr2:
        d[num2] += 1

    for num1 in arr1:
        if d[num1] == 0:
            return num1
        else:
            d[num1] -= 1
    
    
# print(finder2([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
# print(finder2([1,2,4,5,6,7],[7,2,1,4,6]))
# print(finder2([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))




# method udemy 4 using XOR function, linar time O(N) complexity

# By performing a very clever trick, we can achieve linear time and constant space complexity without any problems.
# Here it is: initialize a variable to 0, then XOR every element in the first and second arrays with that variable.
# In the end, the value of the variable is the result, missing element in array2.

def finder3(arr1,arr2):
    result = 0

    for num in arr1+arr2:
        result ^= num

    return result

print(finder3([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
# print(finder3([1,2,4,5,6,7],[7,2,1,4,6]))
# print(finder3([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]))
























