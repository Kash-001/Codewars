def printer_error(s):
    errors = 0
    for x in s:
        if x not in 'abcdefghijklm':
            errors += 1
    return f'{errors}/{len(s)}'
