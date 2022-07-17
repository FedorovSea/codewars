def is_twinprime(n):
    if n <= 2:
        return False
    pred = n - 2
    next = n + 2
    if is_prime(pred) and is_prime(n) or is_prime(next) and is_prime(n):
        return True
    else:
        return False

def is_prime(n):
    d = 2
    while d * d <= n and n%d != 0:
        d += 1
    return d * d > n
