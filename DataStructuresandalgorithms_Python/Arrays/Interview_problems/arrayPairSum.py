# #Given an integer array, output all the unique pairs that sum up to a specific value k.
# So the input:
# pair_sum([1,3,2,2],4)
# would return 2 pairs:
#  (1,3)
#  (2,2)
# NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS

def pair_sum(arr,k):
    counter = 0
    lookup = set()

    for i in arr:
        if (k - i) in lookup:
            counter += 1
        else:
            lookup.add(i)

    return counter

#Method 2
# O(N) because linear and for each element we check whether the k-element is the set of seen numbers. then we pair sum and add to output.
#Insert and find operations of a set are both O(1), so in total O(N) time complexity

def pair_sum1(arr,k):

    #checking edge case
    if len(arr)<2:
        return print('error')

    seen = set()
    output = set()

    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target),max(num,target)))

    print(output)
    print(seen)

    #print ('\n'.join(map(str,list(output))))

    return len(output)
    


# print(pair_sum([1,3,5,6,2,2],4))
# print(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))

print(pair_sum1([1,3,2,2],4))
#print(pair_sum1([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))