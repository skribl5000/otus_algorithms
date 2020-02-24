import timeit
test_array = [10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,10,3,6,10,15,22,1,6,11,24,10,1,1,5,7,8,1,2,3,6,6,11,24,10,1,1,5,7,8,1,2,3,6]

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
    # print(f'Array: {arr} \nIterrations: {counter} \nSwaps: {swaps}')
    return arr

def shell_sort(arr):
    # we will use insertion_sort because it works better for almost sorted arrays
    counter = 0
    swaps = 0

    step = len(arr)//2
    for i in range(step, 0 , -1):
        temp = insertion_sort([arr[k] for k in range(0,len(arr),i)])
        a = 0
        for k in range(0,len(arr), i):
            arr[k] = temp[a]
            a+= 1
            if isinstance(arr[k], str):
                print(arr[k])
    return f'Array: {arr} \nIterrations: {counter} \nSwaps: {swaps}'



# чет долгий shell вышел, взял код с wiki, все равно insert получется быстрее.
def shellSort(array):
	increment = len(array) // 2
	while increment > 0:

		for startPosition in range(increment):
			gapInsertionSort(array, startPosition, increment)


		increment //= 2

def gapInsertionSort(array, low, gap):

	for i in range(low + gap, len(array), gap):
		currentvalue = array[i]
		position = i

		while position >= gap and array[position - gap] > currentvalue:
			array[position] = array[position - gap]
			position = position - gap

		array[position] = currentvalue



print('Buble:')
print(timeit.timeit("buble_sort(test_array)", setup="from __main__ import buble_sort, test_array", number=1))
print('Select:')
print(timeit.timeit("selection_sort(test_array)", setup="from __main__ import selection_sort, test_array", number=1))
print('Insert:')
print(timeit.timeit("insertion_sort(test_array)", setup="from __main__ import insertion_sort, test_array", number=1))
print('Shell:')
print(timeit.timeit("shell_sort(test_array)", setup="from __main__ import shell_sort, test_array", number=1))
print('Shell Wiki:')
print(timeit.timeit("shellSort(test_array)", setup="from __main__ import shellSort, test_array", number=1))
