def generate_hashtag(s: str):
    if s.strip() == '':
        return False
    words = s.split(' ')
    if len(words) <= 0:
        return False
    for w in range(len(words)):
        words[w] = words[w].capitalize()
    final = '#'+''.join(str(w) for w in words)
    return final if len(final) < 140 else False
