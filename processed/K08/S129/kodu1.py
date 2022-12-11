#bingo = lambda r=__import__("random"): ((lambda l: l if len (set(l) & {1, 2, 3}) < 3 else bingo()) (r.sample(range(1, 11), 3) +  r.sample(range(11, 21), 2)))

#võtab parameetreid tho



from random import sample

def bingo():
    x = sample(range(1,11), 3)
    y = sample(range(11, 21), 2)
    numbrid = x + y
    if len(set(numbrid) & {1, 2, 3}) < 3:
        return numbrid
    else:
        return bingo()

print(bingo())





