from random import randint

def minu_shuffle(järjend):
    for i in range(len(järjend)):
        eemaldatud=järjend.pop(i)
        järjend.insert(randint(0,len(järjend)),eemaldatud)
    print(järjend)