def is_pangram(string: str):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for a in alp:
        if a not in string.lower():
            return False
    return True
