from random import randint
def minu_shuffle(järjend):

    for el in järjend:
        suvaline_arv = randint(0, len(järjend)-1)
        suvaline_arv2 = randint(0, len(järjend)-1)
        järjend[suvaline_arv], järjend[suvaline_arv2] = järjend[suvaline_arv2], järjend[suvaline_arv]
    print(järjend)

a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
print(minu_shuffle(a))