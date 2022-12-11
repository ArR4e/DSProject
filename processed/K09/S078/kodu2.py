from random import randint
def minu_shuffle(järjend):
    i = 0

    while i < len(järjend):
        juhuslik_arv = randint(0, len(järjend)-1)
        juhuslik_arv_2 = randint(0, len(järjend)-1)
        järjend[juhuslik_arv], järjend[juhuslik_arv_2] = järjend[juhuslik_arv_2], järjend[juhuslik_arv]
        i+=1