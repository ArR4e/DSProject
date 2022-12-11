from random import randint

def minu_shuffle(x):
    for i in range (0, len(x)):
        suva=randint(0,len(x)-1)
        suva1=randint(0,len(x)-1)
        while suva == suva1:
            suva1=randint(0,len(x)-1)
        else:
            x[suva], x[suva1] = x[suva1], x[suva]
    return x