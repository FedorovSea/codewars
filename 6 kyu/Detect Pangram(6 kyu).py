def is_pangram(s):
#used dict, because since I recently used it
    count = 0
    dict_1 = {'a':'1', 'b':'2', 'c':'3', 'd': '4', 'e': '5', 'f':'6', 'g':'7', 'h':'8', 'i':'9',
               'j':'10', 'k': '11', 'l':'12', 'm':'13', 'n':'14','o':'15','p':'16', 'q':'17','r':'18',
               's':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'}
    for letter in s:
        if letter in dict_1:
            count += 1
            dict_1.pop(letter)
    if count == 26:
        return True
    else:
        return False
