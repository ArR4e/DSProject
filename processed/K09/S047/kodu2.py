from random import randint

a = [1, 3, 3, 4, 5, 5, 5, 6 ,6]

def minu_shuffle(järjend):
    uus = []
    for i in range(0, 30):
        number = järjend.pop(randint(0,len(järjend)-1))
        järjend.append(number)
        uus += [number]


print(minu_shuffle(a))
