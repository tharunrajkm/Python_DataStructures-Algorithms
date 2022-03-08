from numpy import array


def seq_search(arr, ele):
    pos = 0
    found = False
    
    while pos < len(arr) and found == False:
        if arr[pos] == ele:
            found = True
        else:
            pos += 1

    return found


arr = [1,9,2,8,3,4,7,5,6]   

# print(seq_search(arr,1))
# print(seq_search(arr,10))


def ordered_seq_search(arr,ele):
   
   # Sequential search for an Ordered list
    pos = 0

    # Target becomes true if ele is in the list
    found = False

    # Stop marker
    stopped = False

    while pos < len(arr) and not found and not stopped:
        if arr[pos] == ele:
            found = True
        else:
            if arr[pos] > ele :
                stopped = True
            else:
                pos += 1
    return print(found) 

arr.sort() 

ordered_seq_search(arr,3)
ordered_seq_search(arr,1.5)
