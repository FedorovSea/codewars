def take_while (seq, is_even):
    current_seq = []
    for char in seq:
        if is_even(char) == True:
            current_seq.append(char)
        else:
            return current_seq
    return current_seq