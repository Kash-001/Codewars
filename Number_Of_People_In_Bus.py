def number(bus_stops):
    getin,getout = 0,0
    for pair in bus_stops:
        getin += pair[0]
        getout += pair[1]
    return getin-getout
