# Method 1

#TS = O(n) because runtime grows linearly with input size
def sum1(x):
    sum = 0
    for i in range(x+1):
        sum += i
    print(sum)
    return sum

sum1(10)

# sum(from o to n) : n(n+1)/2
# Take an input of n and return the sum of the numbers from 0 to n

# Method 2 

def sum2(x):
    sum = x*(x+1)/2
    print(int(sum))
    return sum

sum2(10)
