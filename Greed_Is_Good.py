def score(dice: list):
    score = 0
    while len(dice) != 0:
        for d in dice:
            if dice.count(d) == 3:
                if d == 1:
                    score += d*1000
                    for i in range(3):
                        dice.remove(d)
                else:   
                    score += d*100
                    for i in range(3):
                        dice.remove(d)
            elif d == 1:
                score += 100
                dice.remove(d)
            elif d == 5:
                score += 50
                dice.remove(d)
            else: 
               dice.remove(d)
    return score
