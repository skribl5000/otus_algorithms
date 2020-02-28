# Complete Tree - дерево, во всех уровнях (кроме, возможно, последнего (не листья)) есть по 2  потомка
# Заполнение строгим образом
# Для нахождения детей: index*2 + 1, index*2 + 2
# Для нахождения родителя: floor((i-1)/2) - желательно иметь проверку на отрицательный индекс - нет родителя

# Heap - неубывающая пирамида - родитель всегда меньше/равен детям, важны только соотношшения ребенка и родителя
# BST - бинарное дерево поиска - один ребенок всегда меньше/равен, второй - всегда больше
import math

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def drown(arr, n, i):
    largest = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < n and arr[i] < arr[left_index]:
        largest = left_index
    if right_index < n and arr[largest] < arr[right_index]:
        largest = right_index
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        drown(arr, n, largest)


class Heap:
    def __init__(self, arr):
        self.n = len(arr)
        for i in range(self.n, -1, -1):
            drown(arr, self.n, i)
        # for i in range(n-1, 0, -1):
        self.heap = arr

    # def display(self):
    #     print(self.heap)
    def get_sort_array(self):
        array = self.heap
        l = self.n
        for i in range(l-1,0,-1):
            array[0], array[i] = array[i], array[0]
            drown(array, i, 0)
        # return array

hip = Heap(array)
