# Возведение в степень

# SIMPLE POW O(n)
def pow(n, degree):
    if degree == 1:
        return n
    return n * pow(n, degree-1)

print(pow(2, 8))

# FAST POW O(log(n))
def fast_pow_recurse(n, degree):
    if degree == 1:
        return n
    if degree % 2 == 0:
        n = n * n
        return pow(n, degree/2)
    else:
        return n * pow(n, degree - 1)

print(fast_pow_recurse(2,8))

def fast_pow_loop(n, degree):
    result = 1
    while degree > 1:
        if degree % 2 == 1:
            result*= n
        else:
            n *= n
        degree /= 2;
    if degree > 0:
        result *= n
    return result

print(fast_pow_loop(2, 8))
