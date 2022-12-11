import random
def minu_shuffle(x):
    z = len(x)
    try:
        y = random.randint(0, (z-1))
    except:
        pass
    try:
        for i in x:
            x[z-1], x[y] = x[y], x[z-1]
            try:
                y = random.randint(0, (z-1))
            except:
                pass
    except:
        pass
