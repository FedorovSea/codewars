def is_a_valid_message(message):
    number_list,strng = [],[]
    number = ''
    count = 0
    if message[0].isnumeric() == False:
        return False
    for i in message:
        if i.isnumeric():
            number += i
            strng.append(' ')
        else:
            strng.append(i)
            if len(number) >= 1:
                number_list.append(number)
                number = ''
    strng = ''.join(strng).split()
    for i in range(0,len(strng)):
        if len(strng[i]) == int(number_list[i]):
            count += 1
    if count == len(strng):
        return True
    return False