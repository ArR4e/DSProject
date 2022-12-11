def bingo():
    from random import sample
    s = (sample(range(1, 11), 3))
    while s[0]+ s[1] + s[2] == 6:
        s = (sample(range(1, 11), 3))
    t = (sample(range(11, 21),2))
    v = s+t
    return(v)