from random import randint
def minu_shuffle(järjend):
    c=randint(20, 40)
    n=0
    while n <= c:
        a=randint(0, len(järjend)-1)
        b=randint(0, len(järjend)-1)
        järjend[a], järjend[b] = järjend[b], järjend[a]
        n += 1
    return järjend