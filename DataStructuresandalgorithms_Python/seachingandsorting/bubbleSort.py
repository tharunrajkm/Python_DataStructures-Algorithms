def bubble_sort(arr):
    # For every element (arranged backwards)
    for i in range(len(arr)-1, 0,-1):
        print(i)
        for k in range(i):
            # If we come to a point to switch
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    return arr






arr = [3,2,13,4,6,5,7,8,1,20]
print(bubble_sort(arr))