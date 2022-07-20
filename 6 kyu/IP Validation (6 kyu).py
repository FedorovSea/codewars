def is_valid_IP(strng):
    if len(strng) == 0:
        return False
    strng = strng.split('.')
    if len(strng) != 4:
        return False
    for num in strng:
        if num.isdigit() != True:
            return False
        if len(num) >= 2 and num[0] == '0':
            return False
        if len(num) > 2 and int(num) == 0 or int(num) > 255:
            return False
    return True