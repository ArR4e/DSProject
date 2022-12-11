from random import randint

def minu_shuffle(järjend):
    for i in range(0, len(järjend)-1):
        uus_asukoht = randint(0,len(järjend)-1)
        liikuv_element = järjend[i]
        järjend.remove(liikuv_element)
        järjend.insert(uus_asukoht, liikuv_element)
        