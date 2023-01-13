def sort_array(numbers: list):
    count = 0
    odds = []
    for n in numbers:
        if n%2 == 1:
            odds.append(n)
    # odds = odds.sort()
    odds = list(sorted(odds))
    for n in numbers:
        if n%2 == 1:
            numbers[count] = odds[0]
            odds.pop(0)
        count += 1
    return numbers

odds = sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
print(odds)