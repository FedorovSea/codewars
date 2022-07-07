def strip_comments(strng, markers):
    spaces = strng.split('\n')
    res = []
    for char in spaces:
        for marker in markers:
            if marker in char:
                char = char[: char.find(marker)].rstrip()
        res.append(char)
    return '\n'.join(res)