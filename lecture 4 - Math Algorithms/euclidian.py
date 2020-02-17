# Алгоритм нахождения наибольшего общего делителя
import time

start_time = time.time()


def euclidian(a, b):
    while a != 0 and b!= 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a or b


print(euclidian(1234567890, 12))
print("Время выполнения:", time.time() - start_time)
