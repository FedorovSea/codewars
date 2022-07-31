def sum_of_intervals(intervals):
    res = []
    for i in intervals:
        ranger = ''.join(str(i))
        a,b = ranger.split()
        a = a.lstrip('(').rstrip(',')
        b = b.rstrip(')')
        for ran in range(int(a)+1, int(b)+1):
            if ran not in res:
                res.append(ran)
    return len(res)