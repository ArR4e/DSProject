from random import randint

def minu_shuffle(järjend):
    järjendi_pikkus = len(järjend)
    
    i = 0
    for järjendi_element in järjend:
        j = randint(0, järjendi_pikkus-1)
        järjend[i], järjend[j] = järjend[j], järjend[i]
        i+=1   