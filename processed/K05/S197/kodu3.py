def moos(x, y, kg):
    box = 0
    req = 0
    while True:
        if req <= kg - 5 and x > 0:
            req += 5
            box += 1
            x -= 1
            continue
        elif req < kg and y > 0:
            req += 1
            box += 1
            y -= 1
            continue
        elif req == kg:
            return box
        return -1