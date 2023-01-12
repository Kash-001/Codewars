def binary_array_to_number(arr: list):
    fin = ''
    for a in arr:
        fin += str(a)
    return int(fin, 2)
