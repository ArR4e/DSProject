from random import randint
def minu_shuffle(järjend):
    if len(järjend) == 1:
        järjend = järjend
    if len(järjend) > 1:
        for i in range(len(järjend)):
            järjend.insert(i,järjend.pop(randint(i,len(järjend)-1)))