def find_it(seq: list):
    return [s for s in seq if seq.count(s)%2 != 0][0]
