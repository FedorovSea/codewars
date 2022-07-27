def compute_sum(n):
    res_sum = 0
    if n < 10:
        return sum(range(0,n+1))
    else:
        res_sum += sum(range(0,10))
        for num in range(10,n+1):
            for el in str(num):
                res_sum += int(el)
    return res_sum