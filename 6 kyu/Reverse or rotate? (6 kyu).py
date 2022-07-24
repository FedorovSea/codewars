def rev_rot(strng, sz):
    k = 0
    res = ''
    for i in range(len(strng)//sz):
        new_strng = strng[k:sz+k]
        sum_el = sum((int(x)**3 for x in new_strng))
        if sum_el % 2 != 0:
            new_strng = new_strng[1:] + new_strng [:1]
        else:
            new_strng = ''.join(reversed(new_strng))
        res += new_strng
        k += sz
    return res