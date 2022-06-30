import math


def reindeer(presents):
    if presents > 180:
        raise ValueError()
    return math.ceil(presents / 30) + 2



print(reindeer(181))