def rgb(r, g, b):
    vals = [r,g,b]
    cnt = 0
    for v in vals:
        if v > 255:
            vals[cnt] = 255
        cnt += 1
    cnt = 0
    for v in vals:
        if str(v).isdigit():
            if v != 0: 
                vals[cnt] = hex(v).lstrip("0x").rstrip("L")
                if len(vals[cnt]) != 2:
                    vals[cnt] = '0'+vals[cnt]
            else:
                vals[cnt] = '00' 
        else:
            vals[cnt] = '00'
        cnt += 1
    return ''.join(str(v) for v in vals).upper()
