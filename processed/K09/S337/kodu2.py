from random import randint
def minu_shuffle(järjend):
    for i in range(len(järjend)-1, 0, -1):
        x = randint(0, i+1)
        järjend[i], järjend[x] = järjend[x], järjend[i]
    return järjend    
