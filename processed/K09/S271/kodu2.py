from random import randint
def minu_shuffle(x):
    for i in range(len(x)):
        index = randint(0, len(x)-1)
        x[i], x[index] = x[index], x[i]