def luck_check(string):
    rang = int(len(string)/2)
    return sum(map(int, string[:rang])) == sum(map(int, string[-rang:]))




