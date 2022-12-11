import copy
from random import randint

def minu_shuffle(arg):
    arg_copy = copy.deepcopy(arg)
    for i in range(0, len(arg)):
        rng = randint(0, len(arg_copy) - 1)
        arg[i] = arg_copy.pop(rng)