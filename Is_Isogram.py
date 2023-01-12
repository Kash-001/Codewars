def is_isogram(string: str):
    a, string = 0, string.upper()
    for s in string:
        a = a + string.count(s)
    return True if a == len(string) else False
