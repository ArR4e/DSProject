from random import randint

def miun_shuffle(järjend):
    for i in range(len(järjend)-1, 0, -1):
        y = randint(0, i)
        järjend[i], järjend[y] = järjend[y], järjend[i]
        