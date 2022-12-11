import random
def minu_shuffle(järjend):
    for i in range(len(järjend)):
        j = random.randint(0, len(järjend)-1)
        element = järjend.pop(j)
        järjend.append(element)
    print(järjend)
