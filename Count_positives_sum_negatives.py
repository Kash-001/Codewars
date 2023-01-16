def count_positives_sum_negatives(arr: list):
    rets = [0,0]
    for a in arr:
        if a > 0:
            rets[0] += 1
        elif a < 0:
            rets[1] += a
        else:
            pass
    return rets if arr != [] else [] 
