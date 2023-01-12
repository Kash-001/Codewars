def is_isogram(string):
    a = 0
    for s in string:
        a += string.count(s)
    return True if a == len(string) else False
