import random

def minu_shuffle(x):
    m = len(x)   
    for element in x:
        if m <= 1:
            break
        else:
            y = random.randint(0, m-1)
            z = random.randint(0, m-1)
            x[y], x[z] = x[z], x[y]
