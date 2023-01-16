def find_even_index(arr):
    for a in range(len(arr)):
        if sum(arr[a+1:]) == sum(arr[:a]):
            return a
    return -1
