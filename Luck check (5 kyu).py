def luck_check(string):
    rang = int(len(string)/2)
    if len(string)%2 == 0:
        return sum(int(x) for x in string[:int(rang)]) == sum(int(z) for z in string[:int(rang-1):-1])
    else:
        return sum(int(x) for x in string[:int(rang)]) == sum(int(z) for z in string[:int(rang):-1])
