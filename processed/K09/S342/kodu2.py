from random import randint
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
def minu_shuffle(järjend):
    if järjend == []:
        järjend
    else:
        kordusi = randint(10, 100)
        while kordusi > 0:
             randomnum = randint(0, len(järjend) - 1)
             a = järjend.pop(randomnum)
             järjend.append(a)
             kordusi -= 1
minu_shuffle([])