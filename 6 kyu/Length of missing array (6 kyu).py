def get_length_of_missing_array(array_of_arrays):
    if array_of_arrays == 'null' or array_of_arrays == [] or len(array_of_arrays) == 0 or array_of_arrays == None:
        return 0
    len_arr = []
    for arr in array_of_arrays:
        if isinstance(arr, list) and len(arr) != 0:
            len_arr.append(len(arr))
        else:
            return 0
    len_arr = sorted(len_arr)
    count = len_arr[0]
    for num in len_arr:
        if num == count:
            count += 1
        else:
            return count