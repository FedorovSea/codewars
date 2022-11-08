def narcissistic( value ):
    lenght = len(str(value))
    res_value = sum(int(x) ** lenght for x in str(value))
    if value == res_value:
        return True
    else:
        return False
