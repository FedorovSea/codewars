def decode(r:str):
    new_str = r.lstrip('0123456789')
    number = r[:-len(new_str)]

    res_str = ''
    for letter in new_str:
        index = ord(letter) - ord('a')
        found = False
        for num in range(0, 26):
            if num * int(number) % 26 == index:
                if found:
                    return "Impossible to decode"
                else:
                    res_str += chr(97 + num)
                    found = True
        if not found:
            return "Impossible to decode"

    return res_str