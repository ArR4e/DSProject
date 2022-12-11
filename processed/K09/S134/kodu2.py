from random import randint
def minu_shuffle(järjend):
    for element in järjend:
        juhuslik_arv = randint(0, len(järjend)-1)
        juhuslik_arv2 = randint(0, len(järjend)-1)
        järjend[juhuslik_arv], järjend[juhuslik_arv2] = järjend[juhuslik_arv2], järjend[juhuslik_arv]