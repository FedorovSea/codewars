import math
def reindeer(presents):
    try:
        if presents < 180:
            return math.ceil(presents / 30) + 2
    except ValueError('Error'):
        return 'Threw an error!'

print(reindeer(181))