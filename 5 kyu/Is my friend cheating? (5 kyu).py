def remov_nb(n):
    res = []
    sum_arr = n * (n+1) // 2
    for i in range(1, n+1):
        j = (sum_arr-i) // (i + 1)
        if j <= n and i*j == (sum_arr - i - j):
            res.append((i,j))
    return res