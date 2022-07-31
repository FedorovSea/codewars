def sum_of_intervals(intervals):
    res = set()
    for start,stop in intervals:
        for el in range(start, stop):
            res.add(el)
    return len(res)
