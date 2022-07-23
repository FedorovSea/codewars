def increment_string(strng):
    word = strng.rstrip('1234567890')
    numbers = strng[len(word):]

    if len(numbers) == 0:
        return strng + '1'
    else:
        length = len(numbers)
        new_numbers = 1 + int(numbers)
        new_numbers = str(new_numbers).zfill(length)
        return word + new_numbers
