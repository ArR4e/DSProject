from random import randint
def minu_shuffle(jar):
    for nr in range(len(jar)):
        rand = randint(0, len(jar)-1)
        jar[nr], jar[rand] = jar[rand], jar[nr]