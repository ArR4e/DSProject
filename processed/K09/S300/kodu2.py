import random
def minu_shuffle(järjend):
    järjendi_viimane_element = len(järjend) - 1
    for element in järjend:
        juhuslik_indeks1 = random.randint(0, järjendi_viimane_element)
        juhuslik_indeks2 = random.randint(0, järjendi_viimane_element)
        järjend[juhuslik_indeks1], järjend[juhuslik_indeks2] = järjend[juhuslik_indeks2], järjend[juhuslik_indeks1]