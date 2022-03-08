# Direct method can use Itertools library in python




def permute(s):

    out  = []
    
    print('s is ',s)

    #Base case
    if len(s) == 1:
        out = [s]



    #Recursion
    else:
        for i, let in enumerate(s):
            
            #print(i, let, out)
            for perm in permute(s[:i]+s[i+1:]):
                
                print('the perm is ', perm)
                #print('1st out' , out)

                out += [let+perm]
                print('2nd out' , out)

    return out

print(permute('abc'))
