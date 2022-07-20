def pascals_triangle(n):
    triangle = []
    for i in range(1, n + 1):
        term = 1
        for j in range(1, i + 1):
            triangle.append(term)
            term = term * (i - j) // j
    return triangle

    #Решение для n <= 5
    # triangle = ''
    # for i in range(0, n):
    #     triangle += str(11**int(i))
    # return list((map(int, triangle)))