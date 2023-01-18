from collections import Counter
from re import findall, sub

def top_3_words(text):
    count = Counter(findall(r"[a-z']+", sub(r" '+ ", " ", text.lower())))
    return [c for c,_ in count.most_common(3)]
