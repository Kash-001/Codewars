def find_it(seq: list):
    for s in seq:
        if str(seq.count(s)) in '13579':
            return s
