def is_twinprime(n):
    if n <= 2:
        return False
    pred = is_prime(n-2)
    next = is_prime(n+2)
    n = is_prime(n)
    if n and (pred or next):
        return True
    else: return False

def is_prime(n):
    d = 2
    while d * d <= n and n%d != 0:
        d += 1
    return d * d > n