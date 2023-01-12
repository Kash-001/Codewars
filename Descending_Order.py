def descending_order(num):
    return int(''.join(str(x) for x in sorted(str(num), reverse=True)))
