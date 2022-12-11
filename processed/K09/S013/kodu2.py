import random
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
def minu_shuffle(b):
    for i in b:
        x = len(b) - 1
        rand = random.randint(0, x)
        rand1 = random.randint(0, x)
        b[rand],b[rand1] = b[rand1],b[rand]