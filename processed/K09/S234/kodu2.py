from random import randint
def minu_shuffle(järjend):
    for a in range(len(järjend)):
        suvaline=randint(0,len(järjend)-1)
        järjend[a],järjend[suvaline]=järjend[suvaline],järjend[a]