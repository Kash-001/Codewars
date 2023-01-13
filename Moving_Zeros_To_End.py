def move_zeros(lst: list):
    cnt = lst.count(0)
    lst = [i for i in lst if i != 0]
    for i in range(0,cnt):
        lst.append(0)
    return lst