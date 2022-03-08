def insertion_sort(arr):
    for i in range(1, len(arr)):
        currentValue = arr[i]
        position = i
        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position - 1]
            position = position -1

        arr[position] = currentValue
    return print(arr)
    



arr =[3,5,4,6,8,1,2,12,41,25]
insertion_sort(arr)