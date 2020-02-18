test_array = [10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,6,11,24,10,1,1,5,7,8,1,2,3,6]

def buble_sort(arr):
    # O(n^2)
    counter = 0
    swaps = 0
    swapped = False
    while swapped == False:
        #O(n)
        swapped = True
        for k in range(1,len(arr)):
            # O(n)
            if arr[k-1] > arr[k]:
                arr[k-1],arr[k] = arr[k],arr[k-1]
                swapped = False
                swaps += 1
            counter += 1
    return f'Array: {arr} \nIterrations: {counter} \nSwaps: {swaps}'



def selection_sort(arr):
    # O(n*(n-1)/2) => O(n^2)
    # O(n) for memory
    counter = 0
    swaps = 0
    for k in range(len(arr)):
        # O(n)
        min = k
        for i in range(k+1,len(arr)):
            # n -> 1
            if arr[i] < arr[min]:
                min = i
                swaps += 1
            counter += 1
        if k != min:
            arr[k],arr[min] = arr[min], arr[k]
    return f'Array: {arr} \nIterrations: {counter} \nSwaps: {swaps}'

def insertion_sort(arr):
    # O(n^2)
    # O(n^2) for memory
    counter = 0
    swaps = 0
    for i in range(len(arr)):
        # O(n)
        # i - length of sorted array
        x = arr[i]
        j = i - 1
        while arr[j] > x and j >=0:
            arr[j+1] = arr[j]
            j = j - 1
            counter += 1
            swaps += 1
        arr[j+1] = x
    return f'Array: {arr} \nIterrations: {counter} \nSwaps: {swaps}'

def shell_sort(arr):
    # we will use insertion_sort because it works better for almost sorted arrays
    counter = 0
    swaps = 0
    return f'Array: {arr} \nIterrations: {counter} \nSwaps: {swaps}'


print(buble_sort(test_array.copy()))
print(selection_sort(test_array.copy()))
print(insertion_sort(test_array.copy()))
print('')
# for almost done list insertion_sort sort works better than others
print(buble_sort([1,2,10,4,5,6,7]))
print(selection_sort([1,2,10,4,5,6,7]))
print(insertion_sort([1,2,10,4,5,6,7]))
