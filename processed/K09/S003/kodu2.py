from random import randint
def minu_shuffle(järjend):
    for i in range(len(järjend)):
        element = järjend.pop(randint(0,len(järjend)-1))
        järjend.append(element)
        
