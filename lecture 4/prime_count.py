import math
import time
# Проверка числа на простоту

# просто проверка на наличие делителей от 1 до n
def is_prime(number):
    for i in range(2,number):
        if number % i ==0:
            return False
    return True

# только до корня из n, т.к. все, что выше будет иметь делитель
def is_prime_sq(number):
    for i in range(2,int(math.sqrt(number))+1):
        if number % i ==0:
            return False
    return True

# только нечетные, т.к. четные имеют делитель 2
def is_prime_odd(number):
    for i in range(4 , number,2):
        if number % i == 0:
            return False
    return True

# Тест на время
def test_prime_method(method, n):
    start_time = time.time()
    counter = 0
    for i in range(1, n+1):
        if method(i):
            counter += 1
    total_time = time.time() - start_time
    return str(method), counter, total_time

print(test_prime_method(is_prime, 50000))
print(test_prime_method(is_prime_sq, 50000))
print(test_prime_method(is_prime_odd, 50000))
