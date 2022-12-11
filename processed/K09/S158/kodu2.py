import random

def minu_shuffle(jär) :
    for indeks, element in enumerate(jär):
        juhuslik_index = random.randint(0, len(jär)-1)
        jär[juhuslik_index], jär[indeks] == jär[indeks], jär[juhuslik_index]