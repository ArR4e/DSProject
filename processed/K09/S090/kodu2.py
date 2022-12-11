from random import sample

def minu_shuffle(x):
    y = sample(range(0, len(x)), len(x))
    for i in range(len(x)):
        x[i], x[y[i]] = x[y[i]], x[i] 
