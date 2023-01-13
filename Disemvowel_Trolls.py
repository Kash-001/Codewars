def disemvowel(string_: str):
    return ''.join(s for s in string_ if s.lower() not in 'aeiou')
