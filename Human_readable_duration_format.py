def format_duration(seconds: int):
    res = []
    if seconds == 0:
        return 'now'
    if seconds >= 31536000 :
        years = seconds // 31536000
        seconds += -31536000 * years
        yearplu = 's' if years > 1 else ''
        res.append(f'{years} year{yearplu}')
    if seconds >= 86400 :
        days = seconds // 86400
        seconds += -86400 * days
        dayplu = 's' if days > 1 else ''
        res.append(f'{days} day{dayplu}')
    if seconds >= 3600 :
        hours = seconds // 3600
        seconds += -3600 * hours
        hourplu = 's' if hours > 1 else ''
        res.append(f'{hours} hour{hourplu}')
    if seconds >= 60 : 
        mins = seconds // 60
        seconds += -60 * mins
        minplu = 's' if mins > 1 else ''
        res.append(f'{mins} minute{minplu}')
        
    secplu = 's' if seconds > 1 else ''
    et = ' and ' if len(res) > 0 else ''
    data = ', '.join([r for r in res])
    secs = f'{et}{seconds} second{secplu}' if seconds > 0 else ''
    
    return  data+secs
