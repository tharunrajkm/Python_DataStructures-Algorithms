import timeit

# 3 methods of solving the problem are used

#Your function will accept a number n and return the nth number of the fibonacci sequence
# Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1.
# Else it returns fib(n-1)+fib(n-2).

##### Iteratively ######

# def fib_iter(n):
#     a,b = 0,1

#     for i in range(n):
#          a,b = b, a+b

#     return print(a) 

# start1 = timeit.default_timer()
# fib_iter(23)
# end1 = timeit.default_timer()
# time1 = end1- start1
# print(time1)



##### Recursively ######
# The recursive solution is exponential time Big-O , with O(2^n).

def fib_rec(n):
    # Base case
    if n == 0 or n == 1:
        return n

    # Recursive case
    else:
        return fib_rec(n-1) + fib_rec(n-2)

    

start2 = timeit.default_timer()
print(fib_rec(10))
end2 = timeit.default_timer()
time2 = end2- start2
print(time2)


# ##### Dynamically using Memotization ######

# n = 10
# chache = [None] * (n+1)


# def fib_dyn(n):

#     # Base Case
#     if n == 0 or n == 1:
#         return n

#     # Check Chache
#     if chache[n] != None:
#         print (n)
#         return chache[n]

#     chache[n] = fib_rec(n-1) + fib_rec(n-2)

#     print( chache)

#     return chache[n]


# # print(fib_dyn(8))
# # print(fib_dyn(2))
# # print(fib_dyn(3))
# # print(fib_dyn(3))
# # print(fib_dyn(10))