Find the smallest integer in the arraydef find_smallest_int(arr: list):
    min = arr[0]
    for a in arr:
        min = a if a < min else min
    return min
