# https://www.geeksforgeeks.org/python-ways-to-shuffle-a-list/
import random

def minu_shuffle(jar):
    # käime iga elemendi järjendis läbi.
    for i in range(len(jar)):
        # genereerime talle suvalise indexi.
        ran_i = random.randint(0, len(jar)-1)
        
        # vahetame listis kahe elemendi kohad.
        jar[i], jar[ran_i] = jar[ran_i], jar[i]

    