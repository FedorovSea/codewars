def sort_by_bit(arr):
    return arr.sort(key=lambda x: (x.bit_count(), x))