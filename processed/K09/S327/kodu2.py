from random import randint
def minu_shuffle(järjend):
    if järjend != []:
        for i in range(0, 100):
            a = randint(0,len(järjend)-1)
            järjend[a-1], järjend[a] = järjend[a], järjend[a-1]

b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
minu_shuffle(b)
print(b)