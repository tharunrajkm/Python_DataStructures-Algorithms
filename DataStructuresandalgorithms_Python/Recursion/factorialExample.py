def fact(n):
    #Base case
    if n == 0:
        return 1

    #Recursion
    else:
        return n*fact(n-1)


print(fact(5)) 