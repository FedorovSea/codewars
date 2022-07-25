def abbreviate(s:str):
    word = ""
    sentence = []
    res_str = ''
    for i in s:
        if i.isalpha():
            word += i
        else:
            sentence.append(word)
            sentence.append(i)
            word = ""
            continue
    sentence.append(word)
    for word in sentence:
        if len(word) >= 4:
            res_str += word[:1] + str((len(word)-2)) + word[-1]
        else:
            res_str += word
    return res_str