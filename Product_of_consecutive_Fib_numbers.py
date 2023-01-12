def productFib(prod):
    x,y,guess = 0,1,0
    turn = x
    while guess < prod:
        if turn == x:
            x = x + y
            guess = x*y
            turn = y
        else:
            y = y + x
            guess = x*y
            turn = x
    if guess > prod:
        if x > y:
            return [y,x,False]
        else:
            return [x,y,False]
    elif guess == prod:
        if x > y:
            return [y,x,True]
        else:
            return [x,y,True]
