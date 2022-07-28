def what_century(year):
    if year[2:] == '00':
        th = year[:2]
    else:
        th = year[:2]
        th = str(int(th) + 1)
    if int(th) < 20 and int(th) > 10:
        ending = 'th'
    else:
        if th[1] == '1':
            ending = 'st'
        elif th[1] == '2':
            ending = 'nd'
        elif th[1] == '3':
            ending = 'rd'
        else:
            ending = 'th'
    return th + ending