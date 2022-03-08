# This interview question requires you to reverse a string using recursion. Make sure to think of the base case here.

def reverse(s):

    #Base case
    if len(s) <= 1:
        return s 

    #Recursion
    else:
        return reverse(s[1:]) + s[0]





print(reverse('abc'))
print(reverse('hello world'))