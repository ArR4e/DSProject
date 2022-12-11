import string
import random


def suurväike(lause):
    uus = ''
    kirjavahe = random.choice(string.punctuation)
    for i in lause:
        if i.islower():
            uus += i.upper()
        elif i in string.punctuation:
            i = kirjavahe
            uus += i 
        else:
            uus += i.lower()
    return uus       





